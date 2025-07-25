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

# 发送 GET 请求获取网页内容
response = requests.get('https://api.github.com')

# 检查请求是否成功
if response.status_code == 200:
    # 打印响应内容
    print("Response Content:", response.text)
else:
    print("Request failed with status code:", response.status_code)

print("===" * 10)

# 发送 POST 请求提交数据
data = {
    'name': 'example',
    'description': 'This is an example.'
}
response = requests.post('https://api.github.com/repos', json=data, headers={
    'content-type': 'application/json',
})
# 检查请求是否成功
if response.status_code == 201:
    # 打印响应内容
    print("Repository created:", response.json())
else:
    print("Failed to create repository with status code:", response.status_code)

print("===" * 10)

# 解析 JSON 响应数据
response = requests.get('https://api.github.com/repos/octocat/Hello-World')
if response.status_code == 200:
    repo_data = response.json()  # 将响应内容解析为 JSON 对象
    print("Repository Name:", repo_data['name'])
    print("Repository Description:", repo_data['description'])
else:
    print("Failed to fetch repository data with status code:", response.status_code)

# --- HTTP 协议的常用状态码 ---
"""
HTTP 协议定义了一些常用的状态码，用于表示请求的处理结果
1. 200 OK：请求成功，服务器返回请求的资源。
2. 201 Created：请求成功，服务器创建了新的资源。
3. 204 No Content：请求成功，但没有返回任何内容。
4. 301 Moved Permanently：请求的资源已被永久移动到新位置。
5. 302 Found：请求的资源临时移动到新位置。
6. 304 Not Modified：请求的资源未修改，客户端可以使用缓存的版本。
7. 400 Bad Request：请求无效，服务器无法理解请求。
8. 401 Unauthorized：请求未授权，需要进行身份验证。
9. 403 Forbidden：服务器拒绝请求，客户端没有权限访问资源。
10. 404 Not Found：请求的资源不存在。
11. 500 Internal Server Error：服务器内部错误，无法处理请求。
12. 502 Bad Gateway：网关错误，服务器作为网关或代理时收到无效响应。
13. 503 Service Unavailable：服务不可用，服务器当前无法处理请求。
"""

# --- HTTP 请求头的常用字段 ---
"""
HTTP 请求头包含了请求的元信息，常用的请求头字段包括：
1. User-Agent：客户端软件的信息，通常包含浏览器类型和版本。
2. Accept：客户端能够处理的内容类型，如 text/html、application/json 等。
3. Content-Type：请求体的内容类型，通常在 POST 请求中使用，如 application/json、application/x-www-form-urlencoded 等。
4. Authorization：用于身份验证的凭据，如 Bearer token 或 Basic auth。
5. Cookie：客户端发送的 Cookie 信息，用于会话管理和状态跟踪。
6. Referer：表示请求的来源 URL，通常用于跟踪用户行为。
7. Host：请求的主机名和端口号，通常在虚拟主务器中使用。
8. Accept-Encoding：客户端支持的内容编码方式，如 gzip、deflate 等。
9. Accept-Language：客户端支持的语言类型，如 en-US、zh-CN 等
10. Connection：表示连接的管理方式，如 keep-alive 或 close。
"""

# --- HTTP 响应头的常用字段 ---
"""
HTTP 响应头包含了响应的元信息，常用的响应头字段包括
1. Content-Type：响应体的内容类型，如 text/html、application/json 等。
2. Content-Length：响应体的长度，以字节为单位。
3. Content-Encoding：响应体的内容编码方式，如 gzip、deflate 等。
4. Cache-Control：缓存控制指令，用于指定响应的缓存策略。
5. Expires：响应的过期时间，表示响应在何时失效。
6. Last-Modified：响应体最后修改的时间，用于缓存验证。
7. ETag：响应体的实体标签，用于缓存验证。
8. Set-Cookie：服务器设置的 Cookie 信息，用于会话管理和状态跟踪。
9. Location：用于重定向的 URL，通常在 3xx 状态码中使用。
10. Server：服务器软件的信息，通常包含服务器类型和版本。
11. Access-Control-Allow-Origin：用于跨域资源共享（CORS）的响应头，指定允许访问资源的源。
12. Access-Control-Allow-Methods：指定允许的 HTTP 方法，如 GET、POST 等。
13. Access-Control-Allow-Headers：指定允许的请求头字段。
14. Access-Control-Allow-Credentials：指定是否允许发送 Cookie。
15. Access-Control-Max-Age：指定预检请求的缓存时间。
16. Access-Control-Expose-Headers：指定允许客户端访问的响应头字段。
"""
