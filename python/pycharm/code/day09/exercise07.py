"""
    建創圖形管理器:
        1. 紀錄所有圖形
        2. 計算總面積
    圖形:
        1. 矩陣
        2. 圓形
        ....
    要求:
        增加新圖形，管理器代碼不變

    畫出設計圖
    寫出哪裡體現了四大原則
        開閉原則: 增加新圖形，管理器代碼不變。
        單一職責: Rectangle負責管理面積的算法，Cirle負責圓形面積的算法，
                GraphicManager負責統一管理圖形。
        依賴倒置: 圖形管理器沒有調用圓形、矩形算法，而是調用圖形類。
        組合復用: 圖形管理器與具體的各種圖形是組合關系
"""

# 自己寫
# class ImageManager:
#
#     def __init__(self):
#         self.__record_list = []
#
#     @property
#     def record_list(self):
#         return self.__record_list
#
#     def calculate_area(self, item):
#         self.__record_list.append(item.name)
#         return item.area()
#
#
# class Image:
#     def area(self):
#         pass
#
#
# class Matrix(Image):
#     def __init__(self, length01=0, length02=0):
#         self.length01 = length01
#         self.length02 = length02
#         self.name = "矩形"
#
#     def area(self):
#         return self.length01 * self.length02
#
#
# class Circle(Image):
#     def __init__(self, radius=0):
#         self.radius = radius
#         self.name = "圓形"
#
#     def area(self):
#         return self.radius ** 2 * 3.14
#
#
# ctr = ImageManager()
# m01 = Matrix(10, 20)
# c01 = Circle(10)
# print(ctr.calculate_area(m01))
# print(ctr.calculate_area(m01))
# for i in range(len(ctr.record_list)):
#     print(ctr.record_list[i])
class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def calculate_total_area(self):
        total_area = 0
        for item in self.__graphics:
            total_area += item.get_area()
        return total_area


class Graphic:
    def get_area(self):
        pass


# ------------------------
class Rectanlge(Graphic):
    def __init__(self, lenght=0, width=0):
        self.lenght = lenght
        self.width = width

    def get_area(self):
        return self.lenght * self.width


class Circle(Graphic):
    def __init__(self, radius=0):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2


manager = GraphicManager()
manager.add_graphic(Rectanlge(2, 6))
manager.add_graphic(Circle(5))
print(manager.calculate_total_area())
