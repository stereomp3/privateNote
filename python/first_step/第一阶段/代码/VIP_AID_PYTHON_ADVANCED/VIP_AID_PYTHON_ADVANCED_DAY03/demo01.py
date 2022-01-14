"""
    lambda表达式
        匿名方法
        语法：
            lambda 参数:方法体
    练习:exercise01
"""
# def func01(a,b):
#     return a > b
#
# print(func01(10,20))

# 1. 有参数有返回值
func01 = lambda a,b:a > b
print(func01(10,20))

# 2. 无参数有返回值
# def func02():
#     return "ok"
#
# print(func02())
func02 = lambda :"ok"
print(func02())

# 3. 无参数无返回值
# def func03():
#     print("ok")
#
# func03()

func03 = lambda :print("ok")
func03()

# 4. 有参数无返回值
# def func03(a):
#     print(a)
#
# func03(100)
func03 = lambda a:print(a)
func03(100)

# 5. lambda 不支持赋值语句
# def func05(iterable):
#     iterable[0] = 100
#
# list01 = [1]
# func05(list01)
# print(list01)

# func05 = lambda iterable: iterable[0] = 100

# 6. lambda 不支持多条语句
# def func06(a,b):
#     print(a)
#     print(b)
#
# func06(10,20)

# func06 = lambda a,b: print(a);print(b)
