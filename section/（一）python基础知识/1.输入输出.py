"""
@Desc: 本讲解Python内置数据类型的输入输出
@Author: Mint.Yan
@Date: 2025-06-162 15:00:40
"""

def answer():
    # 输出
    print("Hello World")
    # 默认会换行
    print("换行")
    # 使用end内容进行控制
    print("Hello World", end="\n")
    # 不换行
    print("Hello World", end=" ")
    # 换行两次
    print("Hello World", end="\n\n")

    # 输入
    # 通过变量保存输入的值，eg：
    name = input("请输入你的名字：\n")
    age = input("请输入你的年龄：\n")
    # 使用f-string格式化输出
    print(f"你的名字是{name}，你的年龄是{age}")


answer()
