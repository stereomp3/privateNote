"""
    出隨機3個題目，正確10分，錯誤扣5分，給用戶做完後顯示分數
"""
import random

# count = 0 ，用while要多一個變數
sum_value = 0
for i in range(3): # 這邊是預定次數跑3次，所以不用while，用for會更方便
    random_number01 = random.randint(1, 10)
    random_number02 = random.randint(1, 10)
    UserInput = int(input("請輸入" + str(random_number01) + "+" + str(random_number02) + "="))
    if UserInput == random_number01 + random_number02:
        sum_value += 10
    elif sum_value <= 0:
        sum_value = 0
    else:
        sum_value -= 5
    # count += 1
print("總分是:"+str(sum_value))