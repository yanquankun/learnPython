"""
@Desc: 本讲解为Python中使用并行和并发设计的示例，主要介绍了如何使用多线程和多进程来提高程序的执行效率。
@Author: Mint.Yan
@Date: 2025-07-202 13:49:43
"""

# 并发和并行的区别
# 并发是指多个任务在同一时间段内交替执行，而并行是指多个任务在同一时间点同时执行。

# ✓ 并发：宏观上，多个任务同时执行
# ✓ 并行：同一时刻发生

# ✓ 并发：一个 CPU 核心交替运行多个程序
# ✓ 并行：多个 CPU 核心同时处理多个程序

# 在python中，可以通过concurrent.futures模块来实现并发和并行设计。
# 官方文档：https://docs.python.org/zh-cn/3/library/concurrent.futures.html

# concurrent.futures 库中的 Executor 对象时并行任务的抽象类
# 它可以由线程和进程两种方式实现并行计算
# Executor 可以通过 submit() 方式执行

# 线程池
# Executor 对象还支持 ThreadPoolExecutor 方式，使用线程池实现并发
# 它还支持 ProcessPoolExecuter 方式，以使用多核 CPU

# 并发举个??
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import concurrent.futures
import urllib.request

# 例子：��用 ThreadPoolExecutor 来并发加载多个 URL
URLS = [
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com'
]


# 定义一个函数来加载 URL
# @param timeout: 超时时间
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


# 使用 ThreadPoolExecutor 来并发加载多个 URL
# @param max_workers: 最大线程数
# @return: 返回一个 Future 对象，表示异步执行的结果
# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     # 提交任务到线程池
#     future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
#
#     # 等待所有任务完成，并获取结果
#     for future in concurrent.futures.as_completed(future_to_url):
#         url = future_to_url[future]
#         try:
#             data = future.result()
#         except Exception as exc:
#             print('%r generated an exception: %s' % (url, exc))
#         else:
#             print('%r page is %d bytes' % (url, len(data)))


# 并行举个??

# 例子：使用 ProcessPoolExecutor 来并行计算
def square(n):
    """计算平方"""
    return n * n

# 为什么if __name__ == '__main__'？
# 因为在 Mac、Windows 系统中，使用多进程时需要保护代码入口
# 否则会导致无限递归调用，进而导致程序崩溃
if __name__ == '__main__':
    # 使用 ProcessPoolExecutor 来并行计算平方
    with ProcessPoolExecutor(max_workers=2) as executor:
        # 提交任务到进程池
        futures = [executor.submit(square, i) for i in range(10)]

        # 等待所有任务完成，并获取结果
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print('Square result: %d' % result)
