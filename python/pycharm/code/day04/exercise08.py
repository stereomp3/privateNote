"""
    在控制台中循環輸入多個人的多個喜好，如果名稱輸入為空則停止輸入
    最後打印所有信息
    數據結構
    {
        "宇謙":["抽菸","喝酒","燙頭"]
    }
"""
dict_persons = {}
while True:
    name = input("請輸入姓名:")
    if name == "":
        break
    dict_persons[name] = []  # 直接創建一個列表，對列表進行操作靠dict_person[name](鍵)
    while True:
        hobby = input("請輸入嗜好:")
        if hobby == "":
            break
        dict_persons[name].append(hobby)

for k, v_list in dict_persons.items():  # 沒寫item只會拿到key不會拿到value
    print(k + "喜歡:")
    for i in v_list:
        print(i)
