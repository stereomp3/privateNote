"""
    yield --> 生成器
"""

"""
    # 生成器:可迭代对象（可以参与for） + 迭代器（产生数据）
    calss Generator:
        def __iter__(self):
            return self
        
        def __next__(self):
            ...
"""

def my_range(stop):
    number = 0
    while number < stop:
        yield number
        number += 1

# for item in my_range(5):
#     print(item)  # 0 1 2 3 4

# 惰性操作/延迟操作
my = my_range(5)
iterator = my.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
