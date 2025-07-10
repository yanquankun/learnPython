"""
@Desc: 本讲解为捕获python中的异常
@Author: Mint.Yan
@Date: 2025-07-191 13:44:16
"""

# 1. try-except 语句
# try：
#   可能产生异常的代码
# except 异常：
#   捕获指定的异常后运行的代码
# else ：
#   try 部分的代码没有抛出异常，执行此部分代码
# finally：
#   无论是否抛出异常，该部分代码均会执行

# 举个🌰
try:
    1 / 0
except ZeroDivisionError as e:
    print(f"捕获到异常：{e}")

# 如果不知道异常类型，可以使用通用异常捕获：
try:
    1 / 0
except Exception as e:
    print(f"捕获到异常：{e}")

# 如果需要在异常发生后继续执行代码，可以使用 else 语句：
try:
    result = 1 / 1
except ZeroDivisionError as e:
    print(f"捕获到异常：{e}")
else:
    print(f"计算结果：{result}")

# finally 语句可以确保无论是否发生异常，都会执行某些代码：
try:
    result = 1 / 0
except ZeroDivisionError as e:
    pass
finally:
    print("无论如何都会执行这段代码")

# 2. 捕获多个异常
# try：
#     可能产生异常的语句
# except 异常 1：
#     处理方式一
# except 异常 2：
#     处理方式二
# except ...

# 举个🌰
num1 = 1
num2 = 0  # '0'
try:
    result = num1 / num2
except ZeroDivisionError as e:
    # 当 num2 为 0 时会抛出 ZeroDivisionError
    print(f"捕获到除法异常：{e}")
except TypeError as e:
    # 当 num2 是字符串时会抛出 TypeError
    print(f"捕获到类型错误：{e}")

# 3. 嵌套捕获（不推荐使用这种模式）
# try:
#     try:
#         语句
#     except:
#         pass
# except:
#     pass

# 举个🌰
try:
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"内层捕获到异常：{e}")
        # raise 重新抛出异常
        # 重新抛出异常后，外层的 except 块也会捕获到这个异常
        raise
except ZeroDivisionError as e:
    print(f"外层捕获到异常：{e}")
