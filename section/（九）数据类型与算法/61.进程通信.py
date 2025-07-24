"""
@Desc: 本章节主要讲解进程之间如何进行通信
@Author: Mint.Yan
@Date: 2025-07-203 13:36:56
"""
import time
# ======================================================================================================================
# 进程间通信（IPC）是指在不同进程之间传递数据或信息的机制。
# 在 CPython 中，由于存在 GIL（全局解释器锁），同一时刻只有一个线程能执行，因此多线程在 CPU 密集型任务上无法发挥多核优势。
# - I/O 密集型应用（如网络请求、文件读写）可使用多线程模型，因为线程在等待 I/O 时会释放 GIL。
# - 计算密集型应用（如科学计算、数据分析）应当使用多进程模型，以利用多核 CPU。
#
# 在 Python 中，`multiprocessing` 模块提供了多种方式实现进程间通信，主要包括：
# 1. 队列 (Queue): 线程安全、进程安全的数据结构，用于在多个进程之间传递消息。
# 2. 管道 (Pipe): 用于在两个进程之间建立一条双向通信通道。
# 3. 共享内存 (Shared Memory):允许多个进程直接访问同一块内存区域，适用于需要高速共享数据的场景。
#    - `Value`: 用于共享单个值。
#    - `Array`: 用于共享一个定长数组。
# 4. 管理器 (Manager): 通过一个服务进程来管理共享的 Python 对象（如 list, dict），支持更复杂的数据共享。
# ======================================================================================================================

from multiprocessing import Process, Queue, Pipe, Value, Array, Manager


# ======================================================================================================================
# 示例 1: 使用队列 (Queue) 进行通信
# 队列是实现多进程通信最常用、最安全的方式之一。它是一个先进先出（FIFO）的数据结构。
# ======================================================================================================================
def producer(q):
    """生产者进程，向队列中放入数据"""
    print("生产者: 开始生产数据...")
    for i in range(5):
        item = f"产品 {i}"
        q.put(item)
        print(f"生产者: 生产了 '{item}'")
        time.sleep(1)
    q.put(None)  # 发送结束信号


def consumer(q):
    """消费者进程，从队列中取出数据"""
    print("消费者: 等待接收数据...")
    while True:
        item = q.get()
        if item is None:  # 收到结束信号
            print("消费者: 接收到结束信号，退出。")
            break
        print(f"消费者: 消费了 '{item}'")
        time.sleep(1.5)


def run_queue_example():
    print("\n--- 队列 (Queue) 通信示例 ---")
    q = Queue()  # 创建一个进程安全的队列

    # 创建生产者和消费者进程
    # Process 是 multiprocessing 模块中的一个类，用于创建新进程
    # args 参数用于传递给目标函数的参数
    p_producer = Process(target=producer, args=(q,))
    p_consumer = Process(target=consumer, args=(q,))

    # 启动进程
    p_producer.start()
    p_consumer.start()

    # 等待进程结束
    # join 方法会阻塞主进程，直到子进程结束
    # 为什么不用close？
    # 由于 Queue 是进程安全的，close 方法不适用
    # 因此在使用 Queue 时，通常不需要调用 close 方法
    # 关闭队列的正确方式是让生产者发送一个结束信号（如 None），然后消费者在接收到该信号后退出。
    p_producer.join()
    p_consumer.join()
    print("--- 队列示例结束 ---\n")


# ======================================================================================================================
# 示例 2: 使用管道 (Pipe) 进行通信
# 管道通常用于两个进程之间的双向通信。Pipe() 返回一个包含两个连接对象的元组，分别代表管道的两端。
# ======================================================================================================================
def sender(conn):
    """发送方进程，通过管道发送消息"""
    print("发送方: 开始发送消息...")
    conn.send("你好，我是发送方！")
    conn.send([1, 2, 3, 4, 5])
    print("发送方: 收到回复 -", conn.recv())
    conn.close()


def receiver(conn):
    """接收方进程，通过管道接收消息"""
    print("接收方: 等待接收消息...")
    msg1 = conn.recv()
    print(f"接收方: 收到消息 - '{msg1}'")
    msg2 = conn.recv()
    print(f"接收方: 收到消息 - {msg2}")
    conn.send("你好，消息已收到！")
    conn.close()


