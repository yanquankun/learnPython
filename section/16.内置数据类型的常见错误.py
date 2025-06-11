# 1.访问错误
# 使用内置方法，访问到某个类型不存在的元素
# • 列表：IndexError: list index out of range
# • 字典： KeyError: 'xxx'
#
# 解决办法：
# 先判断该元素是否存在，再进行操作
# 元素 in 对象

# 2.不同数据类型之间错误报错
# • 不同的数据类型之间，能够支持不同功能但相同写法的运算符，如：
# >、<、==、+、-
# • 不同类型之间操作会出现报错，如：
# >>> 1 + 'a'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 解决办法：
# 转换为相同的类型

# 3.对只读数据类型进行修改报错
# 这种错误经常出现在元组类型中，如：
# >>> t.append('new_element')
# AttributeError: 'tuple' object has no attribute 'append'

# 解决办法：
# 写入前，先判断好类型
# type(t)

# 4.引用错误
# 常⻅于用不可哈希对象作为字典的键
# 典型报错：TypeError: unhashable type: 'list'
# 解决办法：
# 使用元组、字符串、数字作为字典的键

list1 = [1, 2, 3]
tuple1 = ('abc', list1)
print(type(tuple1))
dict1 = {tuple1, 1}
# 会报错 unhashable type: 'list'
# 原因是list是一个不可hash的元素，导致元组整个也是不可哈希的，而字典的key必须为可hash的键，
