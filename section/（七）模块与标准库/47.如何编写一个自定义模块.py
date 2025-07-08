"""
@Desc: 本讲解Python中类的魔术方法和装饰器的使用
@Author: Mint.Yan
@Date: 2025-07-189 13:51:15
"""
import importlib

# 创建自定义模块
# • 使用以 .py 为结尾的文件名保存模块
# • 在文件中定义的属性、函数都可以被调用
# • 在文件中定义的类可以在引用模块时进行实例化

# 注意事项！！！
# 1. 导入自定义模块时，需确保导入路径正确
# 2. 自定义模块的文件名称尽量避免特殊字符，文件名应避免和标准库重名
# 3. 自定义模块多次导入，模块中的代码也只能被执行一次
# 4. 自定义模块中应为函数定义，避免在模块中编写函数调用代码，或将函数
# 调用代码放在 __name__ 代码块中

# 举个🌰：
# 在files目录中创建一个名为 my_module.py 的文件

# 如何导入自定义模块？？？
# case1：
# 同级别目录的可以直接导入
# import my_module

# case2：
# 非同级目录
# 1. 使用 sys.path.append() 添加路径

# 2. 使用 importlib.import_module() 动态导入模块

# 3. 使用包结构 + 相对导入（仅适用于包内部）
#     如果目录有 __init__.py 文件，可以使用相对路径导入
#     # utils/helpers.py
#     def say_hello():
#         print("hello")
#
#     # scripts/main.py
#     from ..utils import helpers  # 相对导入（必须是模块或包）

# 4. 设置环境变量 PYTHONPATH
#     在运行脚本前，设置环境变量，告诉解释器去额外的路径中找模块：
#     export PYTHONPATH=/your/custom/path
#     python your_script.py
#     或一行写法：
#     PYTHONPATH=/your/custom/path python your_script.py

import sys
import os

# print(__file__) # 获取当前工作目录
# print(os.path.abspath(__file__)) # 获取当前工作目录
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../files'))

# 导入自定义模块 (位置：../../files/my_module.py)
import my_module as t  # noqa

t.my_function()
myClass = t.MyClass()
myClass.my_method()  # 输出：<__main__.MyClass object at 0x101adbc70> 100
