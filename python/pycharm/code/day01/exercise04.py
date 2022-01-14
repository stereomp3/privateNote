"""
    轉換成秒
"""
minutes = float(input("請輸入分鐘:"))
hours = float(input("請輸入小時:"))
days = float(input("請輸入天數:"))

second = 60 * (minutes + 60 * (hours + days * 24))
print("一共是"+str(second)+"秒")
