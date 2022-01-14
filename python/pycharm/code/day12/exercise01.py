"""
    需求1:
        1. 在老婆列表中查找方怡對象
        2. 在老婆列表中查找顏值大於95的單個老婆對象
        first

    需求2:
        1. 計算老婆列表中姓名大於2個字的老婆數量
        2. 計算老婆列表中年齡小於25的老婆數量
        get_count


    需求3:
        1. 獲取老婆列表中所有老婆姓名
        2. 獲取老婆列表中所有老婆姓名和顏值
        select

    需求4:
        1. 在老婆列表中判斷是否存在姓名是蘇荃的元素
        2. 在老婆列表中判斷是否存在高度大於170的元素
        is_exists

    需求5:
        1. 累加老婆列表中所有人的年齡
        2. 累加老婆列表中所有人的高度
        sum

    需求6:
        1. 在老婆列表中找出顏值最高的老婆對象
        2. 在老婆列表中找出年齡最大的老婆對象
        get_max


    需求7:
        1. 在老婆列表中刪除年齡小于25的所有老婆對象
        2. 在老婆列表中刪除身高大於170的所有老婆對象
        delete_all

    需求8:
        1. 對老婆列表根據年齡進行升序排列
        2. 對老婆列表根據顏直進行升序排列
        order_by



    步驟:
        1. 根據需求，定義函數。
        2. 將變化點單獨定義為函數。
        3. 將通用代碼定義為函數(使用參數隔離變化點)
        4. 在IterableHelper類中添加新功能
        5. 在當前模塊中進行測試
"""
from common.iterable_tools import IterableHelper


class Wife:
    def __init__(self, name="", face_score=0, age=0, height=0):
        self.name = name
        self.face_score = face_score
        self.age = age
        self.height = height

    def __str__(self):
        return "%s-顏值%d-%d歲-身高%d公分" % (self.name, self.face_score, self.age, self.height)


list_wife = [
    Wife("雙兒", 96, 22, 166),
    Wife("阿珂", 100, 23, 173),
    Wife("小郡主", 96, 22, 161),
    Wife("方怡", 86, 27, 166),
    Wife("蘇荃", 99, 31, 176),
    Wife("建宇", 93, 24, 163),
    Wife("曾柔", 88, 26, 170),
]

print(IterableHelper.first(list_wife, lambda item: item.face_score > 95))
# 練習一:
# def condition01(item):
#     return item.face_score > 90
#
#
# def first01():
#     for item in list_wife:
#         if item.name == "方怡":
#             return item
#
#
# def first02():
#     for item in list_wife:
#         if item.age > 95:
#             return item
#
#
# def condition01(item):
#     return item.name == "方怡"
#
#
# def condition02(item):
#     return item.face_score > 95
#
# print(IterableHelper.first(list_wife, get_count01))


print(IterableHelper.get_count(list_wife, lambda item: item.age < 25))
# 練習二:
# def get_count01():
#     for item in list_wife:
#         if len(item.name) > 2:
#             yield item
#
#
# def get_count02():
#     for item in list_wife:
#         if item.age < 25:
#             yield item
#
# def get_count(func):
#     count = 0
#     for item in list_wife:
#         if func(item):
#             count += 1
#     return count
#
#
# def condition01(item):
#     return len(item.name) > 2
#
#
# def condition02(item):
#     return item.age < 25


for i in IterableHelper.select(list_wife, lambda item: (item.name, item.face_score)):
    print(i)

# 練習三
# def select01():
#     for item in list_wife:
#         yield item.name
#
#
# def select02():
#     for item in list_wife:
#         yield item.name
#
#
# def select(func):
#     for item in list_wife:
#         func(item)
#
#
# def handle01(item):
#     return item.name
#
#
# def handle02(item):
#     return item.name, item.face_score

# 練習4
print(IterableHelper.is_exists(list_wife, lambda item: item.name == "蘇荃"))
print(IterableHelper.is_exists(list_wife, lambda item: item.height > 170))

# 練習5
print(IterableHelper.sum(list_wife, lambda item: item.age))
print(IterableHelper.sum(list_wife, lambda item: item.height))

# 練習6
print(IterableHelper.get_max(list_wife, lambda item: item.face_score))
print(IterableHelper.get_max(list_wife, lambda item: item.age))
print("//////////////")
# 練習7
# IterableHelper.delete_all(list_wife, lambda item: item.age < 25)
# for item in list_wife:
#     print(item)
# IterableHelper.delete_all(list_wife, lambda item: item.height >= 170)
# for item in list_wife:
#     print(item)

# 練習8
#
# IterableHelper.order_by(list_wife, lambda item: item.age)
# for item in list_wife:
#     print(item)

