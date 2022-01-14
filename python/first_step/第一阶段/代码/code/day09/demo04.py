"""
    运算符重载(重写)
        自定义对象使用python运算符
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x的分量是%d,y的分量是%d" % (self.x, self.y)

    # +
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    # +=
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # <
    def __lt__(self, other):
        return self.x + self.y < other.x + other.y

    # ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


pos = Vector2(1, 2)
dir = Vector2(0, 1)
# print(pos + dir)  # pos.__add__(dir)

# pos.x += dir.x
# pos.y += dir.y
pos += dir
# print(pos)

"""
# 创建了新对象
list01 = [1]
print(id(list01))
list01 = list01 + [2]
print(id(list01))

# 累加(在原有对象基础上增加)
list02 = [1]
print(id(list02))
list02 += [2]
print(id(list02))
"""

list01 = [
    Vector2(1, 2),
    Vector2(7, 8),
    Vector2(5, 6),
    Vector2(3, 4)
]

# sorted升序：内部在循环调用每个元素的__lt__
for item in sorted(list01):  #
    print(item)

#in 的内部也在循环调用每个元素的__eq__方法
print(Vector2(1, 2) in list01)# ?

# list01.remove(Vector2(1, 2))
# list01.count(Vector2(1, 2))