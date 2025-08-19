def connect_wifi(ssid, password, timeout=5):
    import network
    import time

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    if not wifi.active():
        print("❌ WiFi 模块激活失败")
        return None

    print('Connecting to network...')
    try:
        wifi.connect(ssid, password)
    except OSError as e:
        print(f"❌ WiFi 连接调用异常: {e}")
        return None

    start_time = time.time()
    while not wifi.isconnected():
        if time.time() - start_time > timeout:
            print(f"❌ Failed to connect to WiFi '{ssid}' within {timeout} seconds.")
            return None
        time.sleep(1)

    print('✅ Network connected:', wifi.ifconfig())
    return wifi


ssid = 'Mint iPhone'  # 替换为你的WiFi名称
password = 'lovemint'  # 替换为你的WiFi密码

wifi = connect_wifi(ssid, password)
if wifi is None:
    print("⚠️ 无法连接到网络，请检查 WiFi 名称和密码。")
