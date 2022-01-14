"""
    將下列代碼加入函數中，打印矩形
        for r in range(3):
            for c in range(5):
                print("*", end=" ")
            print()
"""


def rectangle(row, column, char):
    for r in range(row):
        for c in range(column):
            print(char, end=" ")
        print()


rectangle(5, 5, "#")
