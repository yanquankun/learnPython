"""
@Desc: 本讲解如何接收键盘输入
@Author: Mint.Yan
@Date: 2025-06-169 13:47:31
"""

import argparse

# 输入设备与输入方式
# • 交互方式输入：
#     input() 函数
# • 非交互方式输入：
#     命令行参数、文件

# 本节主要讲命令行参数输入方式
#
# 实现参数处理的两个函数库：
# • argparse——用户友好的命令行选项解析器
# https://docs.python.org/zh-cn/3.10/library/argparse.html
# • getopt——C ⻛格命令行选项解析器
# https://docs.python.org/zh-cn/3.10/library/getopt.html
# * 本课程中采用 argparse
# * argparse 库需要 Python3.2 以上版本支持

# argparse 库的使用步骤：
# 1. 创建 ArgumentParser 对象
parser = argparse.ArgumentParser(description="这是一个示例程序")
# 2. 添加必填参数 必填参数按照声明的顺序输入，且不需要前缀
parser.add_argument(
    "name", type=str, help="请输入您的名字"
)
# 3. 添加可选参数，通过 `-` 或 `--` 前缀来标识
parser.add_argument(
    "-a", "--age", type=int, default=18, help="请输入您的年龄，默认为 18"
)

# 4. 解析命令行参数
args = parser.parse_args()

# 5. 使用参数
print(f"获取到的参数, {args}!")

# 执行命令行示例：
# python section/（四）输入输出与文件操作/25.如何接收键盘输入.py Mint.Yan -a 20
# python section/（四）输入输出与文件操作/25.如何接收键盘输入.py Mint.Yan
# python section/（四）输入输出与文件操作/25.如何接收键盘输入.py -h|--help
