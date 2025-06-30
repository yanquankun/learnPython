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
    res = inner_function(x)
    print(f"The square of {x} is {res}")


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
    print(f"Outside foo: x = {x}")  # type: ignore
    # 这里会报错，因为x在foo函数内部定义
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
# 外部函数和内部函数同时定义，定义和调用都不优雅，定义内部函数的人要修改外部函数的定义，调用需要用两个()进行调用
# 引入 @ 语法（装饰器）实现函数嵌套定义

# eg：
# 获取函数执行时间
import time


# 不使用装饰器的方式
# def work():
#     print("内部函数开始执行")
#     time.sleep(1)
#     print("内部函数执行完成")
#
#
# start = time.time()
# work()
# end = time.time()
# print(f"函数执行时间：{end - start}秒")


# 使用装饰器的方式
# 对公共代码进行封装，避免重复代码
# 格式：
#   声明：
#   def 装饰器函数(func):
#       def 包装函数():
#           func的处理
#       return 包装函数
#   使用：
#   @装饰器函数名
#   被装饰的函数名


def time_decorator(func):
    """
    装饰器函数，用于计算被装饰函数的执行时间
    :param func: 被装饰的函数
    :return: 包装后的函数
    """

    def wrapper():
        """
        包装函数，记录开始时间，调用被装饰函数，记录结束时间，并打印执行时间
        :return: None
        """
        start = time.time()
        func()  # 调用被装饰函数
        end = time.time()
        print(f"函数执行时间：{end - start}秒")

    return wrapper


@time_decorator
def work():
    print("内部函数开始执行")
    time.sleep(1)
    print("内部函数执行完成")


work()

# 自带装饰器
# python内置了一些装饰器，使用了functools模块
# 常用的有：
# @lru_cache：用于缓存函数的返回值，避免重复计算
# @wraps：用于保留被装饰函数的元数据（如函数名、文档字符串等）
# 文档：https://docs.python.org/zh-cn/3.10/library/functools.html

# eg:
from functools import lru_cache, wraps


# 演示@lru_cache装饰器的使用
@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    """
    计算斐波那契数列的第n项
    :param n: int, 斐波那契数列的索引
    :return: int, 第n项的值
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 调用斐波那契函数
start = time.time()
print(f"Fibonacci(10) = {fibonacci(10)}")  # 输出: Fibonacci(10) = 55
end = time.time()
print(f"fibonacci函数第一次执行时间：{end - start}秒")
start = time.time()
print(f"Fibonacci(10) = {fibonacci(10)}")
end = time.time()
print(f"命中fibonacci函数缓存，执行时间：{end - start}秒")  # 输出: 函数执行时间：0.000001秒（缓存命中，几乎没有延迟）


# 演示@wraps装饰器的使用
# 通过装饰器保留函数元数据
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def test():
    pass


print(test.__name__)  # 输出：wrapper，因为my_decorator装饰器改变了函数的名称


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def test():
    pass


print(test.__name__)  # 输出：test，因为@wraps(func)保留了原函数的元数据
