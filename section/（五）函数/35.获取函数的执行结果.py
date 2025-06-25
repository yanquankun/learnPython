"""
@Desc: 本讲解如何获取函数的执行结果
@Author: Mint.Yan
@Date: 2025-06-176 13:53:50
"""


# 通过return语句获取函数的执行结果

def calculate_sum(a: int, b: int) -> int:
    """
    求和函数
    :param a: int, 第一个加数
    :param b: int, 第二个加数
    :return: int, 两个数的和
    """
    return a + b


# 调用函数并获取结果
result = calculate_sum(10, 5)
# 输出结果
print(f"10 + 5 = {result}")  # 输出: 10 + 5 = 15


# 递归
# eg：求阶乘
def factorial(n: int) -> int:
    """
    计算阶乘的递归函数
    :param n: int, 非负整数
    :return: int, n的阶乘
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 调用递归函数并获取结果
result_factorial = factorial(5)
# 输出结果
print(f"5! = {result_factorial}")  # 输出: 5! = 120
