# 内置类型
from typing import Generic, TypeVar, Union


# 1.逻辑值检测
def is_true(value):
    """
    检测一个值是否为True
    """
    return bool(value)


# 2.布尔运算
def boolean_operations(a, b):
    """
    返回布尔运算的结果
    """
    return {
        'and': a and b,
        'or': a or b,
        'not': not a
    }


# 3.比较运算
def compare_values(a, b):
    """
    返回两个值的比较结果
    """
    return {
        'equal': a == b,
        'not_equal': a != b,
        'greater_than': a > b,
        'less_than': a < b,
        'greater_than_or_equal': a >= b,
        'less_than_or_equal': a <= b
    }


# 4.数字类型： int float complex
def number_types():
    """
    返回不同数字类型的示例
    """
    return {
        'integer': 42,
        'float': 3.14,
        'complex': 1 + 2j
    }


# 5.迭代器类型
def iterator_types():
    """
    返回迭代器类型的示例
    """
    return {
        'list_iterator': iter([1, 2, 3]),
        'tuple_iterator': iter((1, 2, 3)),
        'set_iterator': iter({1, 2, 3}),
        'dict_iterator': iter({'a': 1, 'b': 2})
    }


# 6.序列类型 list tuple range
def sequence_types():
    """
    返回序列类型的示例
    """
    return {
        'list': [1, 2, 3],  # 储存的值类型可变
        'tuple': (1, 2, 3),  # 储存的值类型不可变
        'range': range(1, 4)  # 返回一个整数序列
    }


# 7 文本序列类型 str
def text_sequence_type():
    """
    返回文本序列类型的示例
    """
    return {
        'string': "Hello, World!"
    }


# 8.二进制序列类型 bytes bytearray memoryview
def binary_sequence_types():
    """
    返回二进制序列类型的示例
    """
    return {
        'bytes': b'Hello',
        'bytearray': bytearray(b'Hello'),
        'memoryview': memoryview(b'Hello')
    }


# 9.集合类型 set frozenset
def set_types():
    """
    返回集合类型的示例
    """
    return {
        'set': {1, 2, 3},
        'frozenset': frozenset([1, 2, 3])
    }


# 10.映射类型 dict
def mapping_type():
    """
    返回映射类型的示例
    """
    return {
        'dictionary': {'key1': 'value1', 'key2': 'value2'}
    }


# 11. 上下文管理器类型
def context_manager_type():
    """
    返回上下文管理器类型的示例
    """

    class MyContextManager:
        def __enter__(self):
            print("Entering context")
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print("Exiting context")

    return MyContextManager()


# 12. 类型注解的类型 Generic Alisa、Union

T = TypeVar('T')


def generic_type_example(value: T) -> T:
    """
    返回传入的值，演示类型注解的使用
    """
    return value


def union_type_example(value: Union[int, str]) -> str:
    """
    返回传入的值的字符串表示，演示联合类型的使用
    """
    return str(value)


# 13.其他类型类型
def other_types():
    """
    返回其他类型的示例
    """
    return {
        'NoneType': None,  # 表示空值
        'Ellipsis': Ellipsis,  # 表示省略号
        'NotImplemented': NotImplemented  # 表示未实现的操作
    }


# 14. 特殊属性
def special_attributes():
    """
    返回特殊属性的示例
    """
    return {
        '__name__': __name__,  # 模块名
        '__doc__': __doc__,  # 模块文档字符串
        '__file__': __file__,  # 模块文件路径
        '__version__': '3.10.7'  # 模块版本
    }
