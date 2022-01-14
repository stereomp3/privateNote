"""
    在終端中輸入日期(月日)，計算是這一年的第幾天
    EX:
        3月15日 --> 31 + 28 + 15
        5月20日 --> 31 + 28 + 31 + 30 + 20
"""
# 專業
month = int(input("請輸入月份:"))
day = int(input("請輸入天數:"))
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# total_day = 0
# for item in day_of_month[:month - 1]:
#     total_day += item
total_day = sum(day_of_month[:month - 1])
total_day += day
print(total_day)


# 自己寫法
# sum_day = 0
# tuple_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# str_input = input("請輸入日期:")
# list_temp = str_input.split("月")
# print(list_temp)
# if int(list_temp[0]) < 13:
#     for i in range(int(list_temp[0])-1):
#         sum_day += int(tuple_month[i])
# else:
#     print("月份輸入錯誤")
#
# str_temp = list_temp[1]
# list_temp2 = list(str_temp)
# del list_temp2[-1]
# if list_temp2[1]:
#     list_temp2[0] += list_temp2[1]
# print(sum_day + int(list_temp2[0]))
