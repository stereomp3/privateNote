"""
    函数式编程 - 语法
"""
def func01():
    print("func01执行")

a = func01
a()

def func02():
    print("func02执行")

# 通用
def func03(func):
    print("func03执行")
    func()

func03(func02)
func03(func01)


