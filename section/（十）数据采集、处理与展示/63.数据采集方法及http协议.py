"""
@Desc: 本章节主要讲解数据采集方法及HTTP协议
@Author: Mint.Yan
@Date: 2025-07-205 15:34:47
"""

# --- 基于 HTTP 协议实现数据采集的原理 ---
"""
HTTP 协议是 Web 上最常用的协议，数据采集通常通过 HTTP 请求获取网页内容。HTTP 协议定义了客户端和服务器之间的通信方式，包括请求方法、状态码、头部信息等。
常用的 HTTP 请求方法包括 GET、POST、PUT、DELETE 等。GET 方法用于获取资源，POST 方法用于提交数据，PUT 方法用于更新资源，DELETE 方法用于删除资源。
HTTP 请求通常包含以下部分：
1. 请求行：包括请求方法、请求 URL 和 HTTP 版本。
2. 请求头：包含请求的元信息，如 User-Agent、Accept、Content-Type 等
3. 请求体：在 POST 和 PUT 请求中包含要发送的数据。
HTTP 响应通常包含以下部分：
1. 状态行：包括 HTTP 版本、状态码和状态消息。
2. 响应头：包含响应的元信息，如 Content-Type、Content-Length 等。
3. 响应体：包含实际的响应数据，如 HTML、JSON 等。
"""

# --- 基于 HTTP 协议实现数据采集的代码示例 ---
import requests
import json
# requests 库是 Python 中最常用的 HTTP 客户端库，可以方便地发送 HTTP 请求和处理响应。
# json 库用于处理 JSON 数据格式，常用于 API 响应数据的解析。
