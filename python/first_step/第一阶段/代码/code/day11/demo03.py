"""
    迭代器
    目的：迭代自定义对象

"""


class SkillIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]


class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        return SkillIterator(self.__skills)


manager = SkillManager()
manager.add_skill("九阳神功")
manager.add_skill("乾大挪移")
manager.add_skill("太极坤")

# for item in manager:
#     print(item)#

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
