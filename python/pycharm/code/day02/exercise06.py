"""
    輸入季節，打應相對月份
"""
season = input("請輸入季節:")

if season == "春":
    print("1月2月3月")
elif season == "夏":
    print("4月5月6月")
elif season == "秋":
    print("7月8月9月")
elif season == "冬":
    print("10月11月12月")
else:
    print("無此季節")