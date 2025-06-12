"""
@Desc: 本讲解Python内置数据类型的字符串
@Author: Mint.Yan
@Date: 2025-06-162 15:00:11
"""

# 字符串表示
# '' or "" or ''' ''' or """ """

# eg
print('hello "python"')
print('''
    hello python
''')

# 变量输出
name = 'python'
print(name)

# 字符串拼接
# f-strings用法： f"{变量名}" 需要py3.6+版本使用
print(f'名字是：{name}')

# 字符串基本API

# 成员运算
#   1. x in s x在s中
#   2. x not in s x不在s中
x = 'a'
y = 'd'
s = 'abc'
if x in s:
    print(f'{x}在{s}中')

if y not in s:
    print(f'{y}不在{s}中')

# 连接运算
#  1. s+t 连接s和t
#  2. s * n 重复n次s

print(x + y)
print(x * 3)

# 切片运算
#  1. s[i] 获取s中第i个字符
#  2. s[i:j] 从s中提取i到j的字符（不包括j）
#  3. s[i:j:k] 从s中提取i到j的字符（不包括j），步长为k（k指     的是每k步视为一个结果，取该结果的第一个字符ƒ）

s = 'hello'
print(s[0])  # h
print(s[4])  # o
print(s[-1])  # 0
print(s[0:4])  # hell
print(s[0:4:20])  # h
print(s[0:4:4])  # h
print(s[0:4:2])  # hl
print(s[0:4:3])  # hl
