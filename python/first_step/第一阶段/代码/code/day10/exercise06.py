"""
    定义函数,根据年月日计算星期数
    星期一
    星期二
    ...
"""
import time


def get_week(year, month, day):
    tuple_time = time.strptime("%d/%d/%d" % (year, month, day), "%Y/%m/%d")
    tuple_weeks = ("星期一","星期二","星期三","星期四","星期五","星期六","星期日",)
    return tuple_weeks[tuple_time[6]]


print(get_week(2019,12,5))
