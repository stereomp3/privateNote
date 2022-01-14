"""
    continue
    练习:exercise03.py
"""

# 累加1 --50
# sum_value = 0
# for item in range(1, 51):
#     if item % 5 == 0:
#         sum_value += item
# print(sum_value)

sum_value = 0
for item in range(1, 51):
    # 如果不满足累加条件，那么跳过当前数字
    if item % 5 != 0:
        continue
    sum_value += item
print(sum_value)








