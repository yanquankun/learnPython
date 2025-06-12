"""
@Desc: 本讲解Python内置数据类型的match语句
@Author: Mint.Yan
@Date: 2025-06-163 13:45:52
"""

# match语句是Python 3.10引入的一种新的控制流结构，用于模式匹配。

http_response_status = 404
match http_response_status:
    case 400:
        print("Bad request")
    # | 是一个或操作符，可以匹配多个值
    case 404 | 405:
        print("Not found")
    case 418:
        print("I'm a teapot")
    # _ 是一个通配符，匹配所有未被前面的case捕获的情况
    case _:
        print("Something's wrong with the internet")
