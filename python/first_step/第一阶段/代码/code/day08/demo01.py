"""
    封装-设计思想
        请以面向对象的思想，描述以下场景：
            老张开车去东北
"""

# 写法1：每次都会创建一辆新车
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, pos):
        print("去", pos)
        car = Car()
        car.run()


class Car:
    def run(self):
        print("嘟嘟嘟...")


lz = Person("老张")
lz.go_to("东北")
"""

# 写法2：老张的车
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def go_to(self, pos):
        print("去", pos)
        self.car.run()


class Car:
    def run(self):
        print("嘟嘟嘟...")


lz = Person("老张")
lz.go_to("东北")
lz.go_to("西北")
"""

# 写法3：人与车的关系松散
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, pos, vehicle):
        print("去", pos)
        vehicle.run()


class Car:
    def run(self):
        print("嘟嘟嘟...")

lz = Person("老张")
c01 = Car()
lz.go_to("东北", c01)
