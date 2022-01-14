"""
    請以面相對向的思想，描述以下場景:
        張無忌教趙敏九陽神功
        趙敏教張無忌化妝
        張無忌上班掙了10000元
        趙敏上班掙了8000元
"""

"""
 自己寫
class Person:
    def __init__(self, name=""):
        self.name = name

    def teach(self, teach):
        teach.teaching(self.name)

    def work(self, work):
        work.working(self.name)


class Work:
    def __init__(self, money=0):
        self.money = money

    def working(self, name):
        print(name + "上班賺了" + str(self.money))


class Teach:
    def __init__(self, thing="", t_ob=""):
        self.thing = thing
        self.t_ob = t_ob

    def teaching(self, name):
        print(name + "教" + self.t_ob + self.thing)


p01 = Person("張無忌")
p02 = Person("趙敏")
t01 = Teach("九陽神功", "趙敏")
t02 = Teach("化妝", "張無忌")
w01 = Work(10000)
w02 = Work(8000)

p01.teach(t01)
p02.teach(t02)
p01.work(w01)
p02.work(w02)
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def teach(self, other, skill):
        print(self.name + "教" + other.name + skill)

    def work(self, money):
        print(self.name + "上班賺了" + str(money))


p01 = Person("張無忌")
p02 = Person("趙敏")
p01.teach(p02, "九陽神功")
p02.teach(p01, "化妝")
p01.work(10000)
p02.work(8000)
