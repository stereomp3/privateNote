"""
    練習一: 在老婆列表中，查找顏值大於90的所有老婆
    練習二: 在老婆列表中，查找身高小於170的所有老婆
"""


class Wife:
    def __init__(self, name="", face_score=0, age=0, height=0):
        self.name = name
        self.face_score = face_score
        self.age = age
        self.height = height


list_wife = [
    Wife("雙兒", 96, 22, 166),
    Wife("阿珂", 100, 23, 173),
    Wife("小郡主", 96, 22, 161),
    Wife("方怡", 86, 27, 166),
    Wife("蘇荃", 99, 31, 176),
    Wife("建宇", 93, 24, 163),
    Wife("曾柔", 88, 26, 170),
]


def find(func):
    for item in list_wife:
        if func(item):
            yield item


def condition01(item):
    return item.face_score > 90


def condition02(item):
    return item.height < 170


for i in find(condition01):
    print(i.name)
    print(i.face_score)

for i in find(condition02):
    print(i.name)
    print(i.height)