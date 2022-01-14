"""
    對字符串:"  自強不 息,  厚德 載物. "
    查找空格數量
    刪除所有空格
    查找"厚德"位置
    判斷是否以"自強開頭"
"""

message = "   自強不 息,  厚德 載物. "

print(message.count(" "))
print(message.replace(" ", ""))
print(message.find("厚德"))
print(message.startswith("自強"))
print(message)

