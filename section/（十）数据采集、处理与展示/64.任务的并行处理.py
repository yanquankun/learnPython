"""
@Desc: 本章节主要讲解数据采集中的并行处理
@Author: Mint.Yan
@Date: 2025-07-206 13:56:50
"""

#  并行下载模型应当控制并行程序的个数
# • 避免造成服务器或客户机因资源消耗过大，出现服务不可用的情况
# ✅ 推荐进程池模型
# ❎ 不推荐基于采集的图片数量，设置并发数量

#  多线程并行下载，同样推荐线程池模型
# • 将代码改为多线程下载后，分别比较单进程、多进程和多线程下载程序的运行时间
# ★ 结论：多进程和多线程比单进程下载速度快；但多进程和多线程之间没有明显差别

# 举个🌰
# 使用多线程下载图片，将图片写入本地文件系统（files/imgs）中，并且以文件名的形式保存图片的URL

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import os


def download_image(url):
    filename = url.split("/")[-1]
    try:
        response = requests.get(url)
        response.raise_for_status()  # 确保请求成功
        with open(filename, 'wb') as f:
            f.write(response.content)
        return f"{filename}-文件下载完成-{url}"
    except None:
        return f"{filename}-文件下载失败-{url}"


# 获取当前文件的绝对路径
current_file = os.path.abspath(__file__)

# 获取当前文件所在目录
current_dir = os.path.dirname(current_file)

# 获取项目根目录（向上2级）
project_root = os.path.dirname(os.path.dirname(current_dir))

# 图片缓存目录
img_dir = os.path.join(project_root, 'files', 'imgs')

# 确保图片URL列表
# 提供一些在线的图片地址（图片为网上图片获取~~~有惊喜😄）
image_urls = [
    "http://e.hiphotos.baidu.com/image/pic/item/a1ec08fa513d2697e542494057fbb2fb4316d81e.jpg",
    "http://c.hiphotos.baidu.com/image/pic/item/30adcbef76094b36de8a2fe5a1cc7cd98d109d99.jpg",
    "http://h.hiphotos.baidu.com/image/pic/item/7c1ed21b0ef41bd5f2c2a9e953da81cb39db3d1d.jpg",
    "http://g.hiphotos.baidu.com/image/pic/item/55e736d12f2eb938d5277fd5d0628535e5dd6f4a.jpg",
    "http://e.hiphotos.baidu.com/image/pic/item/4e4a20a4462309f7e41f5cfe760e0cf3d6cad6ee.jpg",
    "http://b.hiphotos.baidu.com/image/pic/item/9d82d158ccbf6c81b94575cfb93eb13533fa40a2.jpg",
    "http://e.hiphotos.baidu.com/image/pic/item/4bed2e738bd4b31c1badd5a685d6277f9e2ff81e.jpg",
    "http://g.hiphotos.baidu.com/image/pic/item/0d338744ebf81a4c87a3add4d52a6059252da61e.jpg",
]

try:
    # 确保目录存在，如果不存在则创建
    os.makedirs(img_dir, exist_ok=True)

    # 切换目录到imgs中
    os.chdir(img_dir)

    # 使用线程池下载图片
    print("*" * 10, "开始下载图片", "*" * 10)
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(download_image, url): url for url in image_urls}
        for future in as_completed(futures):
            result = future.result()
            print(result)

        print("*" * 10, "下载完成", "*" * 10)
        # 任务完成，则关闭线程池（避免内存占用）
        executor.shutdown(wait=True)
except OSError as e:
    print(f"{img_dir}: {e}")
