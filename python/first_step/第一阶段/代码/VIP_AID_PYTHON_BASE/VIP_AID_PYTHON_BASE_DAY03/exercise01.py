"""
在终端中获取任意整数，累加每位数字。
输入：“12345”
输出：15
"""
number = input("请输入整数：")
sum_value = 0
for item in number:
    # “1” --> 1
    sum_value += int(item)
print("结果是："+str(sum_value))
