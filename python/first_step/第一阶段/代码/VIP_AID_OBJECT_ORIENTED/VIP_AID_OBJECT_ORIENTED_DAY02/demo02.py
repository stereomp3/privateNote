"""
    实例成员
        实例变量：
            对象.名称
"""


# class Wife:
#     def __init__(self, name="", face_score=0, age=0):
#         self.name = name
#         self.face_score = face_score
#         self.age = age
#
#     def play(self):
#         print(self.name, "玩耍")
#
#
# ak = Wife("阿珂", 100, 23)
# sq = Wife("苏荃", 92, 32)
# ak.play()  # 通过对象地址调用实例方法
# sq.play()

# 不建议
# class Wife:
#     pass
#
#
# ak = Wife()
# # 创建实例变量
# ak.name = "阿珂"
# # 读取实例变量
# print(ak.name)

# 不建议
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.fun01(age)

    def fun01(self, age=0):
        self.age = age

ak = Wife("阿珂", 23)
print(ak.name)
print(ak.age)

# 对象具有的实例变量
print(ak.__dict__)


