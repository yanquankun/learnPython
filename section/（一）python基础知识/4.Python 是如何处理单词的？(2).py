"""
@Desc: 本讲解Python内置字符串方法的使用
@Author: Mint.Yan
@Date: 2025-06-162 15:00:05
"""

# str.count(sub[, start[, end]]) -> int
# 返回子字符串 sub 在字符串 str 中出现的次数(不包括end位置的字符)

s = '12312'
print(s.count('1'))  # 2
print(s.count('1', 0, 3))  # 1

# str.isalnum() -> bool
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，否则返回 False。

print('123'.isalnum())  # True
print('abc'.isalnum())  # True
print('123abc'.isalnum())  # True

# str.isalpha() -> bool
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False。
print('abc'.isalpha())  # True
print('123'.isalpha())  # False

# str.join(iterable) -> str
# 将字符串中的每个字符连接起来，返回一个新的字符串

print(''.join(['a', 'b', 'c']))  # abc

# str.split([sep[, maxSplit=-1]]) -> list
# 将字符串分割成列表，返回一个新的列表
# sep: 分隔符，默认为空格
# maxSplit: 最大分割次数，默认为-1，表示分割所有

print('abc'.split())  # ['abc']
print('a,b,c'.split(','))  # ['a', 'b', 'c']
print('a,b,c'.split(',', 1))  # ['a', 'b,c']
print('a,b,c'.split(',', 2))  # ['a', 'b', 'c']

# str.startwith(prefix[, start[, end]]) -> bool
# 如果字符串以 prefix 开头则返回 True，否则返回 False

print('abc'.startswith('a'))  # True
print('abc'.startswith('b'))  # False

# str.join(iterable) -> str
# 将字符串中的每个字符连接起来，返回一个新的字符串

print(''.join(['a', 'b', 'c']))  # abc
print(','.join(['a', 'b', 'c']))  # a,b,c

# 字符串所有方法 https://docs.python.org/3/library/stdtypes.html#string-methods
