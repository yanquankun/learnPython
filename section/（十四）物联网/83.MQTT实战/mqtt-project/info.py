import esp
import esp32
import network
import machine
import gc
import ubinascii

def collect_esp32_info():
    info = {}

    # 芯片唯一 ID
    info['Chip ID'] = ubinascii.hexlify(machine.unique_id()).decode()

    # 芯片核心数（esp32模块提供的方法）
    try:
        info['CPU cores'] = esp32.cpu_frequency()  # 返回 MHz
    except AttributeError:
        info['CPU cores'] = "无法获取（esp32模块不支持）"

    # Flash 大小
    try:
        info['Flash size'] = esp.flash_size() // 1024  # KB
    except AttributeError:
        info['Flash size'] = "无法获取"

    # PSRAM 信息
    try:
        psram_size = esp.psram_size()
        info['PSRAM size'] = psram_size // 1024 if psram_size > 0 else 0
    except AttributeError:
        info['PSRAM size'] = "固件不支持"

    # 内部 RAM 可用
    gc.collect()
    info['Free RAM'] = gc.mem_free() // 1024  # KB

    # MAC 地址
    wlan = network.WLAN(network.STA_IF)
    mac = ubinascii.hexlify(wlan.config('mac'), ':').decode()
    info['MAC'] = mac

    # Wi-Fi 信息
    if wlan.isconnected():
        info['Wi-Fi connected'] = True
        info['IP config'] = wlan.ifconfig()
    else:
        info['Wi-Fi connected'] = False
        info['IP config'] = None

    return info

if __name__ == "__main__":
    esp_info = collect_esp32_info()
    print("=== ESP32 信息 ===")
    for k, v in esp_info.items():
        print(f"{k}: {v}")