"""
    建創老婆類，老婆列表
    定義下列函數:
        1)獲取所有老婆姓名
        2)獲取顏值大於80的老婆對象
        3)獲取年齡最大的老婆對象
        4)根據顏值對老婆列表進行升序排列
"""


class Wife:
    def __init__(self, name="", face_score=0, age=0):
        self.name = name
        self.face_score = face_score
        self.age = age

    def print_self(self):
        print(self.name, self.age, self.face_score)


list_wife = [
    Wife("阿珂", 100, 23),
    Wife("蘇荃", 92, 32),
    Wife("雙兒", 90, 25),
    Wife("小郡主", 76, 22),
    Wife("方怡", 75, 27),
    Wife("建寧", 86, 25),
    Wife("曾柔", 67, 24),
]


def find01():
    list_wife_name = []
    for wife in list_wife:
        list_wife_name.append(wife.name)
    return list_wife_name


# print(find01())


def find02():
    face_score_wife = []
    for wife in list_wife:
        if 80 < wife.face_score:
            face_score_wife.append(wife)
    return face_score_wife


# for i in find02():
#     # print(i.__dict__)
#     print(i.print_self())


# def find03():
#     age_wife = [0, Wife()]
#     for wife in list_wife:
#         if age_wife[0] < wife.age:
#             age_wife[0] = wife.age
#             age_wife[1] = wife
#     return age_wife[1].__dict__
#
#
# # print(find03())

def get_max():
    max_value = list_wife[0]  # 先設一個值
    for i in range(1, len(list_wife)):
        if max_value.age < list_wife[i].age:
            max_value = list_wife[i]
    return max_value


# re = get_max()
# re.print_self()


def find04():
    for i in range(len(list_wife) - 1):
        for y in range(i + 1, len(list_wife)):
            if list_wife[i].face_score > list_wife[y].face_score:
                list_wife[i], list_wife[y] = list_wife[y], list_wife[i]
# find04()
# for wife in list_wife:
#     print(wife.__dict__)
