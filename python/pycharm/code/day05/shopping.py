trade_item_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

Order = []


def search_trade_item(cid):
    while True:
        if cid in trade_item_info:
            return cid
        else:
            return "该商品不存在"


def check_trade_item(sum_result):
    for item in Order:
        shang_pin = trade_item_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
        sum_result += shang_pin["price"] * item["count"]
        return sum_result


def buy_trade_item():
    while True:
        pay_money = float(input("总价%d元，请输入金额：" % Order[1]["sum_price"]))
        if pay_money >= (Order[1]["sum_price"]):
            print("购买成功，找回：%d元。" % (pay_money - Order[1]["sum_price"]))
            Order.clear()
            return
        print("金額不足")


def shopping():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            for key, value in trade_item_info.items():
                print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
            cid = search_trade_item(int(input("请输入商品编号：")))
            count = int(input("请输入购买数量："))
            Order.append({"cid": cid, "count": count})
            print("添加到购物车。")
        elif item == "2":
            Order.append({"sum_price": check_trade_item(0)})
            buy_trade_item()


shopping()
