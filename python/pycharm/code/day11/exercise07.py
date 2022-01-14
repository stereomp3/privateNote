"""
    參照下列代碼，自訂義生成器my_zip
        list01 = ["八戒", "悟空", "蘇大強"]
        list02 = [102, 105, 107]
        for item in zip(list01,list02):
            print(item)
"""
list01 = ["八戒", "悟空", "蘇大強"]
list02 = [102, 105, 107]


# 要做完整功能麻煩
def my_zip(iterable01, iterable02):  # 使用*args
    # 判斷大小放到len裡面
    for i in range(len(iterable01)):
        yield iterable01[i], iterable02[i]


for item in my_zip(list01, list02):
    print(item)

# 自己寫
# def my_zip(*args):
#     for i in range(len(args)):
#         for y in range(len(args[i])):
#             yield args[i][y], args[i+1][y]
#
#
# for item in my_zip(list01, list02):
#     print(item)
