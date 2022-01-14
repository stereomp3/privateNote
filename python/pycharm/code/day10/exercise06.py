"""
    定義函數，根據年月日計算星期數
    星期一
    星期二
    ...
"""
import time


def count_day(year, month, day):
    time_tuple = time.strptime("%d %d %d" % (year, month, day), "%Y %m %d")
    tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_week[time_tuple[6]]


print(count_day(2021, 9, 21))
