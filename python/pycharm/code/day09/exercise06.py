"""
    手雷爆炸，傷害玩家(扣血，碎屏)和敵人(扣血，頭頂爆字)。
    變化點:鴨子，房子....
    寫出體現三大特徵的代碼:
        封裝: 根據需求分解出手雷類，玩家類，敵人類
        繼承: 使用攻擊目標隔離了手雷與玩家，敵人
        多態: 手雷調用攻擊目標，在玩家和敵人對象中體現了不同效果
                玩家和敵人分別重寫了攻擊目標的受傷方法
"""


class Grenade:
    def __init__(self, atk):
        self.atk = atk

    def explode(self, target):
        target.damage()
        print("爆炸了,造成" + str(self.atk) + "傷害")


class AttackTarget:

    def damage(self):
        print("扣血")


class Player(AttackTarget):
    def damage(self):
        super().damage()
        print("碎屏")


class Enemy(AttackTarget):
    def damage(self):
        super().damage()
        print("頭頂爆字")


w01 = Grenade(10)
p01 = Player()
e01 = Enemy()
w01.explode(e01)
