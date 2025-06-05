# 元组

# 基本序列：列表  元组  range
# 1. 元组创建后不可修改
# 2. 二进制数据和文本字符串属于特别定制的附加序列

# 列表为可变序列
# 元组、字符串为不可变序列
# append、pop、insert等会修改序列本身的函数均无法使用

# 为什么使用元组？
# 1. 元组是不可变的，适用于需要保证数据不被修改的场景。
# 2. 元组的存储效率通常高于列表，适用于存储固定数量的数据。
# 3. 元组的执行效率高于列表，尤其在需要频繁访问数据时。

# 创建一个元组
my_tuple = (1, 2, 3, 1, 1, 1, 3, 'a', 'a', 'b', 'c')
print("元组的内容是：", my_tuple)
print("元组的长度是：", len(my_tuple))
print("元组的元素个数是：", my_tuple.count(my_tuple[0]))  # 统计元组中第一个元素的出现次数

# 元组遍历
for item in my_tuple:
    print(f"遍历的元素：{item}")

# 通过tuple函数创建元组，可以将range、列表、字符串等转换为元组
my_tuple2 = tuple([1, 2, 3, 1, 1, 1, 3, 'a', 'a', 'b', 'c'])
print("通过列表创建的元组是：", my_tuple2)
my_tuple3 = tuple(range(1, 10))
print("通过range创建的元组是：", my_tuple3)
my_tuple4 = tuple('hello')
print("通过字符串创建的元组是：", my_tuple4)

# 元组的删除
del my_tuple
# 注意：删除后无法再访问my_tuple
try:
    print(my_tuple)
except NameError as e:
    print(f"错误：{e}")
