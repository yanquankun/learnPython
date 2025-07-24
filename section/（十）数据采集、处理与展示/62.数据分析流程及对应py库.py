"""
@Desc: 本章节主要讲解数据分析流程及对应py库
@Author: Mint.Yan
@Date: 2025-07-205 14:34:35
"""
"""
@Desc: 本章节主要讲解数据分析流程及对应py库
@Author: Mint.Yan
@Date: 2024-07-25 14:34:35
"""

# --- 数据分析通用流程 ---
# 一个完整的数据分析项目通常遵循以下流程。我们将逐步讲解每个环节，并介绍在Python中实现这些环节的核心库。
# 流程:
# 1. 数据采集 (Data Acquisition)
# 2. 数据清洗与预处理 (Data Cleaning & Preprocessing)
# 3. 数据探索与分析 (Exploratory Data Analysis - EDA)
# 4. 数据可视化 (Data Visualization)
# 5. (可选) 建模与评估 (Modeling & Evaluation)

import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. 数据采集 ---
# 数据采集是数据分析的第一步，目标是获取原始数据。数据来源可以是文件（CSV, Excel）、数据库、API接口或网页。

# 核心库:
# - pandas: 用于读取各种格式的本地文件，如 CSV, Excel, JSON 等。
# - requests: 用于从网络API或网页获取数据。

# 官方文档:
# - pandas: https://pandas.pydata.org/docs/
# - requests: https://requests.readthedocs.io/en/latest/

print("=" * 20, "1. 数据采集", "=" * 20)

# 示例1: 使用 pandas 读取 CSV 文件内容
# 假设我们有一个CSV文件，为了方便演示，我们直接用字符串来模拟文件内容。
csv_data = """OrderID,Product,Quantity,Price
1,Apple,10,2.5
2,Orange,5,3.0
3,Banana,15,1.5
"""
# 使用 io.StringIO 将字符串模拟成文件，pandas可以直接读取
df_from_csv = pd.read_csv(io.StringIO(csv_data))
print("--- 从CSV读取的数据 ---")
print(df_from_csv)
print("\n")

# 示例2: 使用 requests 从 API 获取数据
# 这是一个公开的测试API，返回一些用户信息
api_url = "https://jsonplaceholder.typicode.com/users"
try:
    response = requests.get(api_url)
    response.raise_for_status()  # 如果请求失败 (状态码不是2xx), 会抛出异常
    users_data = response.json()  # 将返回的JSON字符串解析为Python字典列表

    # 将获取的数据转换为 pandas DataFrame，方便后续分析
    df_from_api = pd.DataFrame(users_data)
    print("--- 从API获取的数据 (前5条) ---")
    print(df_from_api.head())
    print("\n")

except requests.exceptions.RequestException as e:
    print(f"请求API时出错: {e}")

# --- 2. 数据清洗与预处理 ---
# 原始数据通常是“脏”的，包含缺失值、重复数据、错误格式等。数据清洗是确保数据质量的关键步骤。

# 核心库:
# - pandas: 提供了强大的功能来处理数据。

# 官方文档:
# - pandas: https://pandas.pydata.org/docs/

print("=" * 20, "2. 数据清洗与预处理", "=" * 20)

# 构造一个包含问题的 "脏" 数据
dirty_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', None],
    'age': [25, 30, None, 35, 25, 22],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York', 'Boston']
}
df_dirty = pd.DataFrame(dirty_data)
print("--- 清洗前的数据 ---")
print(df_dirty)
print("\n")

# 2.1 处理缺失值
# 检查每列的缺失值数量
print("--- 各列缺失值数量 ---")
print(df_dirty.isnull().sum())
print("\n")

# 策略1: 删除包含缺失值的行
df_dropped = df_dirty.dropna()
print("--- 删除缺失值后的数据 ---")
print(df_dropped)
print("\n")

# 策略2: 填充缺失值 (例如，用年龄的平均值填充)
df_filled = df_dirty.copy()  # 创建副本以避免修改原始DataFrame
# mean 函数计算age列的平均值，并用它填充缺失值
# 最终获取的值是一个浮点数，因为平均值可能不是整数
mean_age = df_filled['age'].mean()  # 计算年龄的平均值
print(f"年龄的平均值: {mean_age}")
df_filled['age'] = df_filled['age'].fillna(mean_age)
print("--- 填充缺失值后的数据 ---")
print(df_filled)
print("\n")

# 2.2 处理重复数据
# 检查并删除完全重复的行
df_no_duplicates = df_filled.drop_duplicates()
print("--- 删除重复行后的数据 ---")
print(df_no_duplicates)
print("\n")

# 2.3 数据类型转换
# 假设age列应该是整数类型
df_cleaned = df_no_duplicates.copy()
df_cleaned['age'] = df_cleaned['age'].astype(int)
print("--- 数据类型转换后的数据信息 ---")
print(df_cleaned.info())
print("--- 数据类型转换后的数据 ---")
print(df_cleaned)
print("\n")

# --- 3. 数据探索与分析 (EDA) ---
# 在数据清洗后，我们需要通过统计和分析来理解数据，发现其中的模式、关联和异常。

# 核心库:
# - pandas: 用于计算描述性统计、分组聚合等。
# - NumPy: 为 pandas 提供了底层的数值计算支持，有时也会直接使用。

# 官方文档:
# - NumPy: https://numpy.org/doc/

