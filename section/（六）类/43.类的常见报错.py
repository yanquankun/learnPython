"""
@Desc: 本讲解Python内置数据类型的常见报错
@Author: Mint.Yan
@Date: 2025-07-185 13:38:03
"""


# 1. 语法错误
# • 忘记使用 self 关键字
# • 错误使用 self 与 cls 关键字

# def syntax_error_example():
#     # 语法错误示例：缺少冒号
#     print("Hello, World!"  # 缺少右括号和冒号
#     # 这将导致 SyntaxError: unexpected EOF while parsing

# 语法错误示例：忘记使用 self 关键字
class SyntaxErrorExample:
    """
    示例类，演示语法错误
    """

    def method_without_self():
        """
        错误方法：忘记使用 self 关键字
        :return: None
        """
        print("This method should have 'self' as the first parameter")


# 语法错误示例：错误使用 self 与 cls 关键字
class SyntaxErrorExample:
    """
    示例类，演示语法错误
    """

    def method_with_wrong_self(cls):
        """
        错误方法：错误使用 self 与 cls 关键字
        :param cls: 类本身
        :return: None
        """
        print("This method should use 'self' as the first parameter, not 'cls'")

    @classmethod
    def method_with_wrong_cls(self):
        """
        正确方法：使用 cls 关键字
        :return: None
        """
        print("This method uses 'cls' as the first parameter correctly")

# 2. 设计错误：导致耦合严重，无法拆分
#  类的设计应采用SOLID原则，避免过度耦合
# ‣S 单一职责原则
#   类只负责做一件事，即只有一个职责。即：越小越好
# ‣O 开闭原则
#   类应当对扩展开放，对修改关闭，使其有更好的可维护性
# ‣L 里氏替换原则
#   某个对象使用类的子类时，应当和使用父类有相同的行为，即：对于任何类，客户端都能应该能无差别的使用它的子类，并且不会影响运行时的预期行为
# ‣I  接口隔离原则
#   Python 使用“鸭子类型”实现接口，接口越小越好
# ‣D 依赖倒置原则
#   高层模块不应该依赖低层模块，二者都应该依赖抽象。即：依赖于接口而不是实现
