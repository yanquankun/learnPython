"""
@Desc: 本讲解Python内置数据类型的多重循环
@Author: Mint.Yan
@Date: 2025-06-167 13:41:50
"""

# 多重循环是指在一个循环内部嵌套另一个循环。Python 支持多重循环，可以使用 for 循环或 while 循环来实现
# 多重循环的基本语法如下：
# for outer_variable in outer_iterable:
#     for inner_variable in inner_iterable:
#         # 执行的代码块
# outer_variable 是外层循环变量，inner_variable 是内层循环变量

# 下面是一个简单的多重循环示例
for i in range(3):  # 外层循环
    for j in range(2):  # 内层循环
        print(f"外层循环变量 i: {i}, 内层循环变量 j: {j}")

print('=' * 20)

# 中止多重循环
# 在多重循环中，可以使用 break 语句提前退出内层循环或外层循环。
# 下面是一个演示 break 语句的多重循环示例
for i in range(3):  # 外层循环
    for j in range(2):  # 内层循环
        if i == 1 and j == 0:
            print("遇到 i=1, j=0，退出内层循环")
            break  # 提前退出内层循环
        print(f"外层循环变量 i: {i}, 内层循环变量 j: {j}")

print('=' * 20)

# python支持和js一样的对外层循环进行命名后，通过命名打断for循环吗？
# Python 不支持像 JavaScript 那样对外层循环进行命名后通过命名打断循环。
# 但是可以使用标志变量或异常来实现类似的效果。
# 下面是一个使用标志变量来实现的示例

outer_loop_flag = True  # 标志变量
for i in range(3):  # 外层循环
    if not outer_loop_flag:
        break  # 如果标志变量为 False，退出外层循环
    for j in range(2):  # 内层循环
        if i == 1 and j == 0:
            print("遇到 i=1, j=0，退出外层循环")
            outer_loop_flag = False  # 设置标志变量为 False
            break  # 提前退出内层循环
        print(f"外层循环变量 i: {i}, 内层循环变量 j: {j}")

print('=' * 20)

# 使用 while 循环实现多重循环
i = 0  # 外层循环变量
while i < 3:  # 外层循环条件
    j = 0  # 内层循环变量
    while j < 2:  # 内层循环条件
        print(f"外层循环变量 i: {i}, 内层循环变量 j: {j}")
        j += 1  # 增加内层循环变量
    i += 1  # 增加外层循环变量

print('=' * 20)

# 处理多维列表
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 遍历多维列表
for row in matrix:  # 遍历每一行
    for element in row:  # 遍历每一行中的元素
        print(element, end=' ')  # 打印元素，end=' ' 用于在同一行打印
    print()  # 打印换行符
