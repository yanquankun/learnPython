"""
@Desc: 本讲解Python中类的魔术方法和装饰器的使用
@Author: Mint.Yan
@Date: 2025-07-188 14:04:20
"""

# pycharm 标准库组件目录：
# https://docs.python.org/zh-cn/3/library/index.html

# 内置函数、类型、异常
# 文本处理
# 数字
# 文件和目录
# 通用操作系统
# 并发执行
# 网络和进程间通信
# 互联网协议

# 使用标准库文档：
# 通过 Python 模拟浏览器访问 http://www.baidu.com

# 实现步骤：
# 1. 通过官方文档找到互联网协议和支持
# 2. 找到 HTTP、urllib 目录参考
# 3. 最终确定 urllib.request 可以实现相应功能
# 4. 参考文档中的“例子”和 urlopen() 函数的参数说明，实现模拟浏览器的目的
# * 官方文档：
# https://docs.python.org/zh-cn/3.10/library/urllib.request.html#examples

import urllib.request

print(urllib.request.urlopen('http://www.baidu.com').read(300))
