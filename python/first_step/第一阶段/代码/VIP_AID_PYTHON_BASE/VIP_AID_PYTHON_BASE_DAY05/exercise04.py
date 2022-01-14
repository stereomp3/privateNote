"""
    定义函数，判断列表中是否存在相同元素
    输入：[3,4,6,8,6]
    输出：True
"""

def is_repeating(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True
    return False

list01 = [3,4,6,8,7]
print(is_repeating(list01))