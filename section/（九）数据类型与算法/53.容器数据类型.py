"""
@Desc: 本讲解为Python中实现容器数据类型
@Author: Mint.Yan
@Date: 2025-07-195 13:34:22
"""

# 容器数据类型文档：https://docs.python.org/zh-cn/3.10/library/collections.html

# 命名元组（Named Tuple）
# 是一种扩展的元组类型，允许你为元组中的元素指定名称，从而使代码更具可读性和可维护性。
# 为什么要设计这个类型？
# 因为元组是不可变的，且元素只能通过索引访问，使用命名元组可以通过名称访问元素，使代码更清晰和易于理解。

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
point1 = Point(10, 20)
point2 = Point(30, 40)
print(point1, point2)
print(point1.x, point1.y, point2.x, point2.y)

# namedtuple 其实是通过类的方式来实现的，它生成了一个新的类，具有指定的字段名，并且可以像普通对象一样访问这些字段。
# 同样我们也可以通过重写魔术方法实现一些自定义的操作

# 先看一个命名元组加减操作的结果
print(point1 + point2)  # 输出：(10, 20, 30, 40)
try:
    print(point1 - point2)  # noqa
except Exception as e:
    print(f"减法操作失败：{e}")
print("===" * 10)


# 通过重写 __add__ 和 __sub__ 方法来实现命名元组的加减操作
class PointWithOperations(namedtuple("Point", ["x", "y"])):
    def __add__(self, other):
        return PointWithOperations(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return PointWithOperations(self.x - other.x, self.y - other.y)


point1 = PointWithOperations(10, 20)
point2 = PointWithOperations(30, 40)
print(point1 + point2)  # 输出：PointWithOperations(x=40, y=60)
print(point1 - point2)  # 输出：PointWithOperations(x=-20, y=-20)
print("===" * 10)

# 双端队列（Deque）
# 是一种双端队列数据结构，允许在两端高效地添加和删除元素。它是collections模块中的一个类。
# 相比列表多了 appendleft()、popleft()  方法
from collections import deque

d = deque([1, 2, 3, 4, 5])
d.appendleft(0)
d.pop()
print(d)

# 计数器（Counter）
# 是collections模块中的一个类，用于统计可哈希对象的出现次数。它是一个字典的子类，键为元素，值为元素出现的次数。
from collections import Counter

counter = Counter([1, 1, 1, 2, 3])
print(f"Counter: {counter}")  # 输出：Counter: Counter({1: 3, 2: 1, 3: 1})
print(f"1 出现的次数: {counter[1]}")  # 输出：1 出现的次数: 3
counter2 = Counter("hello world")
print(f"Counter: {counter2}")  # 输出：Counter: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(f"l 出现的次数: {counter2['l']}")  # 输出：l 出现的次数: 3
print("===" * 10)

# 字典和列表子类化
# UserDict 类用于字典对象的二次开发
# UserList 类用于列表对象的二次开发
# 当你需要使用字典、列表，而他们又不能完全满足你的需要时，
# 可以通过继承 UserDict 和 UserList，实现增强功能的字典和列表

# 例如我们可以通过继承它们来实现对于 setter 和 getter 方法的拦截

from collections import UserDict, UserList


class MyDict(UserDict):
    """自定义字典类，继承自 UserDict"""

    def __setitem__(self, key, value):
        """重写 __setitem__ 方法，添加自定义逻辑"""
        print(f"设置键 {key} 的值为 {value}")
        super().__setitem__(key, value)  # 调用父类方法

    def __getitem__(self, key):
        """重写 __getitem__ 方法，添加自定义逻辑"""
        print(f"获取键 {key} 的值")
        return super().__getitem__(key)


myDict = MyDict()  # noqa
myDict['a'] = 1  # 设置键 'a' 的值为 1
myDict['a']  # 获取键 'a' 的值 # noqa


class MyList(UserList):
    """自定义列表类，继承自 UserList"""

    def append(self, item):
        """重写 append 方法，添加自定义逻辑"""
        print(f"向列表中添加元素 {item}")
        super().append(item)  # 调用父类方法

    def __getitem__(self, index):
        """重写 __getitem__ 方法，添加自定义逻辑"""
        print(f"获取索引 {index} 的元素")
        return super().__getitem__(index)


myList = MyList()
myList.append(1)  # 向列表中添加元素 1
myList[0]  # 获取索引 0 的元素 # noqa
print("===" * 10)

# 练习题
# 请你编写程序，统计一篇文章中出现频率在前五的单词，并将单词和出现次数一起输出到终端。

article = "this is a test article. This article is for testing the Counter class in Python. This article is a simple test article."


def top_one_words(article):  # noqa
    """统计文章中出现频率前五的单词"""
    words = article.lower().split()  # 将文章转换为小写并分割成单词
    counter = Counter(words)
    top_one = counter.most_common(1)
    return top_one


top_one = top_one_words(article)
print(f"出现频率最高的单词是：{top_one[0][0]}，出现次数为：{top_one[0][1]}")
