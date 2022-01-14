"""
    1. 使用生成器表達式在list01中找出所有字符串
    2. 使用生成器表達式找出所有大於10的整數
"""
list01 = ["悟空", 57, "八戒", True, 5.8, 10, 90]

for i in (item for item in list01 if type(item) == str):
    print(i)

for i in (item for item in list01 if type(item) == int and item > 10):
    print(i)
