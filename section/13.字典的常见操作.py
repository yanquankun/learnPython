my_list = {"name": "Alice", "age": 30, "city": "New York"}

# 字典的内置函数
# 1.访问字典所有元素
print("字典的所有元素是：", my_list.items())  # 输出字典的所有键值对

# 2.访问字典的某个元素
print("字典中name的值是：", my_list.get("name"))  # 输出键name对应的值
print("字典中age的值是：", my_list["age"])

# 3.访问字典的所有键
print("字典的所有键是：", my_list.keys())  # 输出字典的所有键

# 4.访问字典的所有值
print("字"
      "典的所有值是：", my_list.values())  # 输出字典的所有值
# 5.遍历字典
for key, value in my_list.items():
    print(f"键：{key}, 值：{value}")

# 6.字典的长度
print("字典的长度是：", len(my_list))  # 输出字典的键值对数量

# 7.新增键值对
my_list['sex'] = 'male'  # 添加新的键值对
print("新增键值对后的字典是：", my_list)

# 8.删除字典的某个键值对
city_val = my_list.pop("city")  # 删除键city及其对应的值，返回被删除的值
print("删除city后的字典以及被删除的值是：", my_list, city_val)
sex_item = my_list.popitem()  # 删除字典中的最后一个键值对，并返回被删除的键值对
print("删除的字段是：", sex_item)

# 9.是否存在某个键
print("字典中是否存在age键：", 'age' in my_list)  # 检查键age是否存在

# 10.清空字典
my_list.clear()  # 清空字典
print("清空后的字典是：", my_list)

# 字典的高级用法
# 1.字典默认值
my_list.setdefault("country", "USA")  # 如果键country不存在，则添加键country并设置默认值'USA'，否则返回键对应的值
print("添加默认值后的字典是：", my_list)
country_val = my_list.setdefault("country", "USA")
print("country的值是：", country_val)  # 输出键country对应的值

# 2.通过|=运算符合并字典，需要Python 3.9及以上版本
my_dict1 = {"a": 1, "b": 2}
my_dict2 = {"b": 3, "c": 4}
my_dict1 |= my_dict2  # 合并字典my_dict2到my_dict1
print("合并后的字典是：", my_dict1)  # 输出合并后的字典

# 字典与其他数据类型的混合使用
# 1.字典与列表的混合使用
my_list_of_dicts = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 28}
]
print("列表中的字典是：", my_list_of_dicts)  # 输出列表中的字典

# 2.通过zip函数创建字典
keys = ['name', 'age', 'city']
values = ['David', 22, 'San Francisco']
my_dict4 = dict(zip(keys, values))  # 使用zip函数创建字典
print("使用zip函数创建的字典是：", my_dict4)  # 输出使用zip函数创建的字典
