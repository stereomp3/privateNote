"""
    定義父類
        車(數據:品牌,價格)
    定義子類
        電動車(數據:充電速度,電池容量)
    畫出內存圖
"""


class Car:
    def __init__(self, brand="", price=0):
        self.brand = brand
        self.price = price


class ElectricCar(Car):
    def __init__(self, brend, price, charging_speed=0, battery_capcity=0):
        super().__init__(brend, price)
        self.charging_speed = charging_speed
        self.battery_capacity = battery_capcity



