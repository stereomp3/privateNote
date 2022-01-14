"""
    多继承
        继承：统一概念/隔离变化
        同名方法解析顺序 mro
"""


class A:
    def func(self):
        print("A")


class B(A):
    def func(self):
        print("B")


class C(A):
    def func(self):
        print("C")


class D(B, C):
    def func(self):
        print("D")
        super().func()# ?
        C.func(self)# 调用指定名称的父类同名方法


d01 = D()
d01.func()

print(D.mro())



