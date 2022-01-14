"""
    將兩個列表合併為一個字典
    輸入 : ["張無忌","趙敏","周芷若"] [101, 102, 103]
    輸出 : {"張無忌":101,"趙敏":102,"周芷若":103}
"""
list_names = ["張無忌", "趙敏", "周芷若"]
list_room = [101, 102, 103]

#  自己寫
# count = 0
# for i in list_names:
#     dict_result[i] = list_room[count]
#     count += 1

# dict_result = {}
# for i in range(len(list_names)):
#     dict_result[list_names[i]] = list_room[i]

# 推導式
dict_result = {list_names[i]: list_room[i] for i in range(len(list_names))}

print(dict_result)
