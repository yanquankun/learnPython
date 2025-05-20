# 赋值的几种方式
a = b = 2
print(a, b)  # a = 2, b = 2

# 这种方式赋值，变量数量必须等于值数量
c, d = 3, 4
print(c, d)  # c = 3, d = 4

x = y = z = 5
print(x, y, z)  # x = 5, y = 5, z = 5

e = f = 6
print(e, f)  # e = 6, f = 6

# f指向新的内存地址，修改了f，e不变
f = 7
print(e, f)  # e = 6, f = 7

# f和g指向同一个对象
g = {'a': 1}
f = g
print(g)  # g = {'a': 1}
print(f)  # f = {'a': 1}

# g重新指向新的内存地址，f不变
g = {'a': 2}
print(g)  # g = {'a': 2}
print(f)  # f = {'a': 1}

h = {'b': 1}
i = h
print(h)  # h = {'b': 1}
print(i)  # i = {'b': 1}

# h和i指向同一个对象，修改h，i也会改变
# Python 中，字典是可变对象，赋值操作不会创建副本，而是将变量指向同一个对象
# 修改对象的内容会影响所有引用该对象的变量
h['b'] = 2
print(h)  # h = {'b': 2}
print(i)  # i = {'b': 2}

i['b'] = 3
print(h)  # h = {'b': 3}
print(i)  # i = {'b': 3}
