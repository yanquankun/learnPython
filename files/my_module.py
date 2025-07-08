var1 = 100


def my_function():
    print("This is a function in my_module.py")


class MyClass:
    def __init__(self):
        self.attribute = "This is an attribute of MyClass"

    def my_method(self):
        print(self, var1)


# __name__ 是一个特殊变量，用于判断模块是直接运行还是被导入
# 如果模块是直接运行的（而不是被导入），则执行以下代码
if __name__ == '__main__':
    my_function()
# 如果是被导入的模块，则执行以下代码
elif __name__ == "__my_module__":
    print('This module is being imported')
