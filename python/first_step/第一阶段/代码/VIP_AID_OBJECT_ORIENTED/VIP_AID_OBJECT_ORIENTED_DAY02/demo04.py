"""
    静态方法引入
"""
list01 = [
    ["00","01","02","03","04"],
    ["10","11","12","13","04"],
    ["20","21","22","23","34"],
    ["30","31","32","33","34"],
]

class Vector2:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

def get_right():
    return Vector2(0,1)

pos = Vector2(2,1)
right = get_right()
pos.x += right.x
pos.y += right.y
print(pos.x)
print(pos.y)

# 需求：30位置上向右获取3个元素
def get_elements(list_target,vect_pos,vect_dir,count):
    list_result = []
    for __ in range(count):
        vect_pos.x += vect_dir.x
        vect_pos.y += vect_dir.y
        element = list_target[vect_pos.x][vect_pos.y]
        list_result.append(element)
    return list_result

print(get_elements(list01,Vector2(3,0),get_right(),3))

