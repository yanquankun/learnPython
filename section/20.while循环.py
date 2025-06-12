"""
@Desc: 本讲解Python内置数据类型的while循环
@Author: Mint.Yan
@Date: 2025-06-163 13:49:48
"""
from random import randint

# while 循环是 Python 中的一种循环结构，用于在满足特定条件时重复执行一段代码。

# while 循环的基本语法如下：
# while condition:
#     # 执行的代码块

# condition 是一个布尔表达式，当其值为 True 时，循环继续执行；当其值为 False 时，循环结束。
# 在循环体内，可以使用 break 语句提前退出循环，或者使用 continue 语句跳过当前迭代，继续下一次循环。

# 下面是一个简单的 while 循环示例
count = 0
while count < 5:
    print("当前计数:", count)
    count += 1  # 增加计数
print("循环结束，最终计数:", count)

# 演示 break 和 continue 的用法
count = 0
while count < 10:
    count += 1
    if count == 5:
        print("遇到 5，跳过这次循环")
        continue  # 跳过当前迭代
    if count == 8:
        print("遇到 8，退出循环")
        break  # 提前退出循环
    print("当前计数:", count)

# 使用标志退出循环
flag = True
while flag:
    user_input = input("输入 'exit' 退出循环：")
    if user_input.lower() == 'exit':
        print("用户选择退出循环")
        flag = False  # 设置标志为 False，退出循环
    else:
        print(f"你输入的是: {user_input}")

# 死循环
# while True:
#     print("这是一个死循环，按 Ctrl+C 退出")

# 编写一个猜数字的游戏程序。随机产生一个 100 以内的整数，并要求用户输入三次数据，当任意一次输入的数字和随机数相同，游戏结束。否则需程序运行
# 三次后，提示正确答案，退出程序。
# 提示： 使用 random.randint(1, 10) 函数，可以产生指定范围的随机数


random_num = randint(1, 100)
print(f"欢迎来到猜数字游戏！答案是{random_num}")
guess_count = 0
while guess_count < 3:
    guess_count += 1
    try:
        user_guess = int(input("请输入你猜的数字（1-100）："))
        if user_guess == random_num:
            print("恭喜你，猜对了！")
            guess_count = 0
            break
        else:
            print(f"猜错了，你还有 {3 - guess_count} 次机会。")
    except ValueError:
        print("请输入一个有效的数字！")

if guess_count == 3:
    print(f"很遗憾，你没有猜对。正确答案是 {random_num}。")
    guess_count = 0
