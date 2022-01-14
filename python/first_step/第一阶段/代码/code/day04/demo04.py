"""
    元组tuple
"""
# 1. 创建
tuple01 = ()
tuple02 = tuple()

tuple01 = (12, 33, 4)
list01 = ["a", "b", "c"]
tuple02 = tuple(list01)
print(tuple02)
list03 = list(tuple01)

tuple02 = (1,)  # 元组中只有一个元素
tuple02 = 1, 2, 3  #
print(tuple02)

# 2. 查询
tuple03 = ("a", "b", "c")
a, b, c = tuple03

# 索引
print(tuple02[-1])

# 切片
print(tuple02[:2])

# 循环
for item in tuple02:
    print(item)
