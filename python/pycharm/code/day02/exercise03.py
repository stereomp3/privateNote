"""
    輸入秒數，求得時間
"""
second = int(input("請輸入秒數:"))
day = second // (60*60*24)
day_left = second % (60*60*24)
hours = day_left // (60*60)
hours_left = day_left % (60*60)
minute = hours_left // 60
minute_left = hours_left % 60


print("一共是"+str(day)+"天"+str(hours)+"小時"+str(minute)+"分"+str(minute_left)+"秒")


"""
這樣寫比較簡潔
total_second = int(input("請輸入秒數"))
second = total_second % 60
hour = total_second // 60 // 60
minute = total_second // 60 % 60
print("一共是"+str(hour)+"小時"+str(minute)+"分"+str(second)+"秒")
"""