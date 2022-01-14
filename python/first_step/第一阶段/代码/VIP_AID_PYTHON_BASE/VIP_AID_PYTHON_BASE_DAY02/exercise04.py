"""
    在终端中获取一个四位整数，计算每位相加和。
    输入:1234
    输出:10
"""

print(1 > 10 or 10 > 1)
print(5 < 8 and 7 < 4)
print("3" == "3" and 8 > 4)
print(6 == "6" or 9 > 3)
print("a" != "1" and 5 == 5)



number = int(input("请输入4位整数："))
# 个位 number % 10
result = number % 10
# 十位 number // 10% 10
result += number // 10% 10
# 百位 number // 100 % 10
result += number // 100 % 10
# 千位 number // 1000
result += number // 1000
print(result)