print("=" * 20, "3. 数据探索与分析", "=" * 20)

# 使用第一步中从CSV读取的数据 df_from_csv
df = df_from_csv

# 3.1 描述性统计
# 对数值列进行快速的统计摘要（计数、均值、标准差、最小值、最大值等）
print("--- 销售数据的描述性统计 ---")
print(df.describe())
print("\n")

# 3.2 分组聚合
# 按产品分组，计算每种产品的总销售量和平均价格
# agg函数允许我们对每个分组应用多个聚合函数
# sum函数计算总销售量，mean函数计算平均价格
# 支持的函数包括: sum, mean, count, min, max 等，官方文档地址：
# https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#aggregation
product_summary = df.groupby('Product').agg(
    # 对每个产品进行聚合
    TotalSales=('Quantity', 'sum'),  # 总销售量
    TotalQuantity=('Quantity', 'sum'),  # 总数量
    AveragePrice=('Price', 'mean')  # 平均价格
)
print("--- 按产品分组的统计 ---")
print(product_summary)
print("\n")

# 3.3 排序
# 按总销售量对产品进行排序
print("--- 按总销售量排序 ---")
print(product_summary.sort_values(by='TotalQuantity', ascending=False))
print("\n")

# --- 4. 数据可视化 ---
# “一图胜千言”。可视化能将复杂的数据和分析结果直观地呈现出来，帮助我们更好地理解和沟通。

# 核心库:
# - Matplotlib: Python中最基础、最强大的绘图库，是很多其他库的基础。
# - Seaborn: 基于Matplotlib，提供了更美观、更高级的统计图形。

# 官方文档:
# - Matplotlib: https://matplotlib.org/stable/contents.html
# - Seaborn: https://seaborn.pydata.org/

print("=" * 20, "4. 数据可视化", "=" * 20)
print("--- 图表将以弹窗形式展示 ---")

# 注意: 如果图表中的中文显示为方框，需要配置中文字体。例如:
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows/Linux: 黑体
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] # MacOS
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 示例1: 使用 Matplotlib 绘制产品销量的折线图
# figsize 参数设置图形的大小 10x5 英寸
plt.figure(figsize=(10, 5))  # 创建一个图形
# plot 函数绘制折线图，x轴为产品名称，y轴为数量
plt.plot(df['Product'], df['Quantity'], marker='o', linestyle='-')
plt.title('Product Quantity')
plt.xlabel('Product')
plt.ylabel('Quantity')
plt.grid(True)
plt.show()

# 示例2: 使用 Seaborn 绘制产品价格的条形图
plt.figure(figsize=(10, 5))  # 创建一个新的图形
sns.barplot(x='Product', y='Price', data=df, palette='viridis', hue='Product', legend=False)
plt.title('Product Price')
plt.xlabel('Product')
plt.ylabel('Price')
plt.show()

# --- 5. (可选) 建模与评估 ---
# 在某些分析项目中，最后一步是利用数据构建预测模型或分类模型。

# 核心库:
# - Scikit-learn: Python 机器学习的事实标准库，提供了丰富的算法和工具。

# 官方文档:
# - Scikit-learn: https://scikit-learn.org/stable/

print("=" * 20, "5. 建模与评估", "=" * 20)
print("这是一个更高级的主题，通常涉及特征工程、模型训练、评估和调优。")
print("例如，我们可以根据产品的数量和价格，来预测它是否为“热门商品”。")
print("Scikit-learn 提供了线性回归、逻辑回归、决策树、支持向量机等大量模型。")
print("\n--- 数据分析流程讲解完毕 ---")

# ============================================================================
# 常用数据分析库总结
# ============================================================================

"""
核心库总结：

1. 数据操作：
   - pandas: 数据操作和分析 (https://pandas.pydata.org/)
   - numpy: 数值计算 (https://numpy.org/)

2. 可视化：
   - matplotlib: 基础绘图 (https://matplotlib.org/)
   - seaborn: 统计可视化 (https://seaborn.pydata.org/)
   - plotly: 交互式图表 (https://plotly.com/python/)

3. 机器学习：
   - scikit-learn: 机器学习 (https://scikit-learn.org/)
   - xgboost: 梯度提升 (https://xgboost.readthedocs.io/)
   - lightgbm: 轻量级梯度提升 (https://lightgbm.readthedocs.io/)

4. 深度学习：
   - tensorflow: 深度学习框架 (https://www.tensorflow.org/)
   - pytorch: 深度学习框架 (https://pytorch.org/)
   - keras: 高级神经网络API (https://keras.io/)

5. 统计分析：
   - scipy: 科学计算 (https://scipy.org/)
   - statsmodels: 统计建模 (https://www.statsmodels.org/)

6. 数据收集：
   - requests: HTTP请求 (https://requests.readthedocs.io/)
   - beautifulsoup4: 网页解析 (https://www.crummy.com/software/BeautifulSoup/)
   - scrapy: 网页爬虫框架 (https://scrapy.org/)

7. 数据库操作：
   - sqlalchemy: SQL工具包 (https://www.sqlalchemy.org/)
   - pymongo: MongoDB驱动 (https://pymongo.readthedocs.io/)

安装命令：
pip install pandas numpy matplotlib seaborn plotly scikit-learn xgboost lightgbm tensorflow torch scipy statsmodels requests beautifulsoup4 scrapy sqlalchemy pymongo
"""
