# 练习3：在终端中首先获取一个变量，再获取一个变量，然后交换他们，最后输出两个变量。

variable01 = input("请输入第一个变量：")
variable02 = input("请输入第二个变量：")
# 变量交换思想：
# temp = variable01
# variable01= variable02
# variable02 = temp

# python交换变量
variable01, variable02 = variable02, variable01

print("第一个变量是：" + variable01)
print("第二个变量是：" + variable02)
