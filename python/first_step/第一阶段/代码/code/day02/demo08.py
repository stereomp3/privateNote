"""
    猜数字2.0版本
        如果猜错次数超过5次，则结束游戏，并提示“失败了”
"""
import random

random_number = random.randint(1, 100)
print(random_number)
count = 0
while count < 5:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break
else:
    # 当循环不满足条件时退出，才执行以下代码
    print("失败了")