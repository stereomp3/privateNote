"""
    定義函數，在終端中獲取任意整數，累加每位數字
"""


def add_up_each_digit(number):
    sum_number = 0
    for item in number:
        sum_number += int(item)
    return sum_number


result = add_up_each_digit(input("請輸入:"))

print(result)
