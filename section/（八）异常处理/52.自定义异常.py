"""
@Desc: 本讲解为Python中实现自定义异常处理
@Author: Mint.Yan
@Date: 2025-07-192 13:38:43
"""


# 1. 定义自定义异常类
class CustomError(Exception):
    """自定义异常类"""

    def __init__(self, message):
        super().__init__(message)  # 调用父类的构造函数
        self.message = message

    # 重写 __str__ 方法以提供自定义异常信息
    def __str__(self):
        """返回异常信息"""
        return f"CustomError: {self.message}"


# 2. 使用自定义异常类
def divide(a, b):
    """除法函数，可能抛出自定义异常"""
    if b == 0:
        raise CustomError("除数不能为零")  # 抛出自定义异常
    return a / b


try:
    result = divide(10, 0)  # 尝试除以零
except CustomError as e:
    print(f"捕获到自定义异常：{e}")


# with语句

# 举个🌰
# with open('file.txt', 'w') as f:
#     f.write("Hello, World!")  # 自动处理文件关闭

# with 语句使用了 __enter__() 和 __exit__() 两个方法实现，自定义 with 语句，可以使用如下写法

# 举个🌰
class MyClass:
    def __init__(self, message):
        self.message = message

    # with 语句后的对象会被调用，并将结果返回给 as 语句后的对象
    def __enter__(self):
        print("进入 with 语句块")
        # 注意：as 子句后的变量会被赋值为 __enter__ 方法的返回值！！！
        # 如果想直接mc调用msg属性，可以在这里返回self
        return self

    # with 语句块所有代码执行完，执行此部分代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出 with 语句块")

    @property
    def msg(self):
        """打印消息"""
        return f"消息: {self.message}"


with MyClass("Hello, World!") as mc:
    print(mc.msg)
