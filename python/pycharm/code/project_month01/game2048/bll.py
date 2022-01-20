"""
    遊戲核心邏輯控制器
"""
import random

from model import LocationModel


class GameCoreController:
    def __init__(self):
        self.__list_merge = None  # [2, 2, 2, 2] 不寫沒關係，因為是讀取map裡面的
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty_location = []

    @property  # 不讓別人修改值
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移到列尾
            思路:從後向前一次判斷，如果是零元素則刪除後追加0
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            兩個元素相同就相加，刪掉元素再追加0
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移動
            思路:將每行(一維列表)賦值給全局變量list_merge
                    在通過merge函數操作數據
        """
        for line in self.map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向右移動
            思路:將每行(反向切片)賦值給全局變量list_merge
                    在通過merge函數操作數據
                    再對list_merge(反向切片)
        """
        for line in self.map:
            # 因為切片，所以創建了新列表
            self.__list_merge = line[::-1]
            self.__merge()  # 操作的是新列表
            line[::-1] = self.__list_merge  # 賦值時反者放，不創建新列表

    def __square_matrix_transpose(self):
        for i in range(len(self.map) - 1):
            for y in range(i + 1, len(self.map)):
                self.map[i][y], self.map[y][i] = self.map[y][i], self.map[i][y]

    def move_up(self):
        """
            向上移動
            思想:方陣轉置
                調用向左移動
                方陣轉置
        """
        self.__square_matrix_transpose()
        self.move_left()
        self.__square_matrix_transpose()

    def move_down(self):
        """
            向下移動
            思想:方陣轉置
                調用向右移動
                方陣轉置
        """
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    """ 自己寫
    def generate_position(self):
        pos_list = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 0:
                    pos_list.append((i, j))
        if len(pos_list) == 0:
            print("game over")
            return 0
        pos = random.randrange(0, len(pos_list), 1)
        x = pos_list[pos][0]
        y = pos_list[pos][1]
        self.map[x][y] = self.__generate_number()
        print(self.map)

    @staticmethod
    def __generate_number():
        number = random.randrange(0, 10, 1)
        if number == 0:
            return 4
        else:
            return 2
            
    def is_game_over(self):
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.map[r][c] == 0:
                    return 0

        for r in range(len(self.map)):
            for c in range(len(self.map[r]) - 1):
                if self.map[r][c] == self.map[r][c + 1]:
                    return 0

        self.__square_matrix_transpose()
        for r in range(len(self.map)):
            for c in range(len(self.map[r]) - 1):
                if self.map[r][c] == self.map[r][c + 1]:
                    return 0
        self.__square_matrix_transpose()"""

    def generate_new_number(self):
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)  # 可以直接從裡面選擇一個
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

        # 橫豎同時判斷
        for r in range(len(self.map)):
            for c in range(len(self.map[r]) - 1):
                if self.map[r][c] == self.map[r][c + 1] and self.map[c][r] == self.map[c + 1][r]:
                    return False

        return True
        # for r in range(len(self.map)):  # 橫
        #     for c in range(len(self.map[r])-1):
        #         if self.map[r][c] == self.map[r][c+1]:
        #             return False
        #
        # for c in range(len(self.map)):  # 豎
        #     for r in range(len(self.map)-1):
        #         if self.map[r][c] == self.map[r+1][c]:
        #             return False


if __name__ == '__main__':
    controller = GameCoreController()
