"""
    风清扬使用独孤九剑攻击
    任我行使用吸星大法攻击
    令狐冲即使用独孤九剑有使用吸星大法攻击
    ...
    可能还有很多人,很多技能。
"""


class Person:
    def __init__(self, name=""):
        self.name = name
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def release_skill(self):
        print(self.name, "释放技能")
        for item in self.__skills:
            item.attack()


class Skill:
    def attack(self):
        pass


class DuGuJiuJian(Skill):

    def attack(self):
        super().attack()
        print("独孤九剑攻击")


class XiXinDaFa(Skill):

    def attack(self):
        super().attack()
        print("吸心大法攻击")


fqy = Person("风清扬")
fqy.add_skill(DuGuJiuJian())
fqy.release_skill()

lhc = Person("令狐冲")
lhc.add_skill(DuGuJiuJian())
lhc.add_skill(XiXinDaFa())
lhc.release_skill()
