"""
    創建敵人類, 數據 : 姓名, 血量(0--100), 攻擊力(1--50)
"""


class Enemy:
    def __init__(self, name="", blood=0, attack=0):
        self.name = name
        self.blood = blood
        self.attack = attack

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, value):
        if 1 <= value <= 100:
            self.__blood = value
        else:
            raise Exception("輸入錯誤血量")

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if 1 <= value <= 50:
            self.__attack = value
        else:
            raise Exception("輸入錯誤攻擊力")


e01 = Enemy("詩乃", 150, 2)

print(e01.__dict__)
