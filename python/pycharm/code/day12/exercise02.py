"""
    使用內置高級函數實現下列功能:

    1. 在敵人列表中查找所有敵人名稱與攻擊力
    2. 在敵人列表中查找血量大於500的所有敵人
    3. 對敵人列表進行降序排列
    4. 找出列表[(1,),(2,2,2),(3.3)]中長度最大的元素
    5. 根據value對字典進行升序排列{"張無忌":306, "趙敏":305, "小昭":102}
"""


class Enemy:
    def __init__(self, name="", hp=0, atk=0, shell=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.shell = shell

    def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.hp, self.atk, self.shell)


list_enemy = [
    Enemy("滅霸", 999, 555, 333),
    Enemy("成坤", 360, 100, 50),
    Enemy("玄冥二老", 300, 90, 70),
    Enemy("白骨精", 600, 200, 60),
]

for i in map(lambda item: (item.name, item.atk), list_enemy):
    print(i)

for i in filter(lambda item: item.hp > 500, list_enemy):
    print(i)

print("//////////////")
for i in sorted(list_enemy, key=lambda item: item.hp, reverse=False):
    print(i)

list01 = [(1,), (2, 2, 2), (3.3,)]
print(max(list01, key=lambda item: len(item)))
# 自己寫
# list02 = []
# for item in list01:
#     list02.append(len(item))
# print(max(list02))


dict01 = {"張無忌": 306, "趙敏": 305, "小昭": 102}
# 自己寫
# for i in sorted(dict01, key=lambda item: item):
#     print(i)
for i in sorted(dict01.items(), key=lambda item: item[1]):
    print(i)
