"""
    1. 獲取一個數，判斷是偶數還奇數
    2. 獲取年分，閏年變量day賦值29，其他則是28
    1.
"""
number = int(input("請輸入數字:"))

# 如果number % 2有值(不為0，true)，就是奇數
state = "奇數" if number % 2 else "偶數"
print(state)