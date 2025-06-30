"""
@Desc: 本讲解如何定义和使用高阶函数
@Author: Mint.Yan
@Date: 2025-06-181 13:24:20
"""


# 函数对象和函数调用

# 函数对象是指函数本身的引用，可以将函数作为参数传递给其他函数或将其赋值给变量。
# eg：
def square(x: int = 10) -> int:
    """
    计算平方的函数
    :param x: int, 输入整数
    :return: int, x的平方
    """
    return x * x


# 函数调用
square()

# 函数对象的使用
foo = square  # 将函数赋值给变量foo
print(foo())

print("===" * 10)

# 高阶函数
# 高阶函数是指可以接受函数作为参数或返回一个函数的函数。
# map、filter、reduce等函数都是高阶函数
#  map filter 为内置函数
#  reduce函数需要导入functools模块


numbers = [1, 2, 3, 4, 5]


# 使用map函数将add函数应用于列表中的每个元素
# 格式：map(函数, 可迭代对象1, 可迭代对象2, ...)
#  函数：函数对象、lambda表达式
#  可迭代对象：列表、元组、字符串等
# 作用：对可迭代对象中的每个元素应用函数，并返回一个迭代器
def add(x: int, y: int) -> int:
    """
    求和函数
    :param x: int, 第一个加数
    :param y: int, 第二个加数
    :return: int, 两个数的和
    """
    return x + y


mapped_result = list(map(add, numbers, numbers))  # 将add函数应用于numbers中的每个元素
print("Mapped Result:", mapped_result)  # 输出: Mapped Result: [2, 4, 6, 8, 10]
print(list(map(lambda x: x * 2, numbers)))  # 使用lambda表达式将每个元素乘以2

print("===" * 10)


# 使用filter函数过滤出偶数
# 格式：filter(函数, 可迭代对象)
#  函数：函数对象、lambda表达式
#  可迭代对象：列表、元组、字符串等
def is_even(x: int) -> bool:
    """
    判断是否为偶数的函数
    :param x: int, 输入整数
    :return: bool, 是否为偶数
    """
    return x % 2 == 0


filtered_result = list(filter(is_even, numbers))  # 过滤出偶数
print("Filtered Result:", filtered_result)  # 输出: Filtered Result: [2, 4]

print("===" * 10)

# 使用reduce函数计算列表中所有元素的和
# 格式：reduce(函数, 可迭代对象)
from functools import reduce


def sum_reduce(x: int, y: int) -> int:
    """
    求和函数，用于reduce
    :param x: int, 第一个加数
    :param y: int, 第二个加数
    :return: int, 两个数的和
    """
    return x + y


reduced_result = reduce(sum_reduce, numbers)  # 计算所有元素的和
print("Reduced Result:", reduced_result)  # 输出: Reduced Result: 15

print("===" * 10)

# 偏函数
# 偏函数是指固定函数的某些参数，从而生成一个新的函数。
# 格式：partial(函数, 参数1=值1, 参数2=值2, ...)
# 使用场景：当需要多次调用同一函数但某些参数固定时，可以使用偏函数来简化代码
from functools import partial


def multiply(x: int, y: int) -> int:
    """
    乘法函数
    :param x: int, 第一个乘数
    :param y: int, 第二个乘数
    :return: int, 两个数的积
    """
    return x * y


# 使用partial函数固定y参数为2
double = partial(multiply, y=2)  # 创建一个新的函数，固定y为2
print("Double of 5:", double(5))  # 输出: Double of 5: 10
# 使用partial函数固定x参数为3
triple = partial(multiply, x=3)  # 创建一个新的函数，固定x为3
print("Triple of 5:", triple(y=5))  # 输出: Triple of 5: 15
