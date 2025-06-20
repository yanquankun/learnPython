"""
@Desc: 本讲解如何打开文件
@Author: Mint.Yan
@Date: 2025-06-170 13:53:41
"""

# 使用 open() 函数打开文件
# 参数官方文档：
# https://docs.python.org/zh-cn/3.10/library/functions.html#open
# open() 函数的语法格式：
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# - file：要打开的文件路径
# - mode：文件打开模式，默认为 'r'（只读模式）
#   - 'r'：只读模式（默认）
#   - 'w'：写入模式（会覆盖文件）
#   - 'a'：追加模式（在文件末尾添加内容）
#   - 'b'：二进制模式（用于处理二进制文件）
#   - 't'：文本模式（默认）
#   - '+'：读写模式（可以同时读写文件）
#   - 'x'：独占创建模式（如果文件已存在，则抛出异常）
#   - 'rb'：以二进制只读模式打开文件
#   - 'wb'：以二进制写入模式打开文件（会覆盖文件）
#   - 'ab'：以二进制追加模式打开文件（在文件末尾添加内容）
#   - 'rt'：以文本只读模式打开文件（默认）
#   - 'wt'：以文本写入模式打开文件（会覆盖文件）
#   - 'at'：以文本追加模式打开文件（在文件末尾添加内容）
#   - 'r+'：以读写模式打开文件（可以同时读写文件）
#   - 'w+'：以读写模式打开文件（会覆盖文件）
#   - 'a+'：以读写模式打开文件（在文件末尾添加内容）
#   - 'x+'：以独占创建模式打开文件（如果文件已存在，则抛出异常）
#   - 'rb+'：以二进制读写模式打开文件
#   - 'wb+'：以二进制读写模式打开文件（会覆盖文件）
# - buffering：缓冲策略，默认为 -1（使用系统默认缓冲）
# - encoding：文件编码格式，默认为 None（使用系统默认编码）
#   - 'utf-8'：UTF-8 编码
#   - 'utf-16'：UTF-16 编码
#   - 'ascii'：ASCII 编码
#   - 'gbk'：GBK 编码
# - errors：错误处理方式，默认为 None（使用系统默认错误处理）
# - newline：行结束符，默认为 None（使用系统默认行结束符）
# - closefd：是否关闭文件描述符，默认为 True

file = open("../../files/demo.txt", mode='r', encoding='utf-8')
with file as f:
    content = f.read()
    print(content)

print("===" * 10)

# 文件路径处理
import os

# 获取当前工作目录
current_dir = os.getcwd()
os.chdir("../../files")  # 切换工作目录到文件所在目录
file = open("demo2.txt")
# 读取文件内容
content = file.read()
print(content)
file.close()

print("===" * 10)

# 文件打开模式
# 文件读+最后位置加入新内容模式
file = open("demo3.txt", mode='a+', encoding='utf-8')
file.write("\n新内容")
# 将文件指针移动到文件开头 否则读取的是最后位置指针后的内容，是空数据
file.seek(0)
content = file.read()  # 读取文件内容
print(f"文件已写入新内容:\n{content}")
file.close()

# 最后记得将操作目录切换回原目录
os.chdir(current_dir)  # 切换回原目录
