# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()

print("系统初始化...")

import sys

# blt模块可能会在缓存中，如果希望每次都重新加载，可以在这里删除它
if 'blt' in sys.modules:
    del sys.modules['blt']  # 删除模块缓存
import blt  # 导入蓝牙模块

# 或者使用importlib重新加载模块
# import importlib
# importlib.reload(blt)  # 强制重新加载模块

print("主程序开始运行")
