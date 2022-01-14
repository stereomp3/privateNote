"""
    在控制台中循環輸入內容，如果空則停止
    打印所有不重複的內容
"""
set01 = set()
while True:
    str_input = input("請輸入內容:")
    if str_input == "": break
    set01.add(str_input)

for i in set01:
    print(i)
