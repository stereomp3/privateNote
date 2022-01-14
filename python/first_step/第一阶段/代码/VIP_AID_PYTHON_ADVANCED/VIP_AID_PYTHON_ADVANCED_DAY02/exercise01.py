"""
    创建敌人类,限制攻击力在1--100之间

"""
class AtkRangeError(Exception):
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
            # 多个错误信息(错误名称,错误编号,错误代码...)
            # raise AtkRangeError("年龄超过范围错误", 1324, "1 <= value <= 100")
            raise Exception("年龄超过范围错误", 1324, "1 <= value <= 100")

try:
    mieba = Enemy(400)
# except AtkRangeError as e:
#     print(e.name)
#     print(e.error_id)
#     print(e.error_code)
except Exception as e:
    print(e.args)