def connect_wifi(ssid, password):
    import network
    import time

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    if not wifi.isconnected():
        print('Connecting to network...')
        # ssid为WIFI名称
        # password为WIFI密码
        wifi.connect(ssid, password)
        while not wifi.isconnected():
            time.sleep(1)

    print('Network connected:', wifi.ifconfig())

    return wifi


ssid = 'Mint iPhone'  # 替换为你的WiFi名称
password = 'lovemint'  # 替换为你的WiFi密码

wifi = connect_wifi(ssid, password)
