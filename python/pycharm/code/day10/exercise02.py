"""
    風清揚使用獨孤九劍攻擊
    任我行使用吸星大法攻擊
    令狐沖使用獨孤九劍及吸星大法攻擊
    ...
    可能還有很多人，很多技能。
"""

# 自己寫
# class PersonManager:
#     def __init__(self):
#         self.__persons = []
#
#     @property
#     def persons(self):
#         return self.__persons
#
#     def add_person(self, person):
#         self.__persons.append(person)
#
#     def person_attack(self):
#         for person in self.__persons:
#             person.use_skill()
#
#
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#
#     def use_skill(self, skill):
#         print(self.name + "使用" + skill.name + "攻擊")
#
#
# class Skill:
#     def __init__(self, name=""):
#         self.name = name
#
#
# manager = PersonManager()
# s01 = Skill("獨孤九劍")
# s02 = Skill("吸星大法")
# p01 = Person("風清揚")
# p02 = Person("任我行")
# p03 = Person("令狐沖")
# p01.use_skill(s01)
# p02.use_skill(s02)


class Person:
    def __init__(self, name=""):
        self.name = name
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def release_skill(self):
        print(self.name, "釋放技能")
        for item in self.__skills:
            item.attack()


class Skill:
    def attack(self):
        pass


class DuGuJiuJian(Skill):

    def attack(self):
        super().attack()
        print("獨孤九劍攻击")


class XiXinDaFa(Skill):

    def attack(self):
        super().attack()
        print("吸星大法攻击")


fqy = Person("風清揚")
fqy.add_skill(DuGuJiuJian())
fqy.release_skill()

lhc = Person("令狐沖")
lhc.add_skill(DuGuJiuJian())
lhc.add_skill(XiXinDaFa())
lhc.release_skill()

