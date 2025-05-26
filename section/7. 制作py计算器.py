"""
@Module:
1. 实现两个整数的四则运算
2. 用户输入两个数后，输入运算符
3. 用户输入运算符后，输出结果
@Author: Mint.Yan
@Date: 2025-05-146 14:32:06
"""


def try_again():
    # 使用while循环来确保用户输入的是合法的值
    while True:
        again = input("是否继续计算？(y/n)：").strip().lower()
        if again == 'y':
            calculate()
            break
        elif again == 'n':
            print("感谢使用，再见！")
            break
        else:
            print("无效输入，请输入 'y' 或 'n'。")


def get_operation():
    while True:
        operation = input("请输入运算符 (+, -, *, /)：").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("无效的运算符，请重新输入。")


def get_num(tip):
    while True:
        try:
            num1 = int(input(tip))
            return num1
        except ValueError as e:
            print(f"错误提示：{tip}")


def get_num1():
    return get_num("请输入第一个数字：")


def get_num2():
    return get_num("请输入第二个数字：")


def calculate(num_1=None, num_2=None, operator=""):
    if num_1 is None:
        num1 = get_num1()
    else:
        num1 = num_1

    if num_2 is None:
        num2 = get_num2()
    else:
        num2 = num_2
    operation = operator or get_operation()
    try:
        res = eval(f"{num1} {operation} {num2}")
        print(f"结果是：{res}")
        try_again()
    except ZeroDivisionError:
        print("除数不能为零，请重新输入。")
        calculate(num1)
    except Exception as e:
        print(f"计算发生错误：{e}")
        exit(1)


# calculate()

"""
@Desc: python3.10.7 内置函数文档
@Link: https://docs.python.org/zh-cn/3/library/functions.html
@Author: Mint.Yan
@Date: 2025-05-146 15:55:52
"""

# abs(x) -> 返回数字的绝对值
# aiter(iterable) -> 返回一个异步迭代器对象
# all(iterable) -> 如果 iterable 的所有元素都为真，则返回 True，否则返回 False
# any(iterable) -> 如果 iterable 的任意元素为真，则返回 True，否则返回 False
# bin(x) -> 返回整数 x 的二进制字符串表示
# bool(x) -> 将 x 转换为布尔值
# bytearray([source[, encoding[, errors]]]) -> 返回一个新的字节数组
# bytes([source[, encoding[, errors]]]) -> 返回一个新的字节对象
# callable(object) -> 如果 object 可以被调用，则返回 True，否则返回 False
# chr(i) -> 返回整数 i 对应的 Unicode 字符
# compile(source, filename, mode[, flags[, dont_inherit]]) -> 返回一个代码对象
# complex([real[, imag]]) -> 返回一个复数
# delattr(object, name) -> 删除对象的属性
# dict([mapping-or-iterable]) -> 返回一个新的字典
# dir([object]) -> 返回对象的属性和方法列表
# divmod(a, b) -> 返回一个包含商和余数的元组
# enumerate(iterable[, start]) -> 返回一个枚举对象，包含索引和值
# eval(expression[, globals[, locals]]) -> 执行表达式并返回结果
# exec(object[, globals[, locals]]) -> 执行代码对象或字符串
# filter(function, iterable) -> 返回一个迭代器，包含 iterable 中所有使 function 返回 True 的元素
# float([x]) -> 将 x 转换为浮点数
# format(value[, format_spec]) -> 返回格式化后的字符串
# frozenset([iterable]) -> 返回一个新的不可变集合
# getattr(object, name[, default]) -> 返回对象的属性值
# globals() -> 返回当前全局符号表的字典
# hasattr(object, name) -> 如果对象有指定的属性，则返回 True，否则返回 False
# hash(object) -> 返回对象的哈希值
# help([object]) -> 调用内置的帮助系统
# hex(x) -> 返回整数 x 的十六进制字符串表示
# id(object) -> 返回对象的唯一标识符
# input([prompt]) -> 从标准输入读取一行并返回字符串
# int([x[, base]]) -> 将 x 转换为整数
# isinstance(object, class-or-type) -> 如果对象是指定类或类型的实例，则返回 True，否则返回 False
# issubclass(class, class-or-type) -> 如果 class 是 class-or-type 的子类，则返回 True，否则返回 False
# iter(object[, sentinel]) -> 返回一个迭代器对象
# len(s) -> 返回对象 s 的长度
# list([iterable]) -> 返回一个新的列表
# locals() -> 返回当前局部符号表的字典
# map(function, iterable, ...) -> 返回一个迭代器，应用 function 到 iterable 的每个元素
# max(iterable, *[, key, default]) -> 返回 iterable 中的最大值
# min(iterable, *[, key, default]) -> 返回 iterable 中的最小值
# next(iterator[, default]) -> 返回迭代器的下一个元素
# object() -> 返回一个新的空对象
# oct(x) -> 返回整数 x 的八进制字符串表示
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) -> 返回一个文件对象
# ord(c) -> 返回字符 c 的 Unicode 码点
# pow(x, y[, z]) -> 返回 x 的 y 次幂，如果指定了 z，则返回结果对 z 取模
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> 打印对象到标准输出
# property(fget=None, fset=None, fdel=None, doc=None) -> 返回一个属性对象
# range([start], stop[, step]) -> 返回一个可迭代的整数序列
# repr(object) -> 返回对象的字符串表示
# reversed(seq) -> 返回一个反向迭代器
# round(number[, ndigits]) -> 返回四舍五入后的数字
# set([iterable]) -> 返回一个新的集合
# setattr(object, name, value) -> 设置对象的属性值
# slice(stop) -> 返回一个切片对象
# slice(start, stop[, step]) -> 返回一个切片对象
# sorted(iterable, *, key=None, reverse=False) -> 返回一个排序后的列表
# staticmethod(function) -> 将函数转换为静态方法
# str(object='') -> 返回对象的字符串表示
# sum(iterable[, start]) -> 返回 iterable 中所有元素的和
# super([type[, object-or-type]]) -> 返回一个代理对象，用于调用父类的方法
# tuple([iterable]) -> 返回一个新的元组
# type(object) -> 返回对象的类型
# type(name, bases, dict) -> 返回一个新的类型对象
# vars([object]) -> 返回对象的 __dict__ 属性，如果没有则返回当前局部符号表的字典
# zip(*iterables) -> 返回一个迭代器，聚合多个可迭代对象的元素
# __import__(name[, globals[, locals[, fromlist[, level]]]]) -> 导入模块

# 以上函数可以通过help()函数查看详细文档
