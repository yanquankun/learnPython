"""
@Desc: 本章节主要讲解Python中二维图表的绘制方法，使用Matplotlib库进行数据可视化
@Author: Mint.Yan
@Date: 2025-07-210 14:05:48
"""

# 图形化展示的意义
# 图形化展示可以帮助我们更直观地理解数据，发现数据中的模式和趋势。
# 在数据分析和机器学习中，图形化展示是非常重要的一环，可以帮助我们更好地理解数据。
# Matplotlib是Python中最常用的绘图库之一，提供了丰富的绘图功能和灵活的配置选项。
# numpy是Python中用于科学计算的库，提供了高效的数组操作和数学函数。

# Matplotlib官网地址：https://matplotlib.org/stable/index.html
# 中文地址：https://matplotlib.org.cn/stable/

# numpy官网地址：https://numpy.org/doc/stable/


# • Notebook 不会像 Python 终端一样自动展示图表
# • 如果你用 Notebook 运行 Matplotlib 库，需要在绘图时增加函数 figure.show()

import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体，避免中文乱码
plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题
# 生成一些示例数据
x = np.linspace(0, 10, 100)  # 生成0到10之间的100个点
y = np.sin(x)  # 计算这些点的正弦值
# 绘制折线图
plt.figure(figsize=(10, 5))  # 设置图形大小
plt.plot(x, y, label='sin(x)', color='blue')  # 绘制正弦曲线
plt.title('正弦函数图')  # 设置标题
plt.xlabel('x 值')  # 设置x轴标签
plt.ylabel('sin(x) 值')  # 设置y轴标签
plt.grid(True)  # 显示网格
plt.legend()  # 显示图例
plt.show()  # 显示图形