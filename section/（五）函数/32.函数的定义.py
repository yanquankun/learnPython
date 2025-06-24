"""
@Desc: 本讲解如何定义函数
@Author: Mint.Yan
@Date: 2025-06-175 13:44:24
"""


# 定义一个函数
def greet(name):
    """
    打招呼函数
    :param name: str, 用户名
    :return: None
    """
    print(f"Hello, {name}!")


# 调用函数
greet("Alice")

# 匿名函数
# 通过lambda表达式定义
# 格式: lambda 参数1, 参数2: 表达式

add = lambda x, y: x + y
# 调用匿名函数
result = add(5, 3)
print(f"5 + 3 = {result}")
