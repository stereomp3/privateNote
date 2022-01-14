"""
    函数-参数
    练习:exercise01
"""

def attack():
    """
        攻击函数
    """
    print("侧踹")
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("肘击")

# attack()
# ...
attack()

# 有参数函数
# 形式参数
def attack_repeat(count):
    """
        重复攻击
    :param count:int类型，重复的次数 
    """
    for i in range(count):
        print("侧踹")
        print("直拳")
        print("摆拳")
        print("勾拳")
        print("肘击")

# 实际参数
attack_repeat(3)

"""
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
#.......
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
#.......
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
"""