"""
    終端中輸入4位整數，計算每相位相加和
"""
number = int(input("請輸入4位整數:"))
sum = number // 1000 + number // 100 % 10 + number // 10 % 10 + number % 10
# sum = number // 1000 + number % 1000 // 100 + number % 100 // 10 + number % 10 自己寫的
print("每個相位相加等於:"+str(sum))

