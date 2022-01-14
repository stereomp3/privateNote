"""
    将两个列表合并为一个字典。
    输入：["张无忌","赵敏","周芷若"] [101,102,103]
    输出：{"张无忌":101,"赵敏":102,"周芷若":103}
"""
list_names = ["张无忌", "赵敏", "周芷若"]
list_rooms = [101, 102, 103]

# dict_result = {}
# for i in range(len(list_names)):
#     dict_result[list_names[i]] = list_rooms[i]

dict_result = {list_names[i]: list_rooms[i] for i in range(len(list_names))}
print(dict_result)
