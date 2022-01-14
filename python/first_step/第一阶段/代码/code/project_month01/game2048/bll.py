"""
    游戏核心逻辑控制器
"""
import random

from model import LocationModel


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并数据
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移动
        """
        for line in self.map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向右移动
        """
        for line in self.map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __square_matrix_tranpose(self):
        for c in range(len(self.map) - 1):
            for r in range(c + 1, len(self.map)):
                self.map[r][c], self.map[c][r] = self.map[c][r], self.map[r][c]

    def move_up(self):
        """
            向上移动
        """
        self.__square_matrix_tranpose()
        self.move_left()
        self.__square_matrix_tranpose()

    def move_down(self):
        """
            向下移动
        """
        self.__square_matrix_tranpose()
        self.move_right()
        self.__square_matrix_tranpose()

    def generate_new_number(self):
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0: return
        loc = random.choice(self.__list_empty_location)
        # self.map[loc[0]][loc[1]] = self.__select_random_number()
        self.map[loc.r][loc.c] = self.__select_random_number()

    def __select_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.map[r][c] == 0:
                    # self.__list_empty_location.append((r, c))
                    self.__list_empty_location.append(LocationModel(r, c))

    def is_game_over(self):
        if len(self.__list_empty_location) > 0:
            return False

        for r in range(len(self.map)):
            for c in range(len(self.map[r]) - 1):
                if self.map[r][c] == self.map[r][c + 1] and self.map[c][r] == self.map[c + 1][r]:
                    return False

        return True
        # for r in range(len(self.map)):
        #     for c in range(len(self.map[r])-1):
        #         if self.map[r][c] == self.map[r][c+1]:
        #             return False
        #
        # for c in range(len(self.map)):
        #     for r in range(len(self.map)-1):
        #         if self.map[r][c] == self.map[r+1][c]:
        #             return False


if __name__ == '__main__':
    controller = GameCoreController()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.move_down()
    print(controller.map)
