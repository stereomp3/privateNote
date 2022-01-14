"""
    輸入成績，判斷等級
"""
grade = float(input("請輸入成績:"))

# if 100 >= grade >= 90:
#     print("成績良好")
# elif 90 > grade >= 80:
#     print("成績優秀")
# elif 80 > grade >= 60:
#     print("成績及格")
# elif 60 > grade >= 0:
#     print("成績不及格")
# else:
#     print("成績輸入錯誤")

# 下面的寫法只需要讓電腦進行一次判斷，範圍大的判斷寫前面
if grade < 0 or grade > 100:
    print("成績輸入錯誤")
if grade >= 90:
    print("成績良好")
elif grade >= 80:
    print("成績優秀")
elif grade >= 60:
    print("成績及格")
else:
    print("成績不及格")

