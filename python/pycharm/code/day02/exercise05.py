"""
    判斷是否為閏年(4年一遇，百年不遇，400年遇)
"""
year = int(input("請輸入年分:"))
print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
