# mqtt_pub_retry.py - ESP32版本，带自动重连机制
from umqtt.simple import MQTTClient
import network
import time
import machine

import socket
print(socket.getaddrinfo("broker.emqx.io", 1883))

MAX_RETRIES = 5       # 最大重试次数
RETRY_INTERVAL = 5    # 重试间隔秒数

def check_network():
    """检查网络连接状态"""
    wifi = network.WLAN(network.STA_IF)
    if wifi.isconnected():
        print("网络已连接:", wifi.ifconfig())
        return True
    else:
        print("网络未连接")
        return False

def mqtt_test_with_retry():
    """测试MQTT连接和发布，支持自动重连"""
    if not check_network():
        return

    server = "broker.emqx.io"
    port = 1883
    client_id = "esp32_client_" + str(machine.unique_id().hex())
    topic = b"temp_topic"

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"\n尝试连接MQTT服务器 ({attempt}/{MAX_RETRIES}): {server}:{port}")
            print(f"客户端ID: {client_id}")

            client = MQTTClient(client_id, server, port)
            client.connect()
            print("✓ MQTT连接成功!")

            message = f"Hello from ESP32! Time: {time.ticks_ms()}"
            print(f"发布消息到主题 '{topic.decode()}' 内容: {message}")
            client.publish(topic, message.encode())
            print("✓ 消息发布成功!")

            client.disconnect()
            print("✓ MQTT连接已断开")
            break  # 成功连接并发布后退出循环

        except OSError as e:
            error_code = e.args[0] if e.args else 0
            print(f"✗ MQTT连接错误: {e}")

            if error_code == 113:  # ECONNABORTED
                print("  原因: 连接被中断")
                print("  建议: 检查网络稳定性和防火墙设置")
            elif error_code == 110:  # ETIMEDOUT
                print("  原因: 连接超时")
                print("  建议: 检查服务器地址和端口")
            elif error_code == -2:  # Name resolution failed
                print("  原因: DNS解析失败")
                print("  建议: 检查DNS设置")
            else:
                print(f"  错误代码: {error_code}")

            if attempt < MAX_RETRIES:
                print(f"  等待 {RETRY_INTERVAL} 秒后重试...")
                time.sleep(RETRY_INTERVAL)
            else:
                print("  已达到最大重试次数，停止尝试。")

        except Exception as e:
            print(f"✗ 其他错误: {e}")
            break  # 对于未知错误直接退出循环

# 运行测试
print("=== MQTT测试开始 ===")
mqtt_test_with_retry()
print("=== MQTT测试结束 ===")