"""
    定义函数,在列表中获取所有偶数.
        -- 传统思想：将结果存入新列表再返回
        -- 生成器思想：将结果交给生成器对象推算
    通过调试，体会惰性操作
"""
list01 = [43, 42, 68, 66, 78, 87, 453, 4]


def get_even01():
    list_result = []
    for item in list01:
        if item % 2 == 0:
            list_result.append(item)
    return list_result

result = get_even01()
for item in result:
    print(item)

def get_even02():
    for item in list01:
        if item % 2 == 0:
           yield item

result = get_even02()
for item in result:
    print(item)