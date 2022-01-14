"""
    封装 -- 私有成员
        障眼法：修改了私有变量名称
            本质： __变量名  -->   _类名__变量名
"""
# 1. 私有化实例变量
# 2. 提供两个公开的读写方法

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.__age = age
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise Exception("我不要")


w01 = Wife("宁宁", 25)
w02 = Wife("铁锤", 26)
w01.set_age(27)
print(w01.get_age())

w01.__age = 100
# print(w01.__age)# 私有化
print(w01.__dict__)
print(w01._Wife__age)# ????
