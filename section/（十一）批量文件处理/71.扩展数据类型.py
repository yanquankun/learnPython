"""
@Desc: 扩展数据类型
@Author: Mint.Yan
@Date: 2025-07-212 15:31:53
"""

# collections官网地址：https://docs.python.org/zh-cn/3/library/collections.html
# collections库为我们提供了多种扩展数据类型，这些数据类型在标准库的基础上提供了更多的功能和灵活性。以下是一些常用的扩展数据类型：

# 命名元组
# 命名元组（namedtuple）是一个工厂函数，用于创建一个具有命名字段的元组子类。它可以让你使用点号访问字段，而不是通过索引访问
# 这使得代码更具可读性和可维护性
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p)  # 输出：Point(x=10, y=20)

# 双端队列
# 双端队列（deque）是一个双端队列实现，允许在两端高效地添加和删除元素
# 它比列表更适合于需要频繁在两端操作的场景
from collections import deque

d = deque([1, 2, 3])
d.append(4)  # 在右端添加元素
d.appendleft(0)  # 在左端添加元素
print(d)  # 输出：deque([0, 1, 2, 3, 4])
d.pop()  # 从右端删除元素
d.popleft()  # 从左端删除元素
print(d)  # 输出：deque([1, 2, 3])

# 计数器
# 计数器（Counter）是一个字典子类，用于计数可哈希对象的出现次数
# 它提供了一个简单的方式来统计元素的频率
from collections import Counter

c = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(c)  # 输出：Counter({'apple': 3, 'banana': 2, 'orange': 1})

# 字典和列表子类化
# defaultdict 是一个字典子类，它提供了一个默认值，当访问不存在的键时返回该默认值
from collections import defaultdict

d = defaultdict(int)  # 默认值为 0
d['a'] += 1  # 如果 'a' 不存在，则默认值为 0
d['b'] += 2  # 如果 'b' 不存在，则默认值为 0
print(d)  # 输出：defaultdict(<class 'int'>, {'a': 1, 'b': 2})

# UserDict 和 UserList
# UserDict 和 UserList 是字典和列表的子类，允许你创建自定义的字典和列表类
# 这对于需要扩展标准字典或列表的功能时非常有用
from collections import UserDict, UserList


class MyDict(UserDict):
    def __getitem__(self, key):
        print(f"Accessing key: {key}")
        return super().__getitem__(key)


class MyList(UserList):
    def append(self, item):
        print(f"Appending item: {item}")
        super().append(item)


# 使用自定义的字典和列表
my_dict = MyDict({'a': 1, 'b': 2})
print(my_dict['a'])  # 输出：Accessing key: a \n 1
my_list = MyList([1, 2, 3])
my_list.append(4)  # 输出：Appending item: 4
print(my_list)  # 输出：[1, 2, 3, 4]

# OrderedDict
# OrderedDict 是一个有序字典，它保持元素的插入顺序
# 在 Python 3.7 及更高版本中，标准字典已经是有序的，但 OrderedDict 仍然可以用于需要显式有序字典的场景
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)  # 输出：OrderedDict([('a', 1), ('b', 2), ('c', 3)])
