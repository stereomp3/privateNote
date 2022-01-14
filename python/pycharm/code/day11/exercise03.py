"""
    迭代員工管理器
"""


class StaffIterator:

    def __init__(self, data):
        self.data = data
        self.num = -1

    def __next__(self):
        self.num += 1
        if self.num > len(self.data) - 1:
            raise StopIteration
        return self.data[self.num]


class StaffManager:
    def __init__(self):
        self.__staff_list = []

    @property
    def staff_list(self):
        return self.__staff_list

    def add_staff(self, name):
        self.__staff_list.append(name)

    def __iter__(self):
        return StaffIterator(self.__staff_list)


manager = StaffManager()
manager.add_staff("魏仲彥")
manager.add_staff("詩乃")
manager.add_staff("雅斯娜")
# for i in manager:
#     print(i)


iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
