"""
@Desc: 本讲解如何处理函数参数不固定的情况
@Author: Mint.Yan
@Date: 2025-06-176 13:37:36
"""


# 不定长参数 （可理解为js中的参数解耦）
# * 接收位置参数 接收多个位置参数，参数会被打包成一个元组
# ** 接收关键字参数 没有被定义的参数会被接收为字典

# eg:
def concatenate(*args, **kwargs):
    """
    连接字符串函数
    :param args: str, 可变位置参数，多个字符串
    :param kwargs: str, 可变关键字参数，多个字符串
    :return: str, 连接后的字符串
    """
    print("位置参数:", args)  # 打印位置参数
    print("关键字参数:", kwargs)  # 打印关键字参数
    result = ''.join(args) + ''.join(kwargs.values())
    return result


# 调用函数
result = concatenate("Hello, ", "world", name="!", punctuation="!!!")
print(result)  # 输出: Hello, world! !!!


# 不定长参数的变种：
# 这种只处理第一个和最后一个参数，第二个参数忽略
def xxx(name, *, alisa_name):
    pass


# 函数文档：
print(concatenate.__doc__)
# 输出:
# 连接字符串函数
# :param
# args: str, 可变位置参数，多个字符串
# :param
# kwargs: str, 可变关键字参数，多个字符串
# :return: str, 连接后的字符串

# 函数内省
print(concatenate.__name__)  # 输出函数名: concatenate
print(concatenate.__dir__)  # 输出函数的属性和方法列表
print(dir(concatenate))  # 输出函数的属性和方法列表
