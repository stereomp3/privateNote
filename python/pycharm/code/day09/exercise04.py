"""
    練習: 重寫複合運算符
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x的分量是%d, y的分量是%d" % (self.x, self.y)

    def __iadd__(self, other):  # 不是建創新對象，是返回自身
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __itruediv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def __ifloordiv__(self, other):
        self.x //= other.x
        self.y //= other.y
        return self

    def __imod__(self, other):
        self.x %= other.x
        self.y %= other.y
        return self

    def __ipow__(self, power, modulo=None):
        self.x **= power.x
        self.y **= power.y
        return self


pos = Vector2(1, 2)
dir = Vector2(1, 1)
pos += dir
print(pos)  # (1, 2)+(1, 1) = (2, 3)
pos -= dir
print(pos)  # (2, 3)-(1, 1) = (1, 2)
pos *= dir
print(pos)  # (1, 2)*(1, 1) = (1, 2)
pos /= dir
print(pos)  # (1, 2)/(1, 1) = (1, 2)
pos //= dir
print(pos)  # (1, 2)//(1, 1) = (1, 2)
pos %= dir
print(pos)  # (1, 2)%(1, 1) = (0, 0)
pos **= dir
print(pos)  # (0, 0)**(1, 1) = (0, 0)
