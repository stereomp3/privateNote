"""
    函数-返回值
"""
def fun01():
    print("fun01执行喽")
    return 100# 返回100

number = fun01()
print(number)

def fun02():
    print("fun01执行喽")
    # return # return关键字后面如果没有数据，相当于返回None
    # 如果函数没有返回值，也相当于返回None

re = fun02()
print(re)

# 即使有返回值，调用者仍然可以不使用变量来接受。
fun01()