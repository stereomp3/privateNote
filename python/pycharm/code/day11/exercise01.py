"""
    建創敵人類，限制攻擊力在 1--100之間

"""


class AtkError(Exception):
    def __init__(self, name="", error_id=0, error_code=""):
        self.name = name
        self.error_id = error_id
        self.error_code = error_code


class Enemy:

    def __init__(self, atk=0):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 1 <= value <= 100:
            self.__atk = value
        else:
            raise AtkError("攻擊力超出範圍", 1234, "if 1 <= value <= 100:")


try:
    e01 = Enemy(1000)
except AtkError as e:
    print(e.name)
    print(e.error_id)
    print(e.error_code)
