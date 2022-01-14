"""
    定義函數，多個數值累加
"""


def sum(*args):
    result = 0
    for i in args:
        result += i
    return result


print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 上面的*args只是將數值自動轉成容器，我們也可以自己用容器使用下面的一般方法
# def sum02(args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
#
# print(sum02([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
