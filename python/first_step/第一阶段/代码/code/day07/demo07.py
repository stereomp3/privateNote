"""
    封装 -- 属性
"""
# 1. 创建实例变量
# 2. 提供两个公开的读写方法
# 3. 创建类变量存储property对象

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise Exception("我不要")

    # 类变量
    # property 作用:拦截
    age = property(get_age, set_age)


w01 = Wife("宁宁", 25)
w02 = Wife("铁锤", 26)
# w01.set_age(27)
w01.age = 27
print(w01.age)
print(w01.__dict__)
