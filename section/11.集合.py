# 什么是集合？
# 集合是一个无序的、不重复的数据集合。它可以用来存储多个元素，并且不允许有重复的元素。

# 集合的特点：
# 1. 无序：集合中的元素没有固定的顺序。
# 2. 不重复：集合中的元素不能重复。
# 3. 可变：集合可以动态添加或删除元素。
# 4. 支持数学运算：集合支持并集、交集、差集等数学运算。

# 集合的类型
# 1. 可变集合：使用set()函数创建，可以添加或删除元素。
# 2. 不可变集合：使用frozenset()函数创建，创建后不能修改。

# 为什么要有不可变集合？
# 不可变集合（frozenset）主要用于需要保证数据不被修改的场景，例如作为字典的键或存储在集合中。

# 集合的创建
my_set = {1, 2, 3, 4, 5}
my_frozenset = frozenset([1, 2, 3, 4, 5])

print("可变集合的内容是：", my_set)
print("不可变集合的内容是：", my_frozenset)

# 集合的基本操作
# 集合的长度
print("集合的长度是：", len(my_set))

# 添加元素
my_set.add(6)
print("添加元素6后的集合是：", my_set)

# 删除元素
my_set.remove(2)  # 如果元素不存在，会抛出KeyError
print("删除元素2后的集合是：", my_set)

# 安全删除元素
my_set.discard(3)  # 如果元素不存在，不会抛出错误
print("安全删除元素3后的集合是：", my_set)

# 弹出元素
popped_element = my_set.pop()
print("弹出元素是：", popped_element)
print("弹出元素后的集合是：", my_set)

# 遍历
for item in my_set:
    print(f"遍历的元素：{item}")

# 清空集合
my_set.clear()
print("清空后的集合是：", my_set)

# 删除集合
del my_set
try:
    print(my_set)
except NameError as e:
    print(f"错误：{e}")

# 集合的数学运算
# 并集
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print("并集的结果是：", union_set)
# 交集
intersection_set = set_a.intersection(set_b)
print("交集的结果是：", intersection_set)
# 差集（注意：a.difference(b)指的是相对于a，b中没有的元素）
difference_set = set_a.difference(set_b)
print("set_a相对于set_b差集的结果是：", difference_set)
# 对称差集
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("对称差集的结果是：", symmetric_difference_set)

# 元组转换为集合(可实现元组去除)
my_tuple = (1, 1, 2, 2, 3, 4)
my_set_from_tuple = set(my_tuple)
print("从元组转换为集合的结果是：", my_set_from_tuple)
tuple_from_set = tuple(my_set_from_tuple)
print("从集合转换为元组的结果是：", tuple_from_set)
