"""
    1. 獲取一個數，判斷是偶數還奇數
    2. 獲取年分，閏年變量day賦值29，其他則是28
    2.
"""
years = int(input("請輸入年分:"))


# 不建議，可讀性低， not if years % 4 == years % 4 == 0(為0--> flase)
# answer = 29 not if years % 4  and years % 100 or not years % 400 else 28
# 建議
answer = 29 if years % 4 == 0 and years % 100 != 0 or years % 400 == 0 else 28
print(answer)