"""
    装饰器
    练习:exercise04.py
"""


def func01():
    print("func01执行喽")
    return "ok"


def func02(a):
    print(a, "func02执行喽")


def print_func_name(func):
    def wrapper(*args, **kwargs):  # 合
        # 新功能
        print(func.__name__)
        # 旧功能
        return func(*args, **kwargs)  # 拆

    return wrapper


# func01 = 新功能  +  旧功能
# func01 = print_func_name + func01
func01 = print_func_name(func01)

print(func01())  # 执行的是内部函数

func02 = print_func_name(func02)

func02(100)
