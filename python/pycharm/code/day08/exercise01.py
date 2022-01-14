"""
    請以面相對象的思想，描述以下場景
        玩家(攻擊力)攻擊敵人，敵人(血量)受傷後還可能死亡
"""

"""
 自己寫
class Player:
    def __init__(self, atk=0):
        self.atk = atk


class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def hurt(self, atk):
        if self.hp > atk:
            self.hp -= atk
            print("敵人還剩"+str(self.hp)+"血量")
        else:
            print("敵人死亡")


P1 = Player(5)
E1 = Enemy(10)
E1.hurt(P1.atk)
E1.hurt(P1.atk)
"""


class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self, targe):
        print("玩家:喝")
        targe.damage(self.atk)


class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("敵人:阿")
        if self.hp <= 0:
            self.death()

    @staticmethod
    def death():
        print("敵人死亡")


p01 = Player(50)
e01 = Enemy(100)
p01.attack(e01)
p01.attack(e01)
