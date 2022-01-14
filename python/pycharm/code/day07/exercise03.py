"""
    !!重要技術!!
    在列表裡面
        練習 : 32位置 向上獲取3個元素
        練習 : 34位置 向左獲取3個元素
"""

list01 = [
    ["00", "01", "02", "03", "04"],
    ["10", "11", "12", "13", "14"],
    ["20", "21", "22", "23", "24"],
    ["30", "31", "32", "33", "34"],
]


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def move_left():
        return Vector(0, 1)

    @staticmethod
    def move_left():
        return Vector(0, -1)

    @staticmethod
    def move_up():
        return Vector(-1, 0)

    @staticmethod
    def move_down():
        return Vector(1, 0)


class DoubleListHelper:
    @staticmethod
    def get_element(list_target, vector_pos, vector_dir, count):
        result = []
        for __ in range(count):
            vector_pos.x += vector_dir.x
            vector_pos.y += vector_dir.y
            element = list_target[vector_pos.x][vector_pos.y]  # 這步 重要
            result.append(element)
        return result


print(DoubleListHelper.get_element(list01, Vector(3, 4), Vector.move_up(), 3))
