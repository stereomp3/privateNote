from bll import StudentManagerController
from model import StudentModel


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
        score = self.__input_interger("請輸入學生成績:")
        age = self.__input_interger("請輸入學生年齡:")
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
        stu.id = self.__input_interger("請輸入要修改的學生編號:")
        stu.name = input("請輸入學生姓名:")
        stu.score = self.__input_interger("請輸入學生成績:")
        stu.age = self.__input_interger("請輸入學生年齡:")
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失敗")

    @staticmethod
    def __input_interger(message):
        while True:
            try:
                return int(input(message))
            except:
                print("輸入有錯")

    def __output_student_order_by_score(self):
        self.__controller.order_by_score()
        self.__output_student()
        self.__controller.order_by_id()
