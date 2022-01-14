"""
    函数参数
        实际参数
            位置实参
                序列实参
            关键字实参
                字典实参

        形式参数
            默认形参
            位置形参
                星号元组形参
            命名关键字形参
                双星号字典形参

"""


# 1. 位置形参:约束实参必须提供     【必填】
def fun01(a, b, c):
    print(a)
    print(b)
    print(c)


# 2. 默认参数：实参可以不提供      【可选】
def fun02(a=0, b="", c=0.0):
    print(a)
    print(b)
    print(c)


fun02(1)
fun02(b="bb")


# 3. 星号元组形参：将位置实参合并为一个元组
# 只能有一个,建议形参名称位args
def fun03(*args):
    print(args)


fun03(1, 2, 3)


# fun03(a = 1,b=2)

# 4. 命名关键字形参：星号元组形参，后面的位置形参，必须使用关键字实参传递。
def fun04(*args, a, b, c):
    print(args)


fun04(1, 2, 3, 4, 5, a=1, b=2, c=3)


# 命名关键字形参：星号后面的位置形参，必须使用关键字实参传递。
def fun05(a, *, b=0, c=0):
    print(a)
    print(b)
    print(c)


fun05(1, c=3)

# print(*args, sep=' ', end='\n')
print(1, 2, 3, 4, end=" ")
print(1, 2, 3, 4, sep="-")
print(1, 2, 3, 4, end=" ", sep="-")

# 5. 双星号字典形参：将关键字实参合并为一个字典
# 只能有一个,建议形参名称位args
def fun06(**kwargs):
    print(kwargs)

fun06(a = 1,b = 2)
