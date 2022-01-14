"""
    定義函數，判斷列表中是否存在相同元素
    input : [3,4,6,8,6]
    output : True
"""


def detect_same_element(list01):
    for r in range(len(list01) - 1):
        for c in range(i + 1, len(list01)):
            if list01[r] == list01[c]:
                return True
    return False


print(detect_same_element([3, 4, 6, 8, 6]))
