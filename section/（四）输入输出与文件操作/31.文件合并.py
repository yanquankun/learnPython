"""
@Desc: 本讲解如何合并多个文件的内容到一个新文件中
@Author: Mint.Yan
@Date: 2025-06-174 13:52:10
"""
import os

old_dir = os.getcwd()  # 获取当前工作目录
os.chdir('../../files')  # 切换到files目录

# 案例1：合并files下demo1和demo2到demo4中
with open('demo1.txt', 'r') as file1, \
        open('demo2.txt', 'r') as file2, \
        open('demo4.txt', 'w+') as file4:
    # 读取demo1的内容并写入demo4
    content1 = file1.read()
    file4.write(content1)

    # 在demo4中添加一个换行符
    file4.write('\n')

    # 读取demo2的内容并写入demo4
    content2 = file2.read()
    file4.write(content2)

    # 输出合并完成的提示
    file4.seek(0)  # 将文件指针移动到文件开头
    print("文件合并完成，内容已写入demo4.txt", file4.read())

# 案例2：合并files下所有txt文件到demo5中
file_list = ['demo1.txt', 'demo2.txt', 'demo3.txt']
size = len(file_list)
for index, file_name in enumerate(file_list):
    with open(file_name, 'r') as file:
        content = file.read().strip()  # 读取文件内容并去除首尾空白字符
        with open('demo5.txt', 'a+') as file5:
            if index == 0:
                # 先清空
                file5.truncate(0)
            file5.write(content + '\n')
            print(f"{file_name} 的内容已合并到 demo5.txt 中")
            if index + 1 == size:
                file5.seek(0)
                print(f"demo5.txt 合并完成，内容为：\n{file5.read()}")

os.chdir(old_dir)  # 切换回原工作目录
