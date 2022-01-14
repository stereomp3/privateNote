"""
    練習: 重寫運算符
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x的分量是%d, y的分量是%d" % (self.x, self.y)

    def __add__(self, other):  # 建創新對象
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Vector2(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Vector2(self.x % other.x, self.y % other.y)

    def __pow__(self, power, modulo=None):
        return Vector2(self.x ** power.x, self.y ** power.y)


pos = Vector2(1, 2)
dir = Vector2(1, 1)
print(pos + dir)  # (1, 2)+(1, 1) = (2, 3)
print(pos - dir)  # (1, 2)-(1, 1) = (0, 1)
print(pos * dir)  # (1, 2)*(1, 1) = (1, 2)
print(pos / dir)  # (1, 2)/(1, 1) = (1, 2)
print(pos // dir)  # (1, 2)//(1, 1) = (1, 2)
print(pos % dir)  # (1, 2)%(1, 1) = (0, 0)
print(pos ** dir)  # (1, 2)**(1, 1) = (1, 2)

