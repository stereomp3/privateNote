"""
    調用下列函數
        形參順序
            從左自右
                位置形參 --> 星號元組形參 --> 命名關鍵字形參 --> 雙星號字典形參
"""


def fun01(*args, **kwargs):
    print(args)
    print(kwargs)


def fun02(a, *args, b, c="", **kwargs):
    print(a)
    print(args)
    print(b)
    print(c)
    print(kwargs)


list01 = [1, 2, 3, 4]
dict01 = {"a": 1, "b": 2, "c": 3, "d": 4}

print("fun01")
fun01(1, 2, 3, a=1, b=2, c=3)
fun01(*list01)

print("fun02")
fun02(1, 2, 3, b=2, c=3, d=2, e=3)
fun02(**dict01)

