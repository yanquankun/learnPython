"""
@Desc: 本讲解Python内置数据类型的for循环
@Author: Mint.Yan
@Date: 2025-06-164 13:44:32
"""

# for 循环是 Python 中的一种循环结构，用于遍历可迭代对象（如列表、元组、字符串等）中的元素
# for 循环的基本语法如下：
# for variable in iterable:
#     # 执行的代码块
# variable 是循环变量，它将依次取 iterable 中的每个元素

# 下面是一个简单的 for 循环示例
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("当前水果:", fruit)

# 退出循环方式
# 在循环体内，可以使用 break 语句提前退出循环，或者使用 continue 语句跳过当前迭代，继续下一次循环。

# 演示 break 和 continue 的用法
for i in range(10):
    if i == 5:
        print("遇到 5，退出循环")
        break  # 提前退出循环
    if i % 2 == 0:
        print("遇到偶数，跳过这次循环")
        continue  # 跳过当前迭代
    print("当前数字:", i)

# 遍历字典key和value
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# 遍历枚举类型
# 使用 enumerate() 函数可以同时获取索引和元素
person = {"name": "Alice", "age": 30, "city": "New York"}
for index, (key, value) in enumerate(person.items()):
    print(f"索引 {index} - {key}: {value}")

# 推导式
# 列表推导式可以用来生成新的列表
# 推导式格式
# [expression for item in iterable if condition]
# expression 是对每个 item 的处理，iterable 是可迭代对象，condition 是可选的过滤条件

# 下面是一个简单的列表推导式示例
squared_numbers = [x ** 2 for x in range(10)]
print("平方数列表:", squared_numbers)

squared_numbers = [x ** 2 for x in range(10) if x % 2 == 0]
print("平方数列表（仅偶数）:", squared_numbers)

# 练习题
# 请根据以下要求，对该列表进行处理 [ "rachel", "monica", "Phoebe", "joey" ]：
# 1. 需要将该列表按照首字母升序进行排列；
# 2. 需将该列表中的每个元素全部改为大写字母；
# 3. 需输出排序后的序号和列表内容

names = ["rachel", "monica", "Phoebe", "joey"]
# 冒泡排序
# 冒泡排序是一种简单的排序算法，通过重复遍历要排序的列表，比较相邻元素并交换它们的位置，直到列表完全排序。
# 第一层循环控制遍历次数，第二层循环控制相邻元素的比较和交换，每次将最大或最小的元素“冒泡”到列表的一端。
length = len(names)
for i in range(length - 1):
    for j in range(length - i - 1):
        if names[j].lower() > names[j + 1].lower():
            names[j], names[j + 1] = names[j + 1], names[j]
# 将列表中的每个元素改为大写字母
for index, name in enumerate(names):
    print(f"{index + 1}. {name.upper()}")
