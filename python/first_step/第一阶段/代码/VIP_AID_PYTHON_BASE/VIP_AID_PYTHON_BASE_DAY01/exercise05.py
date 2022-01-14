# 练习2：在终端中分别录入3个数据(分钟数、小时数、天数)
#       输出总秒数
minute = float(input("请输入分钟："))
hour = float(input("请输入小时："))
day = float(input("请输入天："))

result = minute * 60 + hour * 60 * 60 + day * 24 * 60 * 60

print("总秒数是：" + str(result))
