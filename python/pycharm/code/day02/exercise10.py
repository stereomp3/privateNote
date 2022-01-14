"""
    輸入月份，顯示天數
"""
# month = int(input("請輸入月份:"))
# if month < 1 or month > 12:
#     print("無此月份")
# elif month == 2:
#     print("一共28天")
# elif month % 2 == 0 and month < 8:
#     print("一共30天")
# elif month % 2 == 0 and month >= 8:
#     print("一共31天")
# elif month % 2 == 1 and month < 8:
#     print("一共31天")
# elif month % 2 == 1 and month >= 8:
#     print("一共30天")

month = int(input("請輸入月份:"))
if month < 1 or month > 12:
    print("無此月份")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("一共30天")
else:
    print("一共31天")
