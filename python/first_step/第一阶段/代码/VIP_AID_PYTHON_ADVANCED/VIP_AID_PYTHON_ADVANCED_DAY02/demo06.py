"""
    生成器表达式
"""

# 列表推导式
list01 = [34, 43, 54, 65, 67, 7]
list02 = [item for item in list01 if item > 10]
for item in list02:
    print(item)


generator02 = (item for item in list01 if item > 10)
for item in generator02:
    print(item)


for item in (item for item in list01 if item > 10):
    print(item)