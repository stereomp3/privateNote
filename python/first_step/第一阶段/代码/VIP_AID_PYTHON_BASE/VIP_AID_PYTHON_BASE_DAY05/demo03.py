"""
    函数-应用
    练习：exercise02 ~exercise04
"""


# 函数：封装一个特定功能，表示一个行为。
#      小而精
# 两个数值相加功能
# def add():
#     number_one = float(input("请输入第一个数据："))
#     number_two = float(input("请输入第二个数据："))
#     result = number_one + number_two
#     print("结果是：" + str(result))
#
# add()

def add(number_one, number_two):
    return number_one + number_two

result = add(5, 2)

