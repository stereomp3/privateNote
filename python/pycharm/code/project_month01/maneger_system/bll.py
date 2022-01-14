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



