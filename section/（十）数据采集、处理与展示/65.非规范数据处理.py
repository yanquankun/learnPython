"""
@Desc: 本章节主要讲解非规范化数据的处理
@Author: Mint.Yan
@Date: 2025-07-210 13:37:50
"""

# 非规范化数据分类
# 1. 非结构化数据：如文本、图片、音频等
# 2. 半结构化数据：如JSON、XML等
# 3. 结构化数据：如关系型数据库中的表格数据

# 非规范化数据处理方法
# 1. 文本数据处理：使用自然语言处理（NLP）技术进行
#    分词、词性标注、命名实体识别等操作
# 2. 图片数据处理：使用计算机视觉技术进行图像识别、图像分类、目标检测等操作
# 3. 音频数据处理：使用音频处理技术进行音频特征提取、语音识别等操作
# 4. JSON/XML数据处理：使用解析库（如json、xml.etree.ElementTree）进行数据解析和提取

import json
import xml.etree.ElementTree as ET


# 示例：处理JSON数据
def process_json_data(json_str):
    try:
        data = json.loads(json_str)
        print("JSON数据处理成功:", data)
    except json.JSONDecodeError as e:
        print("JSON数据处理失败:", e)


# 示例：处理XML数据
def process_xml_data(xml_str):
    try:
        root = ET.fromstring(xml_str)
        print("XML数据处理成功:", root.tag)
        for child in root:
            print(f"子元素: {child.tag}, 值: {child.text}")
    except ET.ParseError as e:
        print("XML数据处理失败:", e)


# 测试非规范化数据处理
# 测试JSON数据处理
json_data = '{"name": "Mint.Yan", "age": 25, "city": "Beijing"}'
process_json_data(json_data)

# 测试XML数据处理
xml_data = '<root><name>Mint.Yan</name><age>25</age><city>Beijing</city></root>'
process_xml_data(xml_data)

print("===" * 10)

# 通过正则表达式处理非规范化文本数据
import re


def process_text_data(text):
    # 使用正则表达式提取所有的电子邮件地址
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)

    if emails:
        print("提取到的电子邮件地址:", emails)
    else:
        print("未找到电子邮件地址")


# 测试文本数据处理
text_data = "请联系我：17600610907@163.com"
process_text_data(text_data)