def run_pipe_example():
    print("\n--- 管道 (Pipe) 通信示例 ---")
    # 创建一个管道，它返回两个连接对象
    parent_conn, child_conn = Pipe()

    # 创建发送和接收进程
    p_sender = Process(target=sender, args=(child_conn,))
    p_receiver = Process(target=receiver, args=(parent_conn,))

    # 启动进程
    p_sender.start()
    p_receiver.start()

    # 等待进程结束
    p_sender.join()
    p_receiver.join()
    print("--- 管道示例结束 ---\n")


# ======================================================================================================================
# 示例 3: 使用共享内存 (Value 和 Array)
# 共享内存是最快的 IPC 方式，因为它避免了数据的序列化和反序列化。
# `Value` 用于共享单个变量，`Array` 用于共享一个数组。
# 使用时需要指定类型代码，如 'i' for integer, 'd' for double, 'c' for char.
# ======================================================================================================================
def worker_value(num):
    """修改共享数值的进程"""
    print(f"工作进程: 共享数值初始值 = {num.value}")
    num.value += 10.5
    print(f"工作进程: 共享数值修改后 = {num.value}")


def worker_array(arr):
    """修改共享数组的进程"""
    print(f"工作进程: 共享数组初始值 = {list(arr)}")
    for i in range(len(arr)):
        arr[i] = i * i
    print(f"工作进程: 共享数组修改后 = {list(arr)}")


def run_shared_memory_example():
    print("\n--- 共享内存 (Value/Array) 示例 ---")
    # 创建一个共享的 double 类型的数值，初始值为 1.0
    shared_num = Value('d', 1.0)
    # 创建一个共享的 integer 类型的数组，长度为 5
    shared_arr = Array('i', [0, 0, 0, 0, 0])

    # 创建并启动进程
    p1 = Process(target=worker_value, args=(shared_num,))
    p2 = Process(target=worker_array, args=(shared_arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    # 在主进程中查看修改后的结果
    print(f"主进程: 最终共享数值 = {shared_num.value}")
    print(f"主进程: 最终共享数组 = {list(shared_arr)}")
    print("--- 共享内存示例结束 ---\n")


# ======================================================================================================================
# 示例 4: 使用管理器 (Manager)
# Manager 支持更复杂的 Python 对象共享，如 list, dict, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value 和 Array。
# 它通过一个服务进程来管理这些对象，其他进程通过代理访问它们。
# ======================================================================================================================
def worker_manager(shared_dict, shared_list):
    """修改由 Manager 管理的共享对象的进程"""
    print(f"工作进程: 共享字典初始值 = {shared_dict}")
    shared_dict['key1'] = 'value1_modified'
    shared_dict['key2'] = 'value2_new'
    print(f"工作进程: 共享字典修改后 = {shared_dict}")

    print(f"工作进程: 共享列表初始值 = {shared_list}")
    shared_list.append(4)
    shared_list[0] = 99
    print(f"工作进程: 共享列表修改后 = {shared_list}")


def run_manager_example():
    print("\n--- 管理器 (Manager) 示例 ---")
    with Manager() as manager:
        # 创建由 Manager 管理的共享字典和列表
        shared_dict = manager.dict({'key1': 'value1'})
        shared_list = manager.list([1, 2, 3])

        p = Process(target=worker_manager, args=(shared_dict, shared_list))
        p.start()
        p.join()

        # 在主进程中查看结果
        print(f"主进程: 最终共享字典 = {shared_dict}")
        print(f"主进程: 最终共享列表 = {shared_list}")
    print("--- 管理器示例结束 ---\n")


# ======================================================================================================================
# 主函数，依次运行所有示例
if __name__ == "__main__":
    # 依次运行所有示例
    run_queue_example()
    time.sleep(2)  # 等待一下，方便观察输出
    run_pipe_example()
    time.sleep(2)
    run_shared_memory_example()
    time.sleep(2)
    run_manager_example()
