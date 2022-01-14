"""
    在控制台中循环录入学生信息(名称、性别、年龄、成绩)，如果名称录入为空，则停止录入。
    最后打印所有学生信息(一行一个)。
    数据结构：
    [
      {"name":"悟空","sex":"男","age":23,"score":100}
    ]
"""
list_persons = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    sex = input("请输入学生性别：")
    age = int(input("请输入学生年龄："))
    score = int(input("请输入学生成绩："))
    dict_person = {"name":name,"sex":sex,"age":age,"score":score}
    list_persons.append(dict_person)

for item in list_persons:
    print("我叫%s性别是%s今年%d岁啦考了%d分"%(item["name"],item["sex"],item["age"],item["score"]))