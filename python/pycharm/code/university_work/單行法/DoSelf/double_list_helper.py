class Vector2:
    """
        向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def get_left():
        return Vector2(0, -1)

    @staticmethod
    def get_right():
        return Vector2(0, 1)

    @staticmethod
    def get_up():
        return Vector2(-1, 0)


class DoubleListHelper:
    """
        二维列表助手类
    """

    @staticmethod
    def get_elements(list_target, vect_pos, vect_dir, count):
        list_result = []
        for __ in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = list_target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result