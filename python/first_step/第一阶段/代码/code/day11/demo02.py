"""
    可迭代对象
"""
list01 = [34, 4, 5, 46, 57, 87]

# for item in list01:
#     print(item)

# 对象可以for的条件是什么？
# 对象具有__iter__方法
# 对象可以获取迭代器

# for 原理:
# 1. 获取迭代器对象
iterator = list01.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
    # 3. 如果没有元素,则捕获异常，停止循环。
    except StopIteration:
        break



