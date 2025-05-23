# 数字类型：整数 浮点数 复数

# 浮点数类型：float
floatNum = 3.14
print(floatNum)
intToFloatNum = float(3)
print(intToFloatNum)

# 整数类型：int
intNum = 3
print(intNum)
parseFloatNum = int(floatNum)
print(parseFloatNum)

# 复数类型：complex
# 复数是实数和虚数的组合，实数部分和虚数部分都可以是浮点数或整数
# 复数的表示方法：a + bj 或者 a + bJ
# 其中 a 是实数部分，b 是虚数部分，j 或 J 是虚数单位
# 复数的作用是表示一个点在二维平面上的位置
# 例如： 3 + 4j 表示一个点在平面上的位置，实数部分是 x 坐标，虚数部分是 y 坐标
complexNum = 3 + 4j
print(complexNum)

# type() 获取数据类型
print(type(floatNum) is float)
print(type(intNum) is int)
print(type(complexNum) is not complex)
print(type("123") is str)

# str() 将数字转换为字符串
strNum = str(floatNum)
print(strNum)
print(f"{strNum}的类型是{type(strNum)}")

# int() 将只含有字符串转换为整数，否则报错
strNum = "3.14"
try:
    int(strNum)
except ValueError as e:
    # 输出错误
    print(f"{strNum}不能转换为整数，错误信息是：{e}")

strNum = "3"
print(f"{strNum}转换为整数{int(strNum)}")
