"""
    随机产生两个数字(1--10),
    在控制台中获取两个数相加的结果
    如果用户输入正确得10分,否则扣5分。
    总共３道题，最后输出得分.
    例如:“请输入8+3=?” 11  得10分
       　　"请输入4+3=?"   8   扣5分
       　　"请输入4+4=?"   8   得10分
        　 "总分是15"
"""
import random

score = 0
for i in range(3):#0 1 2
    random_number01 = random.randint(1, 10)
    random_number02 = random.randint(1, 10)
    input_number = int(input("请输入" + str(random_number01) + "+" + str(random_number02) + "=?"))
    if input_number == random_number01 + random_number02:
        score += 10
    else:
        score -= 5
print("总分是"+str(score))
