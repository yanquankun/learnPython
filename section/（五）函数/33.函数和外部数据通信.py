"""
@Desc: 本讲解如何使用函数与外部数据进行通信
@Author: Mint.Yan
@Date: 2025-06-175 13:50:28
"""


# 实参与形参
# 实参是调用函数时传入的值，形参是函数定义时的参数变量
# eg：
def add(a, b):  # 形参
    """
    求和函数
    :param a: int, 第一个加数
    :param b: int, 第二个加数
    :return: int, 两个数的和
    """
    return a + b


# 调用函数
result = add(5, 3)  # 实参


# 类型提示
# python3.5开始支持类型提示，可以在函数定义中指定参数和返回值的类型
# 格式如下：
# def function_name(param1: type, param2: type) -> return_type
# 例如：
def multiply(x: int, y: int) -> int:  # x和y设置了类型，返回值是int类型
    """
    乘法函数
    :param x: int, 第一个乘数
    :param y: int, 第二个乘数
    :return: int, 两个数的积
    """
    return x * y


# multiply的类型提示表示：
# def multiply(x: int, y: int) -> int

# 位置参数
# 可通过指定参数的来进行位置传参
def subtract(a: int, b: int) -> int:
    """
    减法函数
    :param a: int, 被减数
    :param b: int, 减数
    :return: int, 两个数的差
    """
    return a - b


# 调用函数
result_subtract = subtract(b=1, a=2)
# 效果和 subtract(2, 1) 相同
print(f"{result_subtract}")  # 输出: 2 - 1 = 1


# 关键字参数与默认值
# 可以为函数参数设置默认值，这样在调用时可以省略某些参数
def divide(a: int, b: int = 1) -> float:
    """
    除法函数
    :param a: int, 被除数
    :param b: int, 除数，默认为1
    :return: float, 两个数的商
    """
    return a / b


# 调用函数
result_divide = divide(10)  # 使用默认值b=1
result_divide_with_b = divide(10, 2)  # 指定b=2
print(f"10 / 1 = {result_divide}")  # 输出: 10 / 1 = 10.0
print(f"10 / 2 = {result_divide_with_b}")  # 输出: 10 / 2 = 5.0
