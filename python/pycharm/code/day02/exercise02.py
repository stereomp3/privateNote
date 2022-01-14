"""
    在終端中輸入距離、時間、初速度，計算加速度
    S = V0*t + a * (t**2/2)
"""
distance = float(input("請輸入距離:"))
initial_velocity = float(input("請輸入初速度:"))
time = float(input("請輸入時間:"))

accelerate_speed = (distance - (initial_velocity*time)) / (time**2/2)

print("加速度是:"+str(accelerate_speed))
