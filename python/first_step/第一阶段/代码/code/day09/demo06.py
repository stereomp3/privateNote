"""
    设计思想
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        print("走喽")
        # 1. 调用交通工具(父)
        if not isinstance(vehicle,Vehicle):
            raise Exception("传入的必须是交通工具")

        vehicle.transport()


class Vehicle:
    """
        交通工具:隔离人与具体交通工具的变化
    """

    def transport(self):
        pass


# -------------------------------------
class Car(Vehicle):
    # 3. 重写
    def transport(self):
        print("嘟嘟～")


class Airplane(Vehicle):

    def transport(self):
        print("嗖嗖~")


p01 = Person("老张")
c01 = Car()
a01 = Airplane()
# 2. 创建子类对象
p01.go_to(c01)
