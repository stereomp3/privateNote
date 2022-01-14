"""
    for item in MyRange(5):
        print(item) # 0 1 2 3 4
"""


# 自己寫
# class RangeIterator:
#     def __init__(self, data):
#         self.data = data
#         self.num = -1
#
#     def __next__(self):
#         self.num += 1
#         if self.num > len(self.data) - 1:
#             raise StopIteration
#         return self.data[self.num]
#
#
# class MyRange:
#     def __init__(self, my_range):
#         self.my_range = my_range
#         self.__rang_list = []
#
#     def add_list(self):
#         num = 0
#         while num < self.my_range:
#             self.__rang_list.append(num)
#             num += 1
#
#     def __iter__(self):
#         MyRange.add_list(self)
#         return RangeIterator(self.__rang_list)
#
#
# for item in MyRange(6):
#     print(item)

# 自訂義迭代器
# class MyRangeIterator:
#     def __init__(self, stop):
#         self.__number = -1
#         self.__stop_value = stop
#
#     def __next__(self):
#         self.__number += 1
#         if self.__number >= self.__stop_value:
#             raise StopIteration()
#
#         return self.__number
#
#
# class MyRange:
#     def __init__(self, stop):
#         self.__stop = stop
#
#     def __iter__(self):
#         return MyRangeIterator(self.__stop)

# 使用函數yield
class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        number = 0
        while number < self.__stop:
            # yield 以前的代碼，放到在__next__方法中
            yield number  # 回傳number
            number += 1


# 循环一次 计算一次  返回一次，不會撐爆內存
for item in MyRange(5):
    print(item)  # 0 1 2 3 4
