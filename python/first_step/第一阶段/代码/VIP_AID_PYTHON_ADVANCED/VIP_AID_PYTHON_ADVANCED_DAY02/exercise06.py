"""
    参照下列代码,自定义生成器my_enumerate.
"""


def my_enumerate(iterable):
    index = 0
    for item in iterable:
        yield (index, item)
        index += 1


dict01 = {"悟空": 26, "八戒": 28}
for item in my_enumerate(dict01):
    print(item)

for item in enumerate(dict01):
    print(item)
