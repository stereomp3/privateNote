dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


class ShopModel:
    def __init__(self, name="", price=0, number=0, id=0):
        self.name = name
        self.price = price
        self.number = number
        self.id = id
        self.__controller = ShopManageController()


class ShopManageController:
    def __init__(self):
        self.__shop_info = []
        self.__list_order = []

    @property
    def shop_info(self):
        return self.__shop_info

    @property
    def list_order(self):
        return self.__list_order

    # @list_order.setter
    # def list_order(self, value):
    #     list_order = value

    def init_info(self):
        self.__shop_info.append(ShopModel("屠龍刀", 10000, 0, 101))
        self.__shop_info.append(ShopModel("倚天劍", 10000, 0, 102))
        self.__shop_info.append(ShopModel("九陰白骨爪", 8000, 0, 103))
        self.__shop_info.append(ShopModel("九陽神功", 9000, 0, 104))
        self.__shop_info.append(ShopModel("降龍十八掌", 8000, 0, 105))
        self.__shop_info.append(ShopModel("乾坤大挪移", 10000, 0, 106))

    def add_item_to_list(self, shop_id, num):
        for n in range(len(self.__shop_info)):
            if shop_id == self.__shop_info[n].id:
                temp = self.__shop_info[n]
                temp.number = num
                self.__list_order.append(temp)

    def calculate_total_price(self):
        total_price = 0
        for item in self.__list_order:
            total_price += item.price * item.number
        return total_price


class ShopManageView:
    def __init__(self):
        self.__controller = ShopManageController()

    def main(self):
        self.__controller.init_info()
        while True:
            try:
                item = input("1鍵購買，2鍵結算。")
                if item == "1":
                    self.buying()
                elif item == "2":
                    self.settlement()
            except:
                print("請輸入正確格式")

    def buying(self):
        self.print_commdity_info()
        self.create_order()
        print("添加到購物車。")

    def settlement(self):
        total_price = self.__controller.calculate_total_price()
        self.print_order_into()
        self.paying(total_price)

    def print_commdity_info(self):
        for item in self.__controller.shop_info:
            print("編號：%d，名稱：%s，單價：%d。" % (item.id, item.name, item.price))

    def create_order(self):
        while True:
            cid = int(input("請輸入商品編碼："))
            if cid in dict_commodity_info:
                break
            else:
                print("該商品不存在")
        count = int(input("請輸入購買數量："))
        self.__controller.add_item_to_list(cid, count)

    def print_order_into(self):
        for order in self.__controller.list_order:
            print("商品：%s，單價：%d,數量:%d." % (order.name, order.price, order.number))

    def paying(self, price):
        while True:
            money = float(input("總價%d元，请输入金額：" % price))
            if money >= price:
                print("購買成功，找回：%d元。" % (money - price))
                self.__controller.list_order.clear()
                break
            else:
                print("金額不足.")


view = ShopManageView()
view.main()
