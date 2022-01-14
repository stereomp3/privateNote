"""
    定義函數，根據出生年月日，計算活了多少天
"""
import time


def stay_life_day(year, month, day):
    tuple_time = time.strptime("%d %d %d" % (year, month, day), "%Y %m %d")
    stay_life = int((time.time() - time.mktime(tuple_time)) / 3600 / 24)
    return stay_life


print(stay_life_day(2002, 4, 29))
