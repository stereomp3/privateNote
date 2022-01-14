"""
    建創員工管理器:
        1. 紀錄所有員工
        2. 計算總薪資
    崗位:
        1. 程序員: 底薪 + 項目分紅
        2. 測試員: 底薪 + Bug數 * 5
        ....
    要求:
        增加新員工，管理器代碼不變
    體會: 三大特徵，四大原則
"""


class StaffManager:
    def __init__(self):
        self.__staffs = []

    @property
    def staffs(self):
        return self.__staffs

    def add_stuff(self, employee):
        self.__staffs.append(employee)

    def calculate_money(self):
        total_money = 0
        for employee in self.__staffs:
            total_money += employee.get_money()
        return total_money


class Staff:
    def __init__(self, base_salary=0):
        self.base_salary = base_salary

    def get_money(self):
        return self.base_salary


class Programmer(Staff):
    def __init__(self, base_salary=0, project_dividend=0):
        super().__init__(base_salary)
        self.project_dividend = project_dividend

    def get_money(self):
        return super().get_money() + self.project_dividend


class Tester(Staff):
    def __init__(self, base_salary=0, number_of_bug=0):
        super().__init__(base_salary)
        self.number_of_bug = number_of_bug

    def get_money(self):
        return super().get_money() + self.number_of_bug * 5


manger = StaffManager()
manger.add_stuff(Programmer(30000, 20000))
manger.add_stuff(Tester(25000, 210))
print(manger.calculate_money())
