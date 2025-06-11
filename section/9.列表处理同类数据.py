"""
@Desc: 本讲解Python内置数据类型的列表
@Author: Mint.Yan
@Date: 2025-06-162 14:57:24
"""

# 列表
# 释义： 列表是一个有序的集合，可以存储多个元素。列表中的元素可以是不同类型的数据，包括数字、字符串、甚至其他列表
# 特点： 列表是可变的，可以随时添加、删除或修改元素。列表中的元素可以通过索引访问，索引从0开始。

# 创建列表
my_list = [1, 2, '3', 4, 6, '5']
# 访问列表元素
print(f"列表的第一个元素是：{my_list[0]}")  # 输出第一个元素
print(f"列表的最后一个元素是：{my_list[-1]}")  # 输出最后一个元素

# 修改列表元素
my_list[0] = 10
print(f"修改后的第一个元素是：{my_list}")  # 输出修改后的第一个元素

# 添加元素到列表
my_list.append(6)
print(f"添加元素后的列表是：{my_list}")  # 输出添加元素后的列表

# 删除列表元素
my_list.remove(6)
print(f"删除元素6后的列表是：{my_list}")  # 输出删除元素后的列表

# 遍历列表
for item in my_list:
    print(f"遍历的元素：{item}")

# 删除列表中的某个索引
del my_list[2]
print(f"删除索引2后的列表是：{my_list}")

# 列表的长度
print(f"列表的长度是：{len(my_list)}")  # 输出列表的长度

# 列表的切片
print(f"输出列表1-3索引的切片{my_list[1:3]}")  # 输出列表的切片，从索引1到索引3（不包括索引3）
print(f"输出列表0-3索引的切片{my_list[:3]}")  # 输出列表的切片，从开始到索引3（不包括索引3）

# 在索引位置插入元素
my_list.insert(2, 'inserted')
print(f"插入元素后的列表是：{my_list}")  # 输出插入元素后的列表

# 列表扩展元素
my_list.extend([7, 8, 9])
print(f"列表扩展是：{my_list}")  # 输出扩展后的列表长度
my_list.extend('abc')  # 扩展列表，添加字符串中的每个字符
print(f"扩展字符串后的列表是：{my_list}")  # 输出扩展字符串后的列表

# 移除索引位置的元素
my_list.pop(1)  # 移除索引1处的元素
print(f"移除索引1后的列表是：{my_list}")  # 输出移除索引1后的列表
my_list.pop()
print(f"移除最后一个元素后的列表是：{my_list}")  # 输出移除最后一个元素后的列表

# 元素的计数
count_of_3 = my_list.count(3)  # 统计元素3的出现次数
print(f"元素3的出现次数是：{count_of_3}")  # 输出元素3的出现次数

# 列表的反转
my_list.reverse()
print(f"反转后的列表是：{my_list}")  # 输出反转后的列表

# 列表的复制
my_list_copy = my_list.copy()
print(f"复制后的列表是：{my_list_copy}")  # 输出复制后的列表

# 删除列表中的所有元素
my_list.clear()
print(f"删除列表中的所有元素:{my_list}")  # 输出删除列表中的所有元素的列表

# 删除整个列表
try:
    del my_list
    print(my_list)  # 输出提示信息
except NameError as e:
    print(f"删除整个列表打印错误：{e}")

# 转换为列表
string = "Hello, World!"
list_str = list(string)  # 将字符串转换为列表
print(f"将字符串转换为列表：{list_str}")  # 输出列表的长度

# 列表的排序
arr = [3, 1, 5, 6]
arr.sort()
print(arr)
print(f"排序后的列表是：{arr}")  # 输出排序后的列表
arr.sort(reverse=True)  # 逆序排序
print(f"逆序排序后的列表是：{arr}")  # 输出逆序排序后的列表

# sorted排序（不改变原列表）
arr2 = [3, 1, 5, 6]
new_arr2 = sorted(arr2)  # 对列表进行排序
print(f"原列表未改变，排序后的新列表是：{new_arr2}，原列表是{arr2}")  # 输出原列表未改变的排序后的新列表

# 列表推导式 创建列表
s = [x for x in range(0, 10) if x % 2 == 0]  # 创建一个包含0到9之间偶数的列表
print(f"列表推导式创建的偶数列表是：{s}")  # 输出列表推导式创建的列表
