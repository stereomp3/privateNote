"""
    重複輸入編碼值打印字符串，如果輸入為空，則退出程式
"""
while True:
    UserInput = (input("輸入編碼值:"))
    if UserInput == "":
        break
    print(chr(int(UserInput)))