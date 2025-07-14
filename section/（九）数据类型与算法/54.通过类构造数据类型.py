"""
@Desc: 本讲解为Python中实现高级数据类型与算法
@Author: Mint.Yan
@Date: 2025-07-195 13:53:00
"""

# 魔术方法的作用
# 魔术方法（Magic Methods）是Python中以双下划线开头和结尾的方法，用于实现特定的操作或行为。
# 这些方法通常用于重载运算符、实现对象的字符串表示、比较等功能。

# 举个🌰

dict1 = {'a': 1}
print(dict1['a'])
print(dict1.__getitem__('a'))
try:
    print(dict1['c'])  # 如果键不存在，会抛出 KeyError 异常
except KeyError as e:
    print(f"捕获到异常：{e}")


# 如果你需要重写字典取值过程，可以通过 __getitem__() 魔术方法来实现

# 如果你不知道有哪些魔术方法，可以使用 dir() 函数查看对象的所有属性和方法
# print(dir(dict))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# 通过重写 __getitem__() 方法来实现自定义字典取值过程
# 同时解决 KeyError 异常的处理
class CustomDict(dict):
    def __getitem__(self, key):
        if key in self:
            print(f"获取键 '{key}' 的值")
            return super().__getitem__(key)  # 调用父类的 __getitem__ 方法
        else:
            print(f"键 '{key}' 不存在")
            return None  # 如果键不存在，返回 None


custom_dict = CustomDict({'a': 1, 'b': 2})
custom_dict['a']  # noqa
custom_dict['c']  # noqa
print(custom_dict['c'])  # None
