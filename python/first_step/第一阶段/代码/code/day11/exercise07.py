"""
    参照下列代码,自定义生成器my_zip
"""


def my_zip(iterable01, iterable02):
    for i in range(len(iterable01)):
        yield (iterable01[i], iterable02[i])


list01 = ["八戒", "悟空", "苏大强"]
list02 = [102, 105]

for item in my_zip(list01, list02):
    print(item)
