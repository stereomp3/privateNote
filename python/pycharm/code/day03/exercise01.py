"""
    在終端中獲取任意整數，累加每位數字
"""
number = input("輸入數字:")
sum = 0
for item in number:
    sum += int(item)
print(sum)