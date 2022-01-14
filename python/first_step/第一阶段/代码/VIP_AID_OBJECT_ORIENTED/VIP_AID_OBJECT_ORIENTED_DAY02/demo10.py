"""
    复习
"""
class MyClass:

    # 类成员:类
    total_count = 0

    @classmethod
    def print_total_count(cls):
        print(cls.total_count)

    # 实例成员:对象
    def __init__(self, name=""):
        self.name = name

    def print_self(self):
        print(self.name)

    # 静态方法：类
    @staticmethod
    def tools():
        print("独立的功能")

c01 = MyClass()
c01.name = "xx"
c01.print_self()