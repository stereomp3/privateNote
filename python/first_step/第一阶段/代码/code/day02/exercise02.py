"""
    在终端中录入距离，时间，初速度，计算加速度。
    匀变速直线运动的位移与时间公式：
        距离=初速度 * 时间 + 加速度 * 时间平方的一半
    输入：
        距离:100
        初速度:2
        时间:5
    输出：加速度7.2

    公式：
        距离=初速度 * 时间 + 加速度 * 时间**2 * 0.5
        (距离 - 初速度 * 时间) * 2/ 时间**2 = 加速度
"""
distance = float(input("请输入距离："))
initial_velocity = float(input("请输入初速度："))
time = float(input("请输入时间："))
accelerated_speed = (distance - initial_velocity * time) * 2 / time ** 2
print("加速度是：" + str(accelerated_speed))



