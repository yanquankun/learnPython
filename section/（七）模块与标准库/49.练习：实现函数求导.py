"""
@Desc: 本讲解为Python中实现函数求导
@Author: Mint.Yan
@Date: 2025-07-189 16:43:51
"""

# 需求：使用python计算函数的导数

# 1. 安装sympy库
# pip3.10 install sympy

# 2. 导入库
from sympy import Derivative, Symbol, plotting

# 3. 实现函数求导
x = Symbol('x')  # 定义符号变量x
y = x * x + 3 * x + 2  # 定义函数y = x^2 + 3x + 2

d = Derivative(y, x)  # 求y对x的导数
# doit 方法用于计算导数
print(d.doit().subs({x: 10}))  # 计算导数在x=10处的值

plot = plotting.plot  # 导入绘图函数
plot(y, (x, -20, 20), show=True)  # 绘制函数图像
