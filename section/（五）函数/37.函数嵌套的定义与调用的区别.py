"""
@Desc: 本讲解函数嵌套的定义与调用
@Author: Mint.Yan
@Date: 2025-06-181 13:47:23
"""


# 先来一个🌰：
# 函数嵌套
def outer_function(x: int):
    """
    外部函数，接受一个整数参数
    :param x: int, 输入整数
    :return: None
    """

    def inner_function(y: int):
        """
        内部函数，接受一个整数参数并返回其平方
        :param y: int, 输入整数
        :return: int, y的平方
        """
        return y * y

    # 调用内部函数并打印结果
    result = inner_function(x)
    print(f"The square of {x} is {result}")


# 调用外部函数
outer_function(5)

# 变量作用域
# 在函数内部定义的变量只能在该函数内部访问，外部无法访问
# eg：
try:
    def foo():
        """
        函数foo，尝试访问内部变量x
        :return: None
        """
        x = 10
        print(f"Inside foo: x = {x}")


    foo()
    print(f"Outside foo: x = {x}")  # 这里会报错，因为x在foo函数内部定义
except NameError as e:
    print(f"OutSide call Error: {e}")


# LEGB原则：
# L: Local（局部作用域） - 函数内部定义的变量
# E: Enclosing（嵌套作用域） - 嵌套函数的外部函数作用域
# G: Global（全局作用域） - 模块级别的变量
# B: Built-in（内置作用域） - Python内置的变量和函数
# 读取顺序：
# 1. Local（局部作用域）
# 2. Enclosing（嵌套作用域）
# 3. Global（全局作用域）
# 4. Built-in（内置作用域）
# 5. 报错

# 闭包
# 闭包是指一个函数可以访问其外部函数的变量，即使外部函数已经返回。
def make_multiplier(factor: int):
    """
    创建一个乘法器函数
    :param factor: int, 乘数因子
    :return: 函数，接受一个整数并返回其与因子的乘积
    """

    def multiplier(x: int):
        """
        内部函数，接受一个整数并返回其与因子的乘积
        :param x: int, 输入整数
        :return: int, x与因子的乘积
        """
        return x * factor

    return multiplier


# 调用make_multiplier函数，创建一个乘法器
multiply_by_3 = make_multiplier(3)
# 调用乘法器函数
result = multiply_by_3(5)  # 5 * 3
print(f"5 multiplied by 3 is {result}")  # 输出: 5 multiplied by 3 is 15
# 直接调用也可以
print(f"5 multiplied by 3 is {make_multiplier(3)(5)}")  # 输出: 5 multiplied by 3 is 15

# 装饰器语法


# 自带装饰器
