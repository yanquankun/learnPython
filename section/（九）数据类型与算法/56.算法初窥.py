"""
@Desc: 本讲解为python中算法的初窥，主要介绍了算法的基本概念、分类以及常用的算法。
@Author: Mint.Yan
@Date: 2025-07-197 14:29:45
"""

# 为什么需要算法？
# 1. 解决问题：算法是解决问题的步骤和方法。
# 2. 提高效率：好的算法可以提高程序的运行效率，减少资源消耗。
# 3. 可复用性：算法可以被多次使用，减少重复代码。

# 常⻅的几种时间复杂度：
# O(1)
# O(logn)
# O(n)
# O(n*n)

# 下面我们给出一个🌰

# 斐波那契数列的递归实现
from time import time


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(f"计算中")
start = time()
fibonacci_recursive(40)
end = time()
print(f"用时：{end - start}")
# 第一次执行用时 21.59s
# 可以看到用时还是比较长的，主要是因为递归调用的次数太多了

# 进行算法优化：
# LRU 算法 —— LRU（Least Recently Used）最近最少使用
# • functools.cache() —— 轻量级的函数缓存功能装饰器
# • 计算缓存后的时间开销

from functools import cache


@cache
def fibonacci_recursive_cache(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive_cache(n - 1) + fibonacci_recursive_cache(n - 2)


print(f"计算中")
start = time()
fibonacci_recursive_cache(50)
end = time()
print(f"第一次用时：{end - start}")  # 9s

start = time()
fibonacci_recursive_cache(50)
end = time()
print(f"第二次用时：{end - start}")  # 0.2s

# 通过使用缓存，我们可以大大减少计算时间，第一次计算仍然需要较长时间，但第二次计算几乎是瞬间完成的。
