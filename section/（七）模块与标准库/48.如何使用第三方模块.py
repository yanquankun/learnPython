"""
@Desc: 本讲解Python中如何使用第三方模块
@Author: Mint.Yan
@Date: 2025-07-189 16:42:56
"""

# 第三方模块的安装

# 格式：
# pip[3.10] install [第三方模块名称]
# python[3.10] -m pip install [第三方模块名称]

# 查找三方模块地址：
# https://pypi.org/project
# 举个🌰：
# 查找requests模块的地址
# https://pypi.org/project/requests/

# 虚拟环境的使用

# 虚拟环境的用途：
# •解决多个模块依赖的问题
# •一次性安装多个指定版本的模块
# •避免对默认环境造成污染

# 创建虚拟环境的命令：
# python -m venv <虚拟环境名称>
# 举个🌰：
# python -m venv myvenv # myvenv 保存虚拟环境的文件夹

# 将当前安装的包及其版本保存到文件中：
# pip3.10 freeze > requirements.txt

# 激活虚拟环境：
# source myvenv/bin/activate

# 在虚拟环境中导入指定的包：
# pip3.10 install -r requirements.txt

# 离开虚拟环境：
# deactivate

# 删除虚拟环境：
# rm -rf myvenv

# 注意事项：
# 1. 虚拟环境的创建和使用需要在命令行中进行
# 2. 在虚拟环境中安装的模块不会影响全局环境
# 3. 在虚拟环境中安装的模块可以在虚拟环境中使用和卸载

# 镜像源加速

# 由于国外的镜像源速度较慢，使用国内镜像源可以加速模块的下载和安装。
# 国内镜像源地址：
# https://pypi.tuna.tsinghua.edu.cn/simple
# https://mirrors.aliyun.com/pypi/simple/

# 临时加速
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name

# 永久加速
# cat ~/pip.conf
# [global]
# index-url = http://mirrors.aliyun.com/pypi/simple/
# [install]
# trusted-host=mirrors.aliyun.com
