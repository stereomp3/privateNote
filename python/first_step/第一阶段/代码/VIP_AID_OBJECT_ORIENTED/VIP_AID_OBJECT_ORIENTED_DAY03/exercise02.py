"""
    请以面向对象的思想，描述以下场景：
        张无忌教赵敏九阳神功
        赵敏教张无忌化妆
        张无忌上班挣了10000元
        赵敏上班挣了8000元
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def teach(self,other,skill):
        print(self.name,"教",other.name,skill)

    def work(self,money):
        print(self.name,"工作挣了",money,"元")


zwj = Person("张无忌")
zm = Person("赵敏")
zwj.teach(zm,"九阳神功")
zm.teach(zwj,"化妆")
zwj.work(10000)
zm.work(8000)