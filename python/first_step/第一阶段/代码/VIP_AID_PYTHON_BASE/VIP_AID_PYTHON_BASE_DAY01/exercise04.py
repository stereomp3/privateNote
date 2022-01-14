# 练习1：在终端中录入一个半径，输出圆形的面积(3.14 × 半径的平方)
#       输出的格式：圆形面积是：xxx

radius = input("请输入圆形半径:")
area = 3.14 * float(radius) ** 2
print("圆形面积是：" + str(area))

