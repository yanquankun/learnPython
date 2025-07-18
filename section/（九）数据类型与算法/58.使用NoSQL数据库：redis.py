"""
@Desc: 本讲解为Python中使用Redis的示例，主要介绍了如何使用Redis进行数据存储和缓存。
@Author: Mint.Yan
@Date: 2025-07-199 13:35:25
"""

# 本例使用MacOs系统演示！！！

# 什么是Redis？
# Redis是一个开源的内存数据结构存储系统，可以用作数据库、缓存和消息代理。它支持多种数据结构，如字符串、哈希、列表、集合等，并提供高性能的数据访问。

# Redis 特点：
# Redis 是一款高性能的键值数据库
# Redis 既有高性能的数据处理能力，又有丰富的编程接口

# Redis数据类型：
# 字符串、双向链表、压缩列表、哈希表、跳表、整数数组


# Redis 官网
# https://redis.io/
# Redis 中文文档
# https://www.redisio.com/Getting-started.html

# 【MacOS安装Redis】
# 1. 使用Homebrew安装Redis（这里我使用homebrew管理包）
# brew install redis

# 2. 启动Redis服务
# 作为后台服务启动
# brew services start redis
# 临时启动（这个方式不会随系统启动，一旦终端关闭或重启，Redis 就停止了）
# redis-server /opt/homebrew/etc/redis.conf

# 3. 查看Redis配置
# brew info list
# 可以看到输出内容：
# To restart redis after an upgrade:
#   brew services restart redis
# Or, if you don't want/need a background service you can just run:
#   /opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf
# 那么我们redis的配置文件在：/opt/homebrew/etc/redis.conf
# 可以看到我们的redis的port是6379

# 4. 设置redis密码（也可以不设置）
# 修改redis.conf如下配置
# requirepass your_secure_password
# 此时，需要在连接Redis时提供密码
# redis-cli -a your_secure_password
# 或者先进入 CLI，再用 AUTH 命令登录：
# redis-cli
# 127.0.0.1:6379> AUTH your_secure_password


# 【命令行工具连接Redis】
# 1. 进入redis-cli
# 通过终端输入以下命令进入Redis命令行界面
# redis-cli
# 或者直接使用完整路径
# /opt/homebrew/opt/redis/bin/redis-cli
# 2. 设置数据
# set key value
# 3. 获取数据
# get key

# 【py链接redis】
# 安装redis-py库
# pip install redis
from redis import Redis

# 连接Redis
conn = Redis('127.0.0.1', 6379)  # 如果设置了密码，需要提供密码
# 设置数据
conn.set('user', 'mint')
name = conn.get('user')
print(name)  # b'mint'
# 设置数据过期时间
conn.setex('user', 10, 'mint')  # 设置10秒后过期，10s后再获取数据将返回None
# 获取所有键
for key in conn.scan_iter(match='*', count=100):
    print(f"Found key: {key}")
# 删除数据
conn.delete('user')

# 【停止redis服务】
# brew services stop redis
# 或手动停止：
# pkill redis-server
