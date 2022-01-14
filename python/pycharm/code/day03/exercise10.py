"""
    輸入一個整數，打印一個矩形
    EX : 輸入4
         輸出 :
                ****
                *  *
                *  *
                ****
"""
number = int(input("輸入一個整數:"))
for i in range(number):
    if i == 0 or i == number - 1:
        print("*" * number)
    else:
        print("*" + " " * (number - 2) + "*")
