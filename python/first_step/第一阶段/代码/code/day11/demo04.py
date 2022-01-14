"""
    迭代器 --> yield
"""

class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        # 你看见的代码,不是这个样子.
        # 代码生成大致流程：
        # 1. 将yield以前的代码,定义在__next__方法中
        # 2. 将yield以后的数据,作为__next__方法的返回值
        # print("准备")
        # yield self.__skills[0]
        # print("准备")
        # yield self.__skills[1]
        # print("准备")
        # yield self.__skills[2]

        for item in self.__skills:
            print("准备")
            yield item


manager = SkillManager()
manager.add_skill("九阳神功")
manager.add_skill("乾大挪移")
manager.add_skill("太极坤")

for item in manager:
    print(item)

# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
