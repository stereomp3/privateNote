"""
    定義函數，正確返回成績(0 -- 100)
"""


def get_score():
    while True:
        try:
            in_score = int(input("請輸入成績:"))

        except:
            print("輸入的不是整數")
            continue

        if in_score < 0 or in_score > 100:
            print("請輸入範圍內的值")
        else:
            return in_score


score = get_score()
print(score)
