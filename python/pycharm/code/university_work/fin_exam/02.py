import sys


class StudentModel:
    """
        學生數據模型
    """

    def __init__(self, name="", phone="0981666000", score=0, subject=0, id=0):
        self.name = name
        self.phone = phone
        self.score = score
        self.subject = subject
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
        self.__class = SubjectManager()

    @property
    def stu_list(self):
        return self.__stu_list

    @property
    def sub_data(self):
        return self.__class

    def add_student(self, stu, sub):
        """
            添加學生訊息
        :param stu: 需要添加的學生對象
        :param sub: 需要添加的科目
        """
        StudentManagerController.__generate_id(stu)  # 加入學生id
        self.__class.add_subject_list(sub, stu)  # 加入學生到dict裡面

    def add_base_stu(self, sub):
        """
            添加基本學生訊息
        :param sub: 需要添加的科目
        """
        std_name = ["魏零一", "魏零二", "魏零三", "魏零四",
                    "魏仲彥"]
        std_score = [86, 87, 80, 89, 100]
        std_phone = ["0911111111", "0922222222", "0933333333", "0944444444", "0988844411"]

        for stu in self.__class.subject_dict[sub]:
            for s in std_name:
                if stu.name == s:
                    return True

        for i in range(len(std_name)):
            self.add_student(StudentModel(std_name[i], std_phone[i], std_score[i]), sub)

    def remove_student(self, stu_id, sub):
        """
            移除學生信息
        :param stu_id: 需要移除的學生編號
        :param sub: 需要添加的科目
        :return: 移除是否成功
        """
        for item in self.__class.subject_dict[sub]:
            if item.id == stu_id:
                self.__class.subject_dict[sub].remove(item)
                return True
        return False  # 告知使用者沒有刪到任何人

    def update_student(self, new_stu, sub):
        """
            修改學生信息(需要id)
        :param new_stu: 需要修改的學生
        :param sub: 需要添加的科目
        :return: 是否修改成功
        """
        for item in self.__class.subject_dict[sub]:
            if item.id == new_stu.id:
                item.name = new_stu.name
                item.score = new_stu.score
                return True
        return False

    def order_by_score(self, sub):
        """
            根據成績升序排列
            :param sub: 需要添加的科目
        """
        for i in range(len(self.__class.subject_dict[sub]) - 1):
            for y in range(i + 1, len(self.__class.subject_dict[sub])):
                if self.__class.subject_dict[sub][i].score > self.__class.subject_dict[sub][y].score:
                    self.__class.subject_dict[sub][i], self.__class.subject_dict[sub][y] = \
                        self.__class.subject_dict[sub][y], self.__class.subject_dict[sub][i]

    def order_by_id(self, sub):
        """
            根據序號升序排列
            :param sub: 需要添加的科目
        """
        for i in range(len(self.__class.subject_dict[sub]) - 1):
            for y in range(i + 1, len(self.__class.subject_dict[sub])):
                if self.__class.subject_dict[sub][i].id > self.__class.subject_dict[sub][y].id:
                    self.__class.subject_dict[sub][i], self.__class.subject_dict[sub][y] = \
                        self.__class.subject_dict[sub][y], self.__class.subject_dict[sub][i]

    def clear_stu_data(self):
        self.__stu_list = []

    def query_score(self, std_nam):
        """
            用名字查詢科目成績
        :return: 字典，{科目:分數}
        """
        flag = False
        q_dict = {}
        for k, v in self.__class.subject_dict.items():
            for s in v:
                if std_nam == s.name:
                    q_dict[k] = s.score
                    flag = True
        if flag:
            return q_dict
        else:
            return False  # 查無此人


