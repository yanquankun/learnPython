"""
@Desc: 本讲解为Python中使用关系型数据库的示例，主要介绍了如何使用SQLite进行数据存储和查询。
@Author: Mint.Yan
@Date: 2025-07-199 13:49:06
"""

# 【关系型数据库的用途】
# 比普通文本更灵活，接口更完善
# 数据安全性比文本更强
# 查询速度更快

# 本节使用MacOS系统演示！！！

# 【MacOS安装Mysql】
# 1. 使用Homebrew安装Mysql（这里我使用homebrew管理包）
# brew install mysql

# 2. 启动Mysql服务
# 作为后台服务启动
# brew services start mysql
# 临时启动（这个方式不会随系统启动，一旦终端关闭或重启，Mysql 就停止了）
# mysql.server start

# 3. 设置mysql密码
# mysql_secure_installation
# 这个命令会引导你设置root用户的密码，并进行一些安全配置。
# 🔒 如果你是第一次设置密码，直接回车可以跳过当前密码输入，然后设置新密码。

# 4. 查看Mysql配置
# brew info mysql
# brew的mysql实际配置目录在：
# /opt/homebrew/etc/my.cnf

# 4. 登录Mysql
# 通过终端输入以下命令登录Mysql
# mysql -u root -p


# 【py连接数据库】pymysql
# 安装pymysql库
# pip install pymysql

import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', password='yqk229218087', db='py_test')

with db.cursor() as cursor:
    # 查看当前数据库表
    cursor.execute("SHOW TABLES")
    # 获取所有表名
    tables = cursor.fetchall()
    for table in tables:
        print(f"数据库表名：{table}")

# 【关闭mysql】
# 通过终端输入以下命令关闭Mysql
# mysql.server stop
# 或者
# brew services stop mysql
