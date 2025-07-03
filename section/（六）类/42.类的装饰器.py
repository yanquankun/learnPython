"""
@Desc: 本讲解Python内置数据类型的装饰器
@Author: Mint.Yan
@Date: 2025-07-184 13:42:30
"""


# 装饰器是Python中的一种特殊语法，用于在函数或方法定义时添加额外的功能。

# classmethod
# 是 Python 中的装饰器之一，用于将一个方法转换为类方法
# 类方法是绑定到类而不是实例的方法，可以通过类名调用
# 注意：类方法的第一个参数通常是 cls，表示类本身，而不是实例对象
# 使用场景：
# 当需要访问类的属性或方法时，可以使用类方法

def class_method_decorator(func):
    def wrapper(*args, **kwargs):
        print("This is a class method decorator")
        return func(*args, **kwargs)

    return wrapper


class MyClass:
    """
    示例类，演示 classmethod 装饰器的使用
    """

    @classmethod
    @class_method_decorator
    def my_class_method(cls):
        """
        类方法，使用 classmethod 装饰器
        :return: str, 类方法的描述
        """
        return "This is a class method"


# 使用示例
print(MyClass.my_class_method())


# staticmethod
# 是 Python 中的装饰器之一，用于将一个方法转换为静态方法
# 使用场景：
# 不需要类的任何信息但又和类相关的一些方法，为了方便维护代码并保持代码工整，可以将该函数定义到类中并使用 staticmethod 修饰

class StaticMethodExample:
    """
    示例类，演示 staticmethod 装饰器的使用
    """

    @staticmethod
    def my_static_method():
        """
        静态方法，使用 staticmethod 装饰器
        :return: str, 静态方法的描述
        """
        return "This is a static method"


print(StaticMethodExample.my_static_method());


# property
# 是 Python 中的装饰器之一，用于将一个方法转换为属性
# 注意：
# 使用 property 装饰器时，方法名不能以 _ 开头，否则会被认为是私有属性
# 使用场景：
# property 装饰器可以让我们像访问属性一样访问方法，提供了一种更简洁的方式来访问类的私有属性
# 通过 property 装饰器，我们可以在访问属性时添加额外的逻辑，比如验证、转换等，而不需要修改类的接口

class PropertyExample:
    """
    示例类，演示 property 装饰器的使用
    """

    def __init__(self):
        """
        初始化方法，设置私有属性
        """
        self.__value = 0

    @property
    def value(self):
        """
        属性方法，使用 property 装饰器
        :return: int, 属性值
        """
        return self.__value

    @value.setter
    def value(self, new_value):
        """
        属性设置方法，使用 property 装饰器
        :param new_value: int, 新的属性值
        """
        # 这里可以添加验证逻辑
        if not isinstance(new_value, int):
            raise ValueError("Value must be an integer")
        self.__value = new_value


property_ins = PropertyExample()
print(f"value init：{property_ins.value}")
property_ins.value = 42  # 设置属性值
print(f"value update：{property_ins.value}")  # 获取属性值，输出: 42
try:
    property_ins.value = "not an int"  # 尝试设置非整数值
except ValueError as e:
    print(f"trigger a type error: {e}")
