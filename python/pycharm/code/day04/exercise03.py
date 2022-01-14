"""
    生成1~10間的數字，將其平方後存入list01
    將list01中的奇數存入list02
    將list01中所有大於5的偶數加1後存入list03
"""
list01 = [i ** 2 for i in range(1, 11)]  # 列表推導式，從for開始讀
list02 = [i for i in list01 if i % 2]  # 列表推導式
list03 = [i + 1 for i in list01 if not i % 2 and i > 5]  # 列表推導式
print(list01)
print(list02)
print(list03)
