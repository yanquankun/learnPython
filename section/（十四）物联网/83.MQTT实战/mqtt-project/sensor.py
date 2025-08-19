from wifi import wifi
from mqtt_pub import connect_mqtt, mqtt_publish_env
import machine
import network
import dht
import ssd1306
import time
import oled_layout

wifiStatu = False if wifi is None else wifi.isconnected()

if wifiStatu:
    print("✅ 已连接网络:", wifi.ifconfig())
else:
    print("❌ 网络未连接")

# 获取mqtt连接状态
qtStatu = connect_mqtt()

# --- 初始化硬件 ---
# DHT22 传感器
dht_pin = machine.Pin(5)
sensor = dht.DHT22(dht_pin)

# OLED 显示 (I2C, SDA=17, SCL=18)
# 此处有坑，我的引脚是 17 和 18，但有些板子可能是 21 和 22，需要你通过checkLedGpi脚本进行检测
i2c = machine.SoftI2C(sda=machine.Pin(17), scl=machine.Pin(18))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


def get_time_string(wifi_on):
    """联网则从网络同步时间，否则用本地 RTC"""
    try:
        if wifi_on:
            import ntptime
            ntptime.settime()

            t = time.localtime()  # 默认是 UTC
        else:
            t = time.localtime(time.time() + 8 * 3600)

        return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
            t[0], t[1], t[2], t[3], t[4], t[5]
        )
    except Exception:
        return "2000-01-01 00:00:00"


while True:
    try:
        # 读取 DHT22
        sensor.measure()
        t = round(sensor.temperature(), 1)
        h = round(sensor.humidity(), 1)
        print(f"{t:.1f}°C, {h:.1f}%")

        now_str = get_time_string(wifiStatu)

        # --- 渲染 OLED ---
        oled_layout.render(oled, t, h, now_str, wifiStatu)

        # 发布 MQTT 消息
        if qtStatu is True:
            mqtt_publish_env(t, h, now_str)

        print(f"{now_str} temp is {t}，humi is {h}");

    except Exception as e:
        print("Error:", e)

    time.sleep(2)
