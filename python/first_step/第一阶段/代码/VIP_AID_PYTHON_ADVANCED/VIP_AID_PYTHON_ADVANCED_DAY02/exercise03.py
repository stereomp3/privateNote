"""
    迭代员工管理器
"""

class EmployeeIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]

class EmployeeManager:
    def __init__(self):
        self.__employee = []

    def add_employee(self, skill):
        self.__employee.append(skill)

    def __iter__(self):
        return EmployeeIterator(self.__employee)

manager = EmployeeManager()
manager.add_employee("八戒")
manager.add_employee("悟空")
manager.add_employee("张无忌")

for item in manager:
    print(item)#