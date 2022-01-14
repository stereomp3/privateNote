class StudentManagerController:
    """
        学生管理控制器:主要负责业务逻辑处理
    """
    init_id = 1000

    @classmethod
    def __generate_id(cls, stu):
        stu.id = cls.init_id
        cls.init_id += 1

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        """
            添加学生信息
        :param stu: 需要添加的学生对象
        """
        StudentManagerController.__generate_id(stu)
        self.__stu_list.append(stu)

    def remove_student(self, stu_id):
        """
            移除学生信息
        :param stu_id:需要移除的学生编号
        :return:移除是否成功
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self, new_stu):
        """
            修改学生信息
        :param new_stu:需要修改的学生信息
        :return:是否修改成功
        """
        for item in self.__stu_list:
            if item.id == new_stu.id:
                item.name = new_stu.name
                item.atk = new_stu.atk
                item.score = new_stu.score
                return True
        return False

    def order_by_score(self):
        """
            根据成绩升序排列
        :return:
        """

        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]