class StudentManageView:
    """
        學生管理視圖:住要負責介面邏輯處理
    """

    def __init__(self):
        self.__controller = StudentManagerController()

    def __diplay_menu(self):
        print()
        print("1) 添加預設學生(5人)")
        print("2) 添加學生信息")
        print("3) 顯示學生信息")
        print("4) 刪除學生信息")
        print("5) 修改學生信息")
        print("6) 根據成績升序排列")
        print("7) 查詢學生各科成績")
        print("8) 回到選擇科目")

    def __select_menu(self, sub):
        item = input("輸入操作選項:")
        if item == "1":
            if (self.__controller.add_base_stu(sub)):
                print("以添加過預設學生")
            return False
        if item == "2":
            self.__input_student(sub)
            return False
        elif item == "3":
            self.__output_student(sub)
            return False
        elif item == "4":
            self.__delete_student(sub)
            return False
        elif item == "5":
            self.__modify_student(sub)
            return False
        elif item == "6":
            self.__output_student_order_by_score(sub)
            return False
        elif item == "7":
            self.query_stu_score()
            return False
        elif item == "8":
            self.__controller.clear_stu_data()
            return True
        else:
            print("輸入錯誤")
            return False

    def main(self):
        while True:
            self.__diplay_subject()
            sub_name = self.__select_subject()
            if sub_name:  # True --> != 0  False == 0
                print("\n進入 " + sub_name + "\n")
                while True:
                    self.__diplay_menu()
                    if self.__select_menu(sub_name):
                        break

    def __input_student(self, sub):
        name = input("請輸入學生姓名:")
        score = int(input("請輸入學生成績:"))
        phone = input("請輸入學生電話")
        stu = StudentModel(name, phone, score)
        self.__controller.add_student(stu, sub)

    def __output_student(self, sub):
        sdu_dict = self.__controller.sub_data.subject_dict
        for item in sdu_dict[sub]:
            print("學生id:%d, 學生姓名:%s, 學生電話: %s, 學生成績%d" %
                  (item.id, item.name, item.phone, item.score))

    def __delete_student(self, sub):
        stu_id = int(input("請輸入要刪除的學生編號:"))
        if self.__controller.remove_student(stu_id, sub):
            print("刪除成功")
        else:
            print("刪除失敗")

    def __modify_student(self, sub):
        stu = StudentModel()
        stu.id = int(input("請輸入要修改的學生編號:"))
        stu.name = input("請輸入學生姓名:")
        stu.score = int(input("請輸入學生成績:"))

        if self.__controller.update_student(stu, sub):
            print("修改成功")
        else:
            print("修改失敗")

    def __output_student_order_by_score(self, sub):
        self.__controller.order_by_score(sub)
        self.__output_student(sub)
        self.__controller.order_by_id(sub)

    def query_stu_score(self):
        name = input("輸入要查詢對象的姓名: ")
        query_dict = self.__controller.query_score(name)
        sum = 0
        if not query_dict:
            print("查無此人")
            return 0
        for k, v in query_dict.items():
            sum += v
            print("科目: '" + str(k) + "' 的分數是: " + str(v))
        print("個人總分: " + str(sum))
        print("平均分數: " + str(sum / len(query_dict)))

    # 下面是選擇科目
    def __diplay_subject(self):
        print()
        print("1) 資料結構")
        print("2) 程式設計")
        print("3) 計算機概論")
        print("4) 顯示各科平均")
        print("5) 離開")

    def __select_subject(self):
        item = input("請輸入要進行操作的科目:")
        if item == "1":
            return "資料結構"
        elif item == "2":
            return "程式設計"
        elif item == "3":
            return "計算機概論"
        elif item == "4":
            self.show_all_class_score()
        elif item == "5":
            sys.exit(0)
        else:
            print("輸入錯誤")
            return False

    def show_all_class_score(self):
        average = self.__controller.sub_data.show_all_average()
        print()
        for k, v in average.items():
            print(str(k) + " 平均分數是: " + str(v))
        print()


class SubjectManager:
    def __init__(self):
        self.__subject_dict = {
            "資料結構": [],
            "程式設計": [],
            "計算機概論": [],
        }

    @property
    def subject_dict(self):
        return self.__subject_dict

    def add_subject_list(self, sub_nam, stu):
        self.__subject_dict[sub_nam].append(stu)

    def show_all_average(self):
        query_dict = {}
        sum_num = 0
        for k, v in self.__subject_dict.items():
            for s in v:
                sum_num += s.score
            query_dict[k] = sum_num / (len(self.__subject_dict[k]) + 1)
            sum_num = 0
        return query_dict


view = StudentManageView()
view.main()
