"""
    需求1：
        1. 在老婆列表中查找方怡对象
        2. 在老婆列表中查找颜值大于95的单个老婆对象
        first
    需求2：
        1. 计算老婆列表中姓名大于2个字的老婆数量
        2. 计算老婆列表年龄小于25的老婆数量
        get_count

    需求3：
        1. 获取老婆列表中所有老婆的姓名
        2. 获取老婆列表中所有老婆的姓名与颜值
        select

    需求4：
        1. 在老婆列表中判断是否存在姓名是苏荃的元素
        2. 在老婆列表中判断是否存在高度大于170的元素
        is_exists

    需求5：
        1. 累加老婆列表中所有人的年龄
        2. 累加老婆列表中所有人的高度
        sum

    需求7：
        1. 在老婆列表中找出颜值最高的老婆对象
        2. 在老婆列表中找出年龄最大的老婆对象
        get_max

    需求8：
        1. 在老婆列表中删除年龄小于25的所有老婆
        2. 在老婆列表中删除身高大于170的所有老婆
        delete_all

    需求9：
        1. 对老婆列表根据年龄进行升序排列
        2. 对老婆列表根据颜值进行升序排列
        order_by

    步骤：
        1. 根据需求，定义函数.
        2. 将变化点单独定义为函数.
        3. 将通用代码定义位函数(使用参数隔离变化点)
        4. 在IterableHelper类中添加新功能
        5. 在当前模块中进行测试
"""
from common.iterable_tools import IterableHelper


class Wife:
    def __init__(self, name="", face_score=0, age=0, height=0):
        self.name = name
        self.face_score = face_score
        self.age = age
        self.height = height

    def __str__(self):
        return "%s-%d-%d-%d"%(self.name,self.face_score,self.age,self.height)


list_wife = [
    Wife("双儿", 96, 22, 166),
    Wife("阿珂", 100, 23, 173),
    Wife("小郡主", 96, 22, 161),
    Wife("方怡", 86, 27, 166),
    Wife("苏荃", 99, 31, 176),
    Wife("建宁", 93, 24, 163),
    Wife("曾柔", 88, 26, 170),
]


# def condition01(item):
#     return item.face_score > 90


# for item in IterableHelper.find_all(list_wife,condition01):
#     print(item)

for item in IterableHelper.find_all(list_wife,lambda item:item.face_score > 90):
    print(item)

# 练习1：
# def first01():
#     for item in list_wife:
#         if item.name == "方怡":
#             return item
#
# def first02():
#     for item in list_wife:
#         if item.face_score > 95:
#             return item

# def condition01(item):
#     return item.name == "方怡"
#
# def condition02(item):
#     return item.face_score > 95

# def first(func):
#     for item in list_wife:
#         # if item.face_score > 95:
#         # if condition02(item):
#         if func(item):
#             return item

# print(IterableHelper.first(list_wife,condition02))
print(IterableHelper.first(list_wife,lambda item:item.face_score > 95))

# 练习2：
# def get_count01():
#     count = 0
#     for item in list_wife:
#         if len(item.name) > 2:
#             count += 1
#     return count
# def get_count02():
#     count = 0
#     for item in list_wife:
#         if item.age < 25:
#             count += 1
#     return count

# def condition01(item):
#     return len(item.name) > 2
#
# def condition02(item):
#     return item.age < 25

# def get_count(func):
#     count = 0
#     for item in list_wife:
#         # if item.age < 25:
#         # if condition02(item):
#         if func(item):
#             count += 1
#     return count

# print(IterableHelper.get_count(list_wife,condition02))
print(IterableHelper.get_count(list_wife,lambda item: item.age < 25))

# 练习3
# def select01():
#     for item in list_wife:
#         yield item.name
#
# def select02():
#     for item in list_wife:
#         yield (item.name,item.face_score)

def handle01(item):
    return item.name

def handle02(item):
    return (item.name,item.face_score)

# def select(func):
#     for item in list_wife:
#         # yield (item.name,item.face_score)
#         # yield handle02(item)
#         yield func(item)

for item in IterableHelper.select(list_wife,handle02):
    print(item)


# 练习4：

# def is_exists01():
#     for item in list_wife:
#         if item.name == "苏荃":
#             return True
#     return False
#
# def is_exists02():
#     for item in list_wife:
#         if item.height > 170:
#             return True
#     return False
#
# def condition01(item):
#     return item.name == "苏荃"
#
# def condition02(item):
#     return item.height > 170
#
# def is_exists(func):
#     for item in list_wife:
#         # if item.height > 170:
#         # if condition02(item):
#         if func(item):
#             return True
#     return False

print(IterableHelper.is_exists(list_wife,lambda item:item.height > 170))

# 练习5：
# def sum01():
#     sum_value = 0
#     for item in list_wife:
#         sum_value += item.age
#     return sum_value
#
# def sum02():
#     sum_value = 0
#     for item in list_wife:
#         sum_value += item.height
#     return sum_value
#
# def sum(func):
#     sum_value = 0
#     for item in list_wife:
#         # sum_value += item.height
#         sum_value += func(item)
#     return sum_value

print(IterableHelper.sum(list_wife,lambda item:item.height))

# 练习6：
print(IterableHelper.get_max(list_wife,lambda element:element.height))

# 练习7:
# print(IterableHelper.delete_all(list_wife,lambda e:e.age > 25))

# 练习8:
IterableHelper.order_by(list_wife,lambda e:e.age)
for item in list_wife:
    print(item)