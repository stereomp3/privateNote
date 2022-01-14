"""
    製作猜數字遊戲(1~100)
    # 隨機數工具
    import random

    #產生隨機數
    random_number = random.randint(1, 100)
"""
import random
random_number = random.randint(1, 100)
count = 0
guess_number = None
print(random_number)
while guess_number != random_number:
    guess_number = int(input("請輸入數字:"))
    count += 1
    if guess_number > random_number:
        print("大了")
    elif guess_number < random_number:
        print("小了")
    else:
        print("猜對了，一共猜" + str(count) + "次")
        break
else:
    # 當循環不滿足條件時退出，才執行(break的不會到這裡)
    print("失敗了")


