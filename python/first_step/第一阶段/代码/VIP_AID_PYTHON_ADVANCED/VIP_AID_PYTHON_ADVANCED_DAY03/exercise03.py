"""
    闭包应用
        逻辑连续
        装饰器
"""

def give_gife_money(money):
    print("得到了", money, "元压岁钱")

    def child_buy(target, price):
        nonlocal money
        money -= price
        print("购买了", target, "还剩", money, "元")

    return child_buy

action = give_gife_money(500)
action("变形金刚", 130)
action("遥控飞机", 250)
action("零食", 120)
