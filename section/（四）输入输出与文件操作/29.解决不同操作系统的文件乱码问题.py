"""
@Desc: 解决不同操作系统的文件乱码问题
@Author: Mint.Yan
@Date: 2025-06-171 14:08:07
"""

# 为什么会出现乱码问题？
# 计算机只能处理数字，如果处理文本，就需要把文本按特定规则转换为计算机
# 能够处理的数字，这个过程就被叫做编码
# • 比如你听过的 ASCII 编码，就是把英文字母、数字和常用符号编码成计算机
# 能够认识的特定数字
# • 计算机普及之后，各个国家有不同的标准，比如中国制定的 GBK 编码，
# 一直被 Windows 沿用
# • 为了避免编码混乱，后续产生了统一的 Unicode 编码
# • 其中最广泛使用的 UTF-8 就是 Unicode 的一种实现方式

import os

os.chdir("../../files")

gbk_file = open("GBK乱码案例.txt", "w+", encoding="gbk")
gbk_file.write("这是一个GBK编码的文件\n这是第二行内容")
gbk_file.seek(0)
content = gbk_file.readlines()
print(f"gbk内容：{content}")
gbk_file.close()
