"""
    練習: 重寫比較運算符
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x的分量是%d, y的分量是%d" % (self.x, self.y)

    # <
    def __lt__(self, other):
        return self.x + self.y < other.x + other.y

    # <=
    def __le__(self, other):
        pass

    # >
    def __gt__(self, other):
        pass

    # ==   常用!
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # !=
    def __ne__(self, other):
        pass


list01 = [
    Vector2(1, 2),
    Vector2(7, 8),
    Vector2(5, 6),
    Vector2(3, 4),
]

# sort(list)可以幫物件進行升序排序，內部再循環調用每個元素的__lt__方法  # <
for item in sorted(list01):
    print(item)

# in 的內部也在循環調用每個元素的__eq__方法，預設是比較地址  # ==
print(Vector2(1, 2) in list01)  # ?
