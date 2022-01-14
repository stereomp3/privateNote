"""
    輸入兩個數，印出中間的數字
"""
# max_value = int(input("輸入數字:"))
# min_value = int(input("輸入數字:"))
#
# if min_value > max_value:
#     max_value, min_value = min_value, max_value
#
# while min_value < max_value - 1:
#     min_value += 1
#     print(min_value)

start = int(input("輸入數字:"))
stop = int(input("輸入數字:"))

"""
# 3 --> 9
while start < stop - 1:
    start += 1
    print(start)

# 9 --> 3
while start > stop + 1:
    start -= 1
    print(start)
"""
# 有重複的代碼，可以寫成下面的方法
dir = 1 if start < stop else -1
while start != stop - dir:
    start += dir
    print(start)

