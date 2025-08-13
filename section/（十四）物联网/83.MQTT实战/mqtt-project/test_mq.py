import usocket
s = usocket.socket()
s.settimeout(20)
try:
    print("TCP CONNECT TEST")
    s.connect(("broker.emqx.io", 1883))
    print("TCP测试 连接成功")
except Exception as e:
    print("TCP测试 连接失败:", e)
finally:
    s.close()