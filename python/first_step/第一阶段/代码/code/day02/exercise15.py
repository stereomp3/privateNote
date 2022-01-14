"""
    在控制台中，获取一个开始值，一个结束值。
    将中间的数字打印出来。
    输入：3           9
    输出：  4 5 6 7 8
"""
start = int(input("请输入开始值："))  # 3
stop = int(input("请输入结束值："))  # 9

"""
# 3 --> 9
while start < stop - 1:
    start += 1
    print(start)
# 9 --> 3
while start > stop +1:
    start -=1
    print(start)
"""
dir = 1 if start < stop else -1
while start != stop - dir:
    start += dir
    print(start)

