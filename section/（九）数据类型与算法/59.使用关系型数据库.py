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

db = pymysql.connect(host='127.0.0.1', user='root', password='yqk229218087')

with db.cursor() as cursor:
    # 创建数据库
    cursor.execute("CREATE DATABASE IF NOT EXISTS py_test")

    # 选择数据库
    cursor.execute("USE py_test")

    # 创建数据库表(如果不存在)
    create_user_table_sql = """
                            CREATE TABLE IF NOT EXISTS `users`
                            (
                                `id`       int(11)                       NOT NULL AUTO_INCREMENT,
                                # 需要将email设置为唯一索引，以便在插入数据时可以使用ON DUPLICATE KEY UPDATE语句更新密码
                                `email`    varchar(255) COLLATE utf8_bin NOT NULL UNIQUE,
                                `password` varchar(255) COLLATE utf8_bin NOT NULL,
                                PRIMARY KEY (`id`)
                            )
                                ENGINE = InnoDB
                                DEFAULT CHARSET = utf8mb4
                                COLLATE = utf8mb4_bin
                                AUTO_INCREMENT = 1;
                            """
    cursor.execute(create_user_table_sql)

    # 查看当前数据库表
    cursor.execute("SHOW TABLES")

    # 获取所有表名
    tables = cursor.fetchall()
    for table in tables:
        print(f"数据库表名：{table}")

    # 插入数据(如果不存在emial为'yqk@gmail'的用户，则插入新纪录；如果存在，则更新密码)
    try:
        insert_user_sql = """
                          INSERT INTO `users` (`email`, `password`)
                          VALUES (%s, %s)
                          ON DUPLICATE KEY UPDATE `password` = VALUES(`password`); \
                          """
        cursor.execute(insert_user_sql, ('yqk@gmail', '123456'))

        # connection 不能自动提交数据，必须手动提交
        cursor.connection.commit()
    except Exception as e:
        # 如果发生错误，回滚事务
        cursor.connection.rollback()
        print(f"插入数据失败: {e}")

    # 读取纪录
    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    cursor.execute(sql, ('yqk@gmail',))
    # fetchone 查询一条
    # fetchall 查询所有
    # fetchmany(size) 查看指定数量的记录
    result = cursor.fetchall()
    print(result)

    # 修改数据
    update_sql = "UPDATE `users` SET `password`=%s WHERE `email`=%s"
    cursor.execute(update_sql, ('654321', 'yqk@gmail'))

    # 提交修改
    cursor.connection.commit()

    # 关闭游标
    cursor.close()

# 【关闭mysql】
# 通过终端输入以下命令关闭Mysql
# mysql.server stop
# 或者
# brew services stop mysql
