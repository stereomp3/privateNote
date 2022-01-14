"""
    请以面向对象的思想，描述以下场景：
        玩家(攻击力)攻击敌人,敌人(血量)受伤后还可能死亡。
"""


class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self, target):
        print("打你")
        target.damage(self.atk)


class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        print("呃！")
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        print("死亡喽")


p01 = Player(50)
e01 = Enemy(100)
p01.attack(e01)
p01.attack(e01)
