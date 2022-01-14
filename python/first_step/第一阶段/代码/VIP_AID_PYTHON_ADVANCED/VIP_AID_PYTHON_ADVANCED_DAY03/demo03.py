"""
    外部嵌套作用域
"""

def func01():
    a = 10

    def func02():
        # 内部函数,可以访问外部嵌套变量
        # print(a)
        # 内部函数,如果修改外部嵌套变量,需要使用nonlocal语句声明
        nonlocal a
        a = 20

    func02()
    print(a)

func01()

