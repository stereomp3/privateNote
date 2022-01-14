"""
    定义函数，根据成绩计算等级。
    输入：96
    输出：优秀
"""


# def get_score_level(score):
#     if score < 0 or score > 100:
#         return "成绩输入有误"
#     elif 90 <= score:
#         return "优秀"
#     elif 80 <= score:
#         return "良好"
#     elif 60 <= score:
#         return "及格"
#     else:
#         return "不及格"

def get_score_level(score):
    if score < 0 or score > 100:
        return "成绩输入有误"
    if 90 <= score:
        return "优秀"
    if 80 <= score:
        return "良好"
    if 60 <= score:
        return "及格"
    return "不及格"


print(get_score_level(95))
