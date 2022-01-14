"""
2. 在控制台中重复获取编码值打印字符串，如果输入空，则退出程序。
"""

while True:
    str_code = input("请输入编码值：")
    if str_code == "":
        break
    char = chr(int(str_code))
    print(char)