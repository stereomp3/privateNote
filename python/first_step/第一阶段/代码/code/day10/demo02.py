"""
    模块
    练习：exercise04.py/exercise05.py
"""
# 导入方式1： import 模块名
# 使用: 模块名.成员
# 本质：创建变量模块地址
# 适用性：面向过程的函数、全局变量
# import module01
#
# print(module01.g01)
# module01.func01()
# module01.MyClass.func03()
# c01 = module01.MyClass()
# c01.func02()

# 导入方式2： from 模块名 import 成员
# 使用: 直接使用成员
# 本质：将其他模块成员导入到当前作用域中（小心命名冲突）
# 适用性：面向对象的类
# from module01 import g01
# from module01 import func01
# from module01 import MyClass
#
# func01()
#
# def func01():
#     print("demo02 -- func01")
#
# print(g01)
# func01()
# MyClass.func03()
# c01 = MyClass()
# c01.func02()


# 导入方式3： from 模块名 import 成员
# 使用: 直接使用成员
# 本质：将其他模块成员导入到当前作用域中（小心命名冲突）
from module01 import *

print(g01)
func01()
MyClass.func03()
c01 = MyClass()
c01.func02()
