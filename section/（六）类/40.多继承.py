"""
@Desc: 本讲解处理类有多个继承的情况
@Author: Mint.Yan
@Date: 2025-07-183 14:20:48
"""


# 类的多继承：
#   • 菱形继承时，Python 会按照 C3 算法（有向无环路图）按顺序遍历继承图
#   • 通过类对象名称.__mro__ 可以查看继承顺序
#   • 多重继承增加了继承的复杂度，应当减少多重继承的使用

# 注意：
#   1. 多继承可能导致菱形继承问题，即多个父类有相同的祖先类
#   2. Python 使用 C3 算法来解决菱形继承问题，确保每个类只被调用一次
#   3. 在多继承中，使用 super() 函数可以确保正确调用父类的方法
#   4. 多继承中类的实例化顺序为从左到右，从上到下

# 举个🌰
# Class D 继承自 Class B 和 Class C，Class B 和 Class C 都继承自 Class A，构成了菱形继承结构
# 类实例化的顺序为：先调用 Class A 的 __init__ 方法，然后 Class B 的 __init__ 方法，最后 Class C 的 __init__ 方法，最后 Class D 的 __init__ 方法

class A:
    """
    父类 A
    """

    def __init__(self):
        print("A's __init__ called")

    def method_a(self):  # noqa
        print(f"Method from A")


class B(A):
    """
    子类 B 继承自 A
    """

    def __init__(self):
        super().__init__()  # 调用父类 A 的初始化方法
        print("B's __init__ called")

    def method_b(self):  # noqa
        print("Method from B")


class C(A):
    """
    子类 C 继承自 A
    """

    def __init__(self):
        super().__init__()  # 调用父类 A 的初始化方法
        print("C's __init__ called")

    def method_c(self):  # noqa
        print("Method from C")


class D(B, C):
    """
    子类 D 继承自 B 和 C
    """

    def __init__(self):
        super().__init__()  # 调用父类 B 的初始化方法
        print("D's __init__ called")

    def method_d(self):  # noqa
        print("Method from D")


# 创建 D 的实例
d_instance = D()
# 调用方法
d_instance.method_d()
d_instance.method_b()
d_instance.method_c()
d_instance.method_a()

print("===" * 10)

# 查看继承顺序
print(D.__mro__)  # 输出继承顺序
