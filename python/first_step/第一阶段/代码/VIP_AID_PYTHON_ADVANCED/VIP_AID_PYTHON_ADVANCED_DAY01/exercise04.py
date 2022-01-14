"""
    将day07/demo05中代码拆分到两个模块中
        工具  -->  double_list_helper.py
        测试  -->  exercise04.py
"""
from double_list_helper import *

pos = Vector2(2,1)
right = Vector2.get_right()
pos.x += right.x
pos.y += right.y
print(pos.x)
print(pos.y)

list01 = [
    ["00","01","02","03","04"],
    ["10","11","12","13","14"],
    ["20","21","22","23","24"],
    ["30","31","32","33","34"],
]

print(DoubleListHelper.get_elements(list01,Vector2(3,0),Vector2.get_right(),3))

# 练习:32位置 向上获取3个元素
print(DoubleListHelper.get_elements(list01,Vector2(3,2),Vector2.get_up(),3))
# 练习:34位置 向左获取3个元素
print(DoubleListHelper.get_elements(list01,Vector2(3,4),Vector2.get_left(),3))

