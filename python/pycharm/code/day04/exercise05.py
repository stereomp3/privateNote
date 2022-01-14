"""
    在終端中輸入商品信息(名稱與單價)
    如果輸入為空則停止輸入
    最後打印所有商品信息(一行一個)
"""
dict01 = {}
while True:
    name = input("請輸入商品名稱:")
    if name == "":
        break
    prices = input("請輸入商品價格:")
    if prices == "":
        break
    dict01[name] = prices
for k, v in dict01.items():
    print("%s的商品價格是%s" % (k, v))

if "遊戲機" in dict01:
    print(dict01["遊戲機"])  # 如果有輸入遊戲機，打印其價格
