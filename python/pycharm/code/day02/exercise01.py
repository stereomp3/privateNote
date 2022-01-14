"""
    古代的秤一斤有16兩，在終端獲取兩，得到幾斤幾兩
"""
liang_weight = int(input("請輸入兩:"))

jin = str(liang_weight // 16)
liang = str(liang_weight % 16)

print("一共是"+jin+"斤"+liang+"兩")