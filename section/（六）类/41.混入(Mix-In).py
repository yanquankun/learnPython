"""
@Desc: 本讲解如何使用混入（Mix-In）类来实现代码复用和功能扩展
@Author: Mint.Yan
@Date: 2025-07-183 14:37:33
"""


# 使用场景：
# 1. 当需要在多个类中共享相同的功能时，可以使用混入类来封装这些功能。
# 2. 当需要在类之间进行功能扩展时，可以使用混入类来添加额外的方法。
# 3. 当需要避免代码重复时，可以使用混入类来实现通用功能。

# 混入类的特点：
# 1. 不能实例化，而是作为其他类的父类使用。
# 2. 只包含方法，不包含属性。
#     这不是强制规定，Python 并不会因为混入类中有属性而报错。
#     “只包含方法，不包含属性”是混入（Mixin）设计的一种推荐规范，目的是让混入类更专注于功能扩展，避免状态冲突。
#     如果在混入类中定义属性，代码可以正常运行，但可能导致多重继承时属性冲突或覆盖，增加维护难度。
#     所以建议混入类只写方法，不写属性，但不是语法强制。
# 3. 用于提供通用功能，避免代码重复。
# 4. 混入类一般在类名称后增加 Mixin

# 使用场景：
#   1. 当需要在多个类中共享相同的功能时，可以使用混入类来封装这些功能。
#   2. 当需要在类之间进行功能扩展时，可以使用混入类来添加额外的方法。
#   3. 当需要避免代码重复时，可以使用混入类来实现通用功能。

# 使用格式：
# class X(B, CMixin, DMixin)

# 举个🌰

class AMixin:
    """
    混入类 AMixin，提供通用功能
    """

    def common_method(self):  # noqa
        """
        通用方法，所有使用此混入类的类都可以调用
        :return: str, 通用方法的描述
        """
        print("This is a common method from AMixin")


class BMixin:
    """
    混入类 BMixin，提供额外的功能
    """

    def additional_method(self):  # noqa
        """
        额外方法，所有使用此混入类的类都可以调用
        :return: str, 额外方法的描述
        """
        print("This is a addition method from BMixin")


class Base(AMixin, BMixin):
    """
    基类，继承自 AMixin 和 BMixin
    """

    def __init__(self, name):
        """
        初始化方法，创建一个基类实例
        :param name: str, 实例名称
        """
        self.name = name


# 实例化 Base 类并调用混入类的方法
base = Base("Example")
base.common_method()
base.additional_method()

# 总结：
# 混入类是一种设计模式，用于在多个类之间共享功能，避免代码重复。它们不能实例化，只包含方法而不包含属性。通过多重继承，可以将混入类的功能添加到其他类中，从而实现代码复用和功能扩展。
