"""
    練習: 對象計數器
        使用類變量紀錄
        使用類方法打印
"""


class Wife:
    count = 0

    @classmethod
    def counter(cls):
        print("Wife()出現" + str(Wife.count) + "次")

    def __init__(self, name="", face_score=0, age=0):
        self.name = name
        self.face_score = face_score
        self.age = age
        Wife.count += 1


w01 = Wife()
w02 = Wife()
w03 = Wife()
w04 = Wife()
w05 = Wife()

Wife.counter()
