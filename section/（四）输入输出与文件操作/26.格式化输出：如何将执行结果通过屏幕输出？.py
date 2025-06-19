"""
@Desc: 本讲解如何将执行结果通过屏幕输出
@Author: Mint.Yan
@Date: 2025-06-170 13:30:54
"""

# 1. 百分号 %
print("%s is %s than %s" % ("Beautiful", "better", "ugly"))
# 弊端
# - 需要手动指定参数位置，且只能使用字符串类型
# - 不支持关键字参数，且只能使用位置参数
# - 不支持格式化输出，且只能使用位置参数
# - 不支持 f-string 的表达式

# % 用于格式化输出，常用于字符串的格式化
# - %s：字符串
print("%s is %s than %s" % ("Beautiful", "better", "ugly"))
# - %d：整数
print("%d + %d = %d" % (1, 2, 3))
# - %f：浮点数
print("%f + %f = %f" % (1.0, 2.0, 3.0))
# - %x：十六进制整数
print("%x + %x = %x" % (10, 20, 30))
# - %o：八进制整数
print("%o + %o = %o" % (10, 20, 30))
# - %e：科学计数法
print("%e + %e = %e" % (1.0, 2.0, 3.0))
# - %c：单个字符
print("%c" % 'A')  # 输出 A
# - %r：字符串的原始表示
print("%r is %r than %r" % ("Beautiful", "better", "ugly"))
# - %%：百分号本身
print("%% is a percent sign")  # 输出 % is a percent sign

print("===" * 10)

# 2. format() 函数
print("{B} is {b} than {u}".format(u="ugly", B="Beautiful", b="better"))
print("{1} is {2} than {0}".format("ugly", "Beautiful", "better"))
# 弊端
# - 需要手动指定参数位置，且只能使用字符串类型
# - 不支持 f-string 的表达式
# - 不支持关键字参数，且只能使用位置参数

# format() 用于格式化输出，常用于字符串的格式化\
# - {0}：位置参数
# - {1}：位置参数
# - {name}：关键字参数

print("===" * 10)

# 3. f-strings （推荐）
print(f"{'Beautiful'} is {'better'} than {'ugly'}")

# 弊端
# - 需要 Python3.6 以上版本支持
