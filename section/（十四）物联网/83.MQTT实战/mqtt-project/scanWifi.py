# 添加网络诊断功能
def scan_networks():
    import network
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    print("扫描可用WiFi网络...")
    networks = wifi.scan()

    print("可用网络:")
    for i, net in enumerate(networks):
        ssid = net[0].decode()
        channel = net[2]
        rssi = net[3]
        authmode = net[4]

        print(f"{i + 1}. SSID: {ssid}")
        print(f"   信号强度: {rssi} dBm")
        print(f"   频道: {channel}")
        print(f"   加密类型: {authmode}")
        print("---")


# 运行网络扫描
scan_networks()
