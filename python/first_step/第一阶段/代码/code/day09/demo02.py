"""
    继承 - 数据
"""


class Person:
    def __init__(self, name=""):
        self.name = name


class Student(Person):
    def __init__(self, name="", score=0):
        super().__init__(name)
        self.score = score


# 如果子类没有构造函数,直接使用父类构造函数
s01 = Student("悟空", 100)
print(s01.name)
