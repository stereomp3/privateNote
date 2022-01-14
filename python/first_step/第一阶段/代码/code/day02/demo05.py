"""
    真值表达式

    条件表达式

    练习:exercise12.py
"""
content = input("请输入内容：")
# if content != "":
#     print("真值")

if content:  # bool(content)
    print("真值")

# 根据一个条件，为变量进行赋值。
# if input("请输入性别：") == "男":
#     sex = 1
# else:
#     sex = 0

sex = 1 if input("请输入性别：") == "男" else 0
