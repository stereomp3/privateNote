"""
    在控制台中輸入學生信息(名稱、性別、年齡、成績)，如果輸入為空，打印信息(一行一個)
    數據結構:
    [
        {"name":"悟空", "sex":"男", "age":23, "score":100}
    ]
    利用列表存儲類別
    用字典存儲個人資料
"""
list_data = []
while True:
    stu_name = input("請輸入名稱:")
    if stu_name == "":
        break
    stu_gender = input("請輸入性別:")
    stu_age = input("請輸入年齡:")
    stu_grade = input("請輸入成績:")
    dict_person = {"name": stu_name, "sex": stu_gender, "age": stu_age, "score": stu_grade}
    list_data.append(dict_person)
    # list_data.append({"name": stu_name, "sex": stu_gender, "age": stu_age, "score": stu_grade})

for item in list_data:
    print("我叫%s，今年%s歲，性別%s，考了%s分" % (item["name"], item["age"], item["sex"], item["score"]))
