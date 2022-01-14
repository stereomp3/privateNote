"""
    定义父类
        车(数据：品牌,价格)
    定义子类
        电动车(数据:充电速度,电池容量)
    画出内存图
"""


class Car:
    def __init__(self, brand="", price=0):
        self.brand = brand
        self.price = price


class Electrocar(Car):
    def __init__(self, brand="", price=0, charging_speed=0, battery_capacity=0):
        super().__init__(brand,price)
        self.charging_speed = charging_speed
        self.battery_capacity = battery_capacity

e01 = Electrocar("宝马",300000,60,10000000)
