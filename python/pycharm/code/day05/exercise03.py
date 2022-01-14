"""
    定義函數，根據成績，判斷等級
"""


def grade_detect(grade):
    if grade < 0 or grade > 100: return "成績輸入錯誤"
    if grade >= 90:
        return "成績頂尖"
    if grade >= 80:
        return "成績優秀"
    if grade >= 60:
        return "成績及格"
    return "成績不及格"


print(grade_detect(float(input("請輸入成績:"))))
