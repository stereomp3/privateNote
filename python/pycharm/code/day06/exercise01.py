"""
    創建狗類
    數據成員包含:品種、愛稱、年齡、性別。
    方法成員包含:吃
    創建兩個對象並調用方法

    定義函數，在狗列表中查找所有拉不拉多
"""


class Dog:
    """
        狗
    """

    def __init__(self, breed="", name="", age=0, sex=""):
        self.breed = breed
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print(self.name + "吃飯")


dog01 = Dog("拉不拉多", "小白", 10, "女")
dog02 = Dog("拉不拉多", "小黑", 18, "男")
dog01.eat()
dog02.eat()

list01 = [
    dog01,
    dog02,
    Dog("沙皮", "毛毛", 3, "公"),
    Dog("金毛", "皮皮", 1, "母"),
]


def find_dog():
    list_result = []
    for dog in list01:
        if dog.breed == "拉不拉多":
            list_result.append(dog)
    return list_result


re = find_dog()
for item in re:
    print(item.name)
