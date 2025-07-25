"""
@Desc: 本讲解Python内置数据类型的数和字符串的使用区别
@Author: Mint.Yan
@Date: 2025-06-162 14:57:50
"""

# 区分数据类型及好处
# 1. 强类型编程语言
# 2. 数据类型不会因运算等原因中途改变
# 3. 必须显式改变类型

# 字符串与数字的用途
# 1. 数字用于数学运算、统计分析等
# 2. 字符串用于文本处理、数据存储等

# 字符串比较按字典序进行
print("456" > "1234")  # True

# 不同类型相加会报错
try:
    print(123 + "456")
except TypeError as e:
    print(f"错误：{e}，不能将数字和字符串相加")

# 练习：
# 比较字符串
print("ABC" > "ABD")  # False, 因为"A"相同，"B"相同，但"C"大于"D"
print("123.0" > "123")  # True
print("123.0" == "123")  # False
# 比较字符串和数字会报错
try:
    print("ABC" > 123)
except TypeError as e:
    print(f"错误：{e}，不能比较字符串和数字")
# 浮点数和整数比较
print(3.0 > 3)  # False
