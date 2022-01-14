"""
    面向对象编程

    手机
        数据：品牌、价格、颜色..
        行为：通话..
"""


class Cellphone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand, "打电话")


# 创建手机对象
# 会调用__init__构造函数
iphone01 = Cellphone("苹果", 9999, "绿色")
huawei01 = Cellphone("华为", 6666, "白色")
iphone01.call()
huawei01.call()
