"""
    遊戲介面邏輯模塊
"""
import os  # 要在 linux 執行 才可以顯示

from bll import GameCoreController

"""class GameConsoleView: #自己寫
    
    # 控制台介面類
   
    def __init__(self):
        self.controller = GameCoreController()

    def main(self):
        self.init_map()
        while True:
            self.generate_map()
            self.get_player_input()
            if self.controller.is_game_over():
                print("Game Over")
                break

    def generate_map(self):
        for line in self.controller.map:
            print(line)

    def get_player_input(self):
        player_input = input("input wasd to play: ")
        if player_input == 'w':
            self.controller.move_up()
        if player_input == 'a':
            self.controller.move_left()
        if player_input == 's':
            self.controller.move_down()
        if player_input == 'd':
            self.controller.move_right()

        self.controller.generate_new_number()


    def init_map(self):
        self.controller.generate_new_number()
        self.controller.generate_new_number()"""


class GameConsoleView:
    """
        控制台界面类
    """

    def __init__(self):
        self.__controller = GameCoreController()

    def __start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__draw_map()

    def __update(self):
        while True:
            self.__move_map_for_input()
            self.__controller.generate_new_number()
            self.__draw_map()
            if self.__controller.is_game_over():
                print("GameOver")

    def __move_map_for_input(self):
        dir = input("WASD input direction:")
        if dir == "w":
            self.__controller.move_up()
        elif dir == "s":
            self.__controller.move_down()
        elif dir == "a":
            self.__controller.move_left()
        elif dir == "d":
            self.__controller.move_right()

    def main(self):
        self.__start()
        self.__update()

    def __draw_map(self):
        os.system("clear")  # 要在 linux 執行 才可以顯示
        for line in self.__controller.map:
            for item in line:
                print(item, end="\t")
            print()



