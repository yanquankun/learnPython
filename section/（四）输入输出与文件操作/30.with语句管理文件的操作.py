"""
@Desc: 本讲解如何使用 with 语句管理文件的操作
@Author: Mint.Yan
@Date: 2025-06-174 13:45:56
"""
# with语句可以自动管理文件的打开和关闭，离开with语句的作用域时，文件会自动关闭
# 格式如下：
# with open(file, mode='r', encoding='utf-8') as f:
#     # 在这里进行文件操作

# 使用with语句打开文件
with open("../../files/demo.txt", mode='r', encoding='utf-8') as f:
    content = f.read()

print(content)
