"""
    不能用for
    練習1: 使用迭代思想，獲取元組中所有元素
    練習2: 使用迭代思想，獲取字典中所以有k.v
"""

tuple01 = (1, 2, 3, 4, 5, 6, 7)
dict01 = {"name": "悟空", "age": 26, "sex": "male"}

# for i in tuple01:
#     print(i)
#
# for k, v in dict01.items():
#     print(k)
#     print(v)

# iterator = tuple01.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
Myiterator = dict01.items().__iter__()
while True:
    try:
        item = Myiterator.__next__()
        print(item)
    except StopIteration:
        break

iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, str(dict01[key]))
    except StopIteration:
        break

