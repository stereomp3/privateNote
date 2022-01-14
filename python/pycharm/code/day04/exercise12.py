"""
    使用for繪製下列圖形:
    *****
    #####
    *****
    #####
"""
for i in range(4):
    for j in range(5):
        if i % 2: print("#", end="")
        else: print("*", end="")
    print()
