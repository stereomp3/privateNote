"""
    參照下列代碼，自訂義生成器my_enumerate
        dict01 = {"悟空": 26, "八戒": 28}
        for item in enumerate(dict01):
            print(item)
"""
dict01 = {"悟空": 26, "八戒": 28}


def my_enumerate(iterable):
    index = 0
    for i in iterable:
        yield index, i
        index += 1


for item in my_enumerate(dict01):
    print(item)
