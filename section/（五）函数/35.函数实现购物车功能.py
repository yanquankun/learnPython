"""
@Desc: 本讲解如何实现购物车功能
@Author: Mint.Yan
@Date: 2025-06-177 13:39:34
"""

# 需求描述：
# • 展示商品
# • 添加商品、删除商品
# • 调整商品数量
# • 费用总计
# 购物⻋功能分析
# • 忽略功能：库存数量、商品类目

# 商品 采用二维列表存储
# 模拟数据库
# 商品id|商品名称|商品类型|商品价格
products = [[1000, "iphone", "phone", 12000],
            [1001, "ipad", "pad", 15000],
            [1002, "macbook", "laptop", 20000]]

# 购物车 "product_id":"product_number"
# 采用字典存储，键为商品ID，值为商品数量
cart = {1000: 5, 1001: 2}


# 需求1：展示商品
def display_products():
    """
    展示商品列表
    """
    print("商品列表:")
    print("ID\t名称\t类型\t价格")
    for product in products:
        print(f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}")


display_products()


# 需求2：展示购物车商品详情
def display_cart():
    """
    展示购物车商品详情
    """
    print("购物车商品详情:")
    print("ID\t名称\t数量\t单价\t小计")
    total_cost = 0
    for product_id, quantity in cart.items():
        # 查找商品信息
        product = next((p for p in products if p[0] == product_id), None)
        if product:
            subtotal = product[3] * quantity  # 小计 = 单价 * 数量
            total_cost += subtotal
            print(f"{product[0]}\t{product[1]}\t{quantity}\t{product[3]}\t{subtotal}")
    print(f"总计: {total_cost}")


display_cart()


# 需求3：添加商品到购物车
def add_to_cart(product_id, quantity):
    """
    添加商品到购物车
    :param product_id: 商品ID
    :param quantity: 商品数量
    """
    if product_id in cart:
        cart[product_id] += quantity  # 增加数量
    else:
        cart[product_id] = quantity  # 新增商品
    print("===商品已添加到购物车===")
    display_cart()


add_to_cart(1000, 3)  # 添加3个iphone到购物车


# 需求4：删除购物车中的商品
def remove_from_cart(product_id, number=1):
    """
    从购物车中删除商品
    :param product_id: 商品ID
    """
    if product_id in cart:
        if cart[product_id] > number:
            cart[product_id] -= number
        else:
            del cart[product_id]
        print("===商品已从购物车中删除===")
        display_cart()
    else:
        print("===商品不在购物车中===")


remove_from_cart(1000, 2)  # 删除2个iphone从购物车中
