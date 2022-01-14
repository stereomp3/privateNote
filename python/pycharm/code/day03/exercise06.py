"""
    一個球從100m高度落下，每次彈回高度的一半
    計算:
    總共彈多少次才落地(最小談起高度0.01m)
    總共經過多少米
"""

height = 100
distance = height
times = 0

# 判斷彈起來的高度，如果沒/2，是判斷彈之前的
while height / 2 > 0.01:
    height /= 2
    distance += height*2
    times += 1

print("總共彈"+str(times)+"次落地")
print("總共經過"+str(distance)+"米")