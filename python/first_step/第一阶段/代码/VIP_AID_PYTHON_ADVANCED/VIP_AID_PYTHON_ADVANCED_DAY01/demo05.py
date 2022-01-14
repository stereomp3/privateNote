"""
    时间处理
"""
import time

# 1. 获取当前时间戳:从1970年1月1日到现在经过的秒数
print(time.time())# 1576595536.5944133

# 2. 获取当前时间元组（年、月、日、时、分、秒、星期、年的第几天、夏令时）
time_tuple = time.localtime()
print(time_tuple)

# 3. 时间戳--->时间元组
print(time.localtime(1576595536.5944133))

# 4. 时间元组--->时间戳
print(time.mktime(time_tuple))

# 5. 时间元组--->字符串
print(time.strftime("%y/%m/%d %H:%M:%S",time_tuple))# 19/12/17 23:17:23
print(time.strftime("%Y/%m/%d %H:%M:%S",time_tuple))# 19/12/17 23:17:23

# 6. 字符串--->时间元组
print(time.strptime("19/12/17 23:17:23","%y/%m/%d %H:%M:%S"))







