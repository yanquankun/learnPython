"""
@Desc: 本讲解Python中类的魔术方法和装饰器的使用
@Author: Mint.Yan
@Date: 2025-07-188 13:44:34
"""


# 魔术方法（Magic Methods）是Python中以双下划线开头和结尾的方法，用于实现类的特殊行为。
# 官方地址：https://docs.python.org/zh-cn/3/reference/datamodel.html#special-method-names

class Test:
    pass;


# 查询魔术方法：
print(dir(Test))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# 数据类型魔术方法
num = 1
print(dir(num))
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# 举例：
# 求和 __add__
print(num.__add__(2))  # 3


# 重写模式方法
class MyInt(int):
    """
    自定义整数类，重写加法运算符
    """

    def __add__(self, other):
        if isinstance(other, int):
            return myInt(super().__add__(other))
        return 'Unsupported type for addition'


num2 = MyInt(1)
print(num2.__add__('1'))
