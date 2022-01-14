"""
    bool 运算
    练习:exercise05.py
    练习:exercise06.py
"""
# 1. 比较运算符
# 参与的数据：主要就是数值
# 比较之后的结果是：bool类型
number01 = 5
number02 = 8
print(number01 > number02)  # 5 > 8 False
print(number01 < number02)  # 5 < 8 True
print(number01 == number02)  # 5 == 8 False
# print(5 > "10")  # 不能用整数与字符串进行大小的比较
print(5 == "5")  # False  类型不一样

# 2. 逻辑运算符
# 参与的数据：主要就是bool类型的数据
# 比较之后的结果是：bool类型
# 与and 一假俱假--> 都得满足条件，结论才满足条件  表达并且的关系
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# 或or 一真俱真 --> 一个满足就行   表达或者的关系
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

# 非not 取反
print(not True)

