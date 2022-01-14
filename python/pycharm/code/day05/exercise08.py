"""
    函數參數
        形式參數:
"""


# 1. 位置形參:約束實參必須提供       [必填]
def fun01(a, b, c):
    print(a)
    print(b)
    print(c)

print("/2///////////")
# 2. 默認參數:實參可以不提供         [可選]
def fun02(a=0, b="", c=0.0):
    print(a)
    print(b)
    print(c)


fun02(1)
fun02(b="bb")

print("/3///////////")
# 3. 星號元組形參:將位置實參合併為一個元組
# 參數只能有一個，建議命名為args
def fun03(*args):
    print(args)


fun03(1, 2, 3)


# fun03(a=1,b=2) #報錯

print("/4///////////")
# 4. 命名關鍵字形參:星號元組形參，後面的位置形參，必須用關鍵字實參傳遞
def fun04(*args, a, b, c):
    print(args)


fun04(1, 2, 3, 4, 5, a=1, b=2, c=3)

print("/5///////////")
# 命名關鍵字形參:星號後面的位置形參，必須用關鍵字實參傳遞
def fun05(a, *, b=0, c=0):  # a 用位置形參，一定要值，其他的是默認參數
    print(a)
    print(b)
    print(c)


fun05(1, c=3)
# fun05(1,2,3) # 報錯


# def print(*args, sep=' ', end='\n'):
print(1, 2, 3, 4, end=" ")
print(1, 2, 3, 4, sep="-")

print("/6///////////")
# 5. 雙星號字典形參:將關鍵字實參合併為一個字典
# 參數只能有一個，建議命名為kwargs
def fun06(**kwargs):
    print(kwargs)


fun06(a=1, b=2)
# fun06(1, 2, 3) # 報錯
