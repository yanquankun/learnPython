# mqtt_pub.py — minimal MQTT helper for ESP32/MicroPython
# Responsibilities:
#   1) connect_mqtt(...) : establish a global MQTT client
#   2) mqtt_publish_env(temp, humi, timestamp, mqtt_topic=...) : publish JSON once
#      (only if connected; otherwise return False)

from umqtt.simple import MQTTClient
import machine
import network
import ujson

# ---- Module-global MQTT client ----
_mqtt_client = None

# ---- Defaults (can be overridden via function args) ----
MQTT_SERVER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = b"esp32/senor"


def connect_mqtt(mqtt_server=MQTT_SERVER, mqtt_port=MQTT_PORT, client_id=None):
    """Connect to MQTT and keep a global client. Return True on success, False otherwise."""
    global _mqtt_client
    if client_id is None:
        try:
            client_id = "esp32_" + machine.unique_id().hex()
        except Exception:
            client_id = "esp32_client"
    try:
        c = MQTTClient(client_id, mqtt_server, mqtt_port)
        c.connect()
        _mqtt_client = c
        print("✓ MQTT已连接: {}:{} (client_id={})".format(mqtt_server, mqtt_port, client_id))
        return True
    except Exception as e:
        print("✗ MQTT连接失败:", e)
        _mqtt_client = None
        return False


def mqtt_publish_env(temp, humi, timestamp, mqtt_topic=MQTT_TOPIC):
    """Publish one JSON message {temperature_c, humidity_pct, timestamp}.
    Only works when MQTT is connected (via connect_mqtt). Returns True/False.
    """
    global _mqtt_client
    if _mqtt_client is None:
        print("✗ 未连接MQTT，放弃发布")
        return False
    try:
        payload = {
            "temperature_c": None if temp is None else round(float(temp), 1),
            "humidity_pct": None if humi is None else round(float(humi), 1),
            "timestamp": str(timestamp or ""),
        }
        msg = ujson.dumps(payload)
        topic = mqtt_topic if isinstance(mqtt_topic, (bytes, bytearray)) else str(mqtt_topic).encode()
        _mqtt_client.publish(topic, msg)
        print("✓ 发布成功 -> {}: {}".format(topic.decode(), msg))
        return True
    except Exception as e:
        print("✗ 发布失败:", e)
        return False
