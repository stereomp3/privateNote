"""
    步驟一:
        數據模型類: StudentModel
            數據: 姓名 name, 年齡 age, 成績 score, 編號 id
        邏輯控制類: StudentManagerController
            數據: 學生列表 __stu_list
            行為: 獲取列表 stu_list
                 添加學生 add_student,
                 刪除學生 remove_student(stu_id)，
                 修改學生 update_student(new_stu)，
                 根據成績進行升序排列 order_by_score。
    步驟二:
        界面視圖類: StudentManageView
            行為: 顯示菜單 __display_menu，
                 選擇菜單項 __select_menu_item，入口邏輯main，
                 輸入學生 __input_student，
                 顯示學生信息 __output_student
                 刪除學生信息 __delete_student
                 修改學生信息 __modify_student
                 根據成績升序輸出學生 __output_student_order_by_score
"""

"""
自己寫
class StudentModel:
    def __init__(self, name="", age=0, score=0, s_id=None):
        self.name = name
        self.age = age
        self.score = score
        self.s_id = s_id


class StudentManagerController:
    stu_list = []

    def __init__(self, stu_list):
        self.stu_list = stu_list

    def get_list(self):
        return self.stu_list

    def add_student(self, stu):
        stu_dict = {"name": stu.name, "age": stu.age, "score": stu.score, "id": stu.s_id}
        StudentManagerController.stu_list.append(stu_dict)
        self.stu_list = StudentManagerController.stu_list
        
    def remove_student(self, stu):
        self.__stu_list.remove(stu)


class StudentManageView: Bug 無法刪除和修改
    def __init__(self):
        self.controller = StudentManagerController()

    def __diplay_menu(self):
        print("1) 添加學生信息")
        print("2) 顯示學生信息")
        print("3) 刪除學生信息")
        print("4) 修改學生信息")
        print("5) 根據成績升序排列")

    def __select_menu(self):
        item = input("請輸入選項:")
        if item == "1":
            name = input("輸入學生姓名:")
            age = input("輸入學生年齡:")
            score = input("輸入學生成績:")
            self.controller.add_student(StudentModel(name, age, score))
        elif item == "2":
            for item in self.controller.stu_list:
                print("學生id:" + str(item.id), "學生姓名:" + str(item.name), "學生年齡:"
                      + str(item.age), "學生成績" + str(item.score))
        elif item == "3":
            stu_id = input("請入要刪除的學生的id:")
            self.controller.remove_student(stu_id)
        elif item == "4":
            stu_id = input("請入要修改的學生的id:")
            name = input("輸入要修改的學生姓名:")
            age = input("輸入要修改的學生年齡:")
            score = input("輸入要修改的學生成績:")
            self.controller.update_student(StudentModel(name, age, score, stu_id))
        elif item == "5":
            self.controller.order_by_score()

    def main(self):
        while True:
            self.__diplay_menu()
            self.__select_menu()
            
            
stu01 = StudentModel("王曉明", 15, 60, 1)
stu02 = StudentModel("王大明", 16, 50, 2)
stu03 = StudentModel("王中明", 15, 70, 3)
SM1 = StudentManagerController([])
SM1.add_student(stu01)
SM1.add_student(stu02)
SM1.add_student(stu03)


a = SM1.get_list()
print(a)
"""


class StudentModel:
    """
        學生數據模型
    """

    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        學生管理控制器:住要負責業務邏輯處理
    """

    init_id = 1000

    @classmethod
    def __generate_id(cls, stu):
        stu.id = cls.init_id
        cls.init_id += 1  # 讓id自增長

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        """
            添加學生訊息
        :param stu: 需要添加的學生對象
        """
        StudentManagerController.__generate_id(stu)  # 加入學生id
        self.__stu_list.append(stu)

    def remove_student(self, stu_id):
        """
            移除學生信息
        :param stu_id: 需要移除的學生編號
        :return: 移除是否成功
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        return False  # 告知使用者沒有刪到任何人

    def update_student(self, new_stu):
        """
            修改學生信息(需要id)
        :param new_stu: 需要修改的學生
        :return: 是否修改成功
        """
        for item in self.__stu_list:
            if item.id == new_stu.id:
                item.name = new_stu.name
                item.age = new_stu.age
                item.score = new_stu.score
                return True
        return False

    def order_by_score(self):
        """
            根據成績升序排列
        """
        for i in range(len(self.__stu_list) - 1):
            for y in range(i + 1, len(self.__stu_list)):
                if self.__stu_list[i].score > self.__stu_list[y].score:
                    self.__stu_list[i], self.__stu_list[y] = self.__stu_list[y], self.__stu_list[i]

    def order_by_id(self):
        """
            根據序號升序排列
        """
        for i in range(len(self.__stu_list) - 1):
            for y in range(i + 1, len(self.__stu_list)):
                if self.__stu_list[i].id > self.__stu_list[y].id:
                    self.__stu_list[i], self.__stu_list[y] = self.__stu_list[y], self.__stu_list[i]


class StudentManageView:
    """
        學生管理視圖:住要負責介面邏輯處理
    """

    def __init__(self):
        self.__controller = StudentManagerController()

    def __diplay_menu(self):
        print("1) 添加學生信息")
        print("2) 顯示學生信息")
        print("3) 刪除學生信息")
        print("4) 修改學生信息")
        print("5) 根據成績升序排列")

    def __select_menu(self):
        item = input("請輸入選項:")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_student()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_order_by_score()

    def main(self):
        while True:
            self.__diplay_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("請輸入學生姓名:")
        score = int(input("請輸入學生成績:"))
        age = int(input("請輸入學生年齡:"))
        stu = StudentModel(name, age, score)
        self.__controller.add_student(stu)

    def __output_student(self):
        for item in self.__controller.stu_list:
            print("學生id:%d, 學生姓名:%s, 學生年齡:%d, 學生成績%d" %
                  (item.id, item.name, item.age, item.score))

    def __delete_student(self):
        stu_id = int(input("請輸入要刪除的學生編號:"))
        if self.__controller.remove_student(stu_id):
            print("刪除成功")
        else:
            print("刪除失敗")

    def __modify_student(self):
        # 這種寫法比上面的效能好一些，開闢的地較少
        stu = StudentModel()
        stu.id = int(input("請輸入要修改的學生編號:"))
        stu.name = input("請輸入學生姓名:")
        stu.score = int(input("請輸入學生成績:"))
        stu.age = int(input("請輸入學生年齡:"))

        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失敗")

    def __output_student_order_by_score(self):
        self.__controller.order_by_score()
        self.__output_student()
        self.__controller.order_by_id()


view = StudentManageView()
view.main()

# # 測試
# controller = StudentManagerController()
# data01 = StudentModel("悟空", 23, 96)
# controller.add_student(data01)
# controller.add_student(StudentModel("八戒", 25, 65))
# controller.update_student(StudentModel("123", 23, 96, 1000))
# # print(controller.remove_student(1001))
# controller.order_by_score()
# for item in controller.stu_list:
#     print(item.id, item.name)
