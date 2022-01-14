"""
    計算無窮序列前n項的和
"""
import math


def factorial_loop(n):
    factor = 1.0
    for i in range(2, n + 1):
        num = math.pow((1 / i), 0.5) * math.pow(i, 0.5)  ## (1/i)^0.5 * 根號i
        factor += num  # 累加
    return factor


print(factorial_loop(10))