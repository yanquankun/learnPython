"""
@Desc: 本讲解Python内置数据类型的转换实现通讯录功能
@Author: Mint.Yan
@Date: 2025-06-162 14:56:46
"""

from tinydb import TinyDB, Query

# 通讯录功能 样例文件：files/通讯录.csv

# 读取files目录中通讯录.csv文件
with open('../files/通讯录.csv', 'r', encoding='utf-8') as file:
    file_data = file.readlines()

print("读取到的通讯录数据：", file_data)

# 指定TinyDB数据库文件路径
db = TinyDB('../files/通讯录.json')
# 定义查询对象
Contact = Query()


# 将读取到的通讯录数据转换为字典格式
def convert_to_dict(_line):
    parts = _line.strip().split(',')
    return {
        'name': parts[0],
        'source': parts[1],
        'phone': parts[2]
    }


dict_data = [convert_to_dict(line) for line in file_data if line.strip()]

# 过滤掉已存在的数据
for line in dict_data:
    if line:
        if not db.contains(Contact.name == line['name']):
            db.insert(line)
            print("Data inserted successfully.")
        else:
            print("Duplicate data. Insertion skipped.")

# 输出数据库中的所有数据
print("数据库中的所有数据：", db.all())

# 根据姓名查询数据
one_data = db.search(Contact.name == '张三')
print("查询到的张三的数据：", one_data)
one_data = db.search(Contact.name.matches(r'^李四$'))
print("查询到的李四的数据：", one_data)
