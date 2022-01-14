"""
    在終端輸入字符，輸入為空則傳回輸入字符拼接成的字符串
"""
list_temp = []
while True:
    str_input = input("請輸入:")
    if str_input == "":
        break
    list_temp.append(str_input)
str_result = "".join(list_temp)
print(str_result)
