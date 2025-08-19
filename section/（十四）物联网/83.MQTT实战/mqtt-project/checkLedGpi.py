# 用来检测你的esp32是否有I2C接口，是否能连接到OLED屏幕
# 如果有多个I2C接口，可能需要尝试不同的SCL和SDA引脚组合

from machine import Pin, SoftI2C

pairs = [
    (20, 21),
    (21, 20),
    (47, 21),
    (21, 47),
    (48, 21),
    (21, 48),
]

for scl, sda in pairs:
    try:
        i2c = SoftI2C(scl=Pin(scl), sda=Pin(sda), freq=100000)
        addrs = i2c.scan()
        print("try SCL=%d SDA=%d ->" % (scl, sda), addrs)
        if addrs:
            print("FOUND on SCL=%d SDA=%d, addr(s):" % (scl, sda), [hex(a) for a in addrs])
            # 找到就初始化 OLED 测试：
            from ssd1306 import SSD1306_I2C
            oled = SSD1306_I2C(128, 64, i2c, addr=addrs[0])  # 0x3c 或 0x3d
            oled.fill(0)
            oled.text("OK " + hex(addrs[0]), 0, 0)
            oled.show()
            break
    except Exception as e:
        print("err on SCL=%d SDA=%d:" % (scl, sda), e)