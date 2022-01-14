"""
    輸入兩個數字和一個運算符，計算結果
"""
number01 = float(input("輸入數字:"))
Operation_symbol = input("輸入運算符:")
number02 = float(input("請輸入數字:"))
if Operation_symbol == "+":
    print("運算結果為:" + str(number01 + number02))
elif Operation_symbol == "-":
    print("運算結果為:" + str(number01 - number02))
elif Operation_symbol == "*":
    print("運算結果為:" + str(number01 * number02))
elif Operation_symbol == "/":
    print("運算結果為:" + str(number01 / number02))
else:
    print("運算符號有誤")
