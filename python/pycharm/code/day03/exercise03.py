"""
    累加 10 ~ 50 間個位數不是 2, 5, 9的整數
"""
sum_value = 0
for item in range(10, 51, 1):
    if item % 10 == 2 or item % 10 == 5 or item % 10 == 9:
        continue
    sum_value += item
print(sum_value)
# 可以把重複的部分用變數做統一(unit = item % 10)
