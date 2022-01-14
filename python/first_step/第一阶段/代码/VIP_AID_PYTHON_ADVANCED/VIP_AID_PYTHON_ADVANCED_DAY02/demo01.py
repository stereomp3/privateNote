"""
    异常处理
        主动抛出异常
"""


class AgeRangeError(Exception):
    def __init__(self, name="", error_id=0, error_code=""):
        self.name = name
        self.error_id = error_id
        self.error_code = error_code


class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            # 多个错误信息(错误名称,错误编号,错误代码...)
            raise AgeRangeError("年龄超过范围错误", 1324, "if 20 <= value <= 30")
            # raise Exception("我不要")

try:
    shuanger = Wife(40)
except AgeRangeError as e:
    print(e.name)
    print(e.error_id)
    print(e.error_code)
