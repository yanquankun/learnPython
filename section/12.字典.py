# 字典

# 什么是字典
# 字典是一个无序的键值对集合，使用花括号{}表示，可理解为js中的对象

# 字典的特点
# 1. 键值对存储
# 2. 键是唯一的，不允许重复
# 3. 无序存储
# 4. 可变类型，可以动态添加或删除键值对
# 5. 支持快速查找

# 字典和集合的区别
# 1. 字典是键值对的集合，而集合是元素的集合。
# 2. 字典中的键是唯一的，而集合中的元素也是唯一的。
# 3. 字典是有序的（Python 3.7及以上版本），而集合是无序的。
# 4. 字典可以通过键快速访问对应的值，而集合不支持键值对的访问。

# 字典的创建
# 1. 使用花括号创建
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print("字典的内容是：", my_dict)

# 2. 使用dict()函数创建
my_dict2 = dict(name='Bob', age=25, city='Los Angeles')
print("使用dict函数创建的字典是：", my_dict2)

# 3. 使用键值对列表创建
my_dict3 = dict([('name', 'Charlie'), ('age', 28), ('city', 'Chicago')])
print("使用键值对列表创建的字典是：", my_dict3)

# 4. 使用zip函数创建
keys = ['name', 'age', 'city']
values = ['David', 22, 'San Francisco']
my_dict4 = dict(zip(keys, values))
print("使用zip函数创建的字典是：", my_dict4)
