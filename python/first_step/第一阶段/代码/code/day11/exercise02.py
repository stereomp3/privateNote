"""
    练习1:使用迭代思想,获取元组中所有元素
    练习2:使用迭代思想,获取字典中所有k.v
"""
dict01 = {"唐僧":27,"悟空":29,"八戒":30}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key,dict01[key])
    except StopIteration:
        break