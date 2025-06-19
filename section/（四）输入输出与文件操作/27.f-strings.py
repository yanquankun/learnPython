"""
@Desc: 本讲解如何使用 f-strings 格式化输出
@Author: Mint.Yan
@Date: 2025-06-170 13:41:03
"""

# f-strings 是 Python3.6 版本引入的一种格式化字符串的方式
# 它允许在字符串中直接嵌入表达式，使用大括号 {} 包裹表达式，
# 并在字符串前加上字母 f 或 F。

# f-strings 的优点：
# - 更加简洁和易读
# - 支持表达式计算
# - 支持多行字符串

# 官方文档：
# https://docs.python.org/zh-cn/3.10/reference/lexical_analysis.html#f-strings

name = "Mint.Yan"
age = 18
height = 1.75
print(f"My name is {name}, I am {age} years old, and my height is {height} meters.")

# 支持表达式计算
print(f"My age in months is {age * 12}.")


# 支持函数调用
def greet(name):
    return f"Hello, {name}!"


print(f"{greet(name)} I am {age} years old.")

# 支持多行字符串
multiline_string = f"""
This is a multi-line string.
It supports f-strings too.
My name is {name}.
My age is {age}.
"""
print(multiline_string)

# 宽度和精度调整
pi = 3.141592653589793
print(f"Pi is approximately {pi:.2f}.")  # 保留两位小数
print(f"Pi is approximately {pi:10.2f}.")  # 总宽度为10，保留两位小数
print(f"Pi is approximately {pi:010.2f}.")  # 总宽度为10，前面补0，保留两位小数
print(f"{123.456:010}")  # 总宽度为10，前面补0

