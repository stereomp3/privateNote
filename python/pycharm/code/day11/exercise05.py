"""
    定義函數，在傳統列表中獲取所有偶數
        -- 傳統思想: 將結果存入新列表再返回
        -- 生成器思想: 將結果交給生成器對象推算
        通過調適，體會惰性操作
"""
list01 = [43, 45, 65, 67, 78, 87, 453, 4]

"""自己寫
# 傳統思想
# list02 = []
# for i in list01:
#     if not i % 2:
#         list02.append(i)
# for item in list02:
#     print(item)

# 生成器思想
# def generator():
#     for i in list01:
#         if not i % 2:
#             yield i
# 
# 
# g = generator()
# for item in g:
#     print(item)
"""


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
