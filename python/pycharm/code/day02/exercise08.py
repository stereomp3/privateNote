"""
    在終端中輸入4個數字，找出最大的
"""
number01 = float(input("第一個:"))
number02 = float(input("第二個:"))
number03 = float(input("第三個:"))
number04 = float(input("第四個:"))

max_number = number01

if max_number < number02:
    max_number = number02
if max_number < number03:
    max_number = number03
if max_number < number04:
    max_number = number04

print("最大數:"+str(max_number))
