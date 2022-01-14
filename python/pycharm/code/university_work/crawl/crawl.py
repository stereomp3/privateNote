# import json   # 要轉json時用
# import re  # 使用正規表達式
# import requests
# from lxml import etree
from pyppeteer import launch
import asyncio
from pyquery import PyQuery as pq

list01 = []
dict01 = [
    {"國旅券": '#domesticTravel li'},
    {"i 原券": '#iYuan li'},
    {"農遊券": '#agriculture li'},
    {"數位藝fun券": '#artFunE li'},
    {"紙本藝fun券": '#artFunP li'},
    {"動茲券": '#sports li'},
    {"客庄券": '#hakka li'},
    {"地方創生券": '#rgionalRevitalization li'},
]


def bonus5():
    flag = False
    number = input("請輸入要查詢的數字:")
    for y in range(len(list01)):
        for k, v in list01[y].items():
            for i in range(len(v)):
                if len(v[i]) == 2:
                    if number[-2:] == v[i]:
                        print("中了" + k)
                        flag = True
                else:
                    if number[-3:] == v[i]:
                        print("中了" + k)
                        flag = True
    if not flag:
        print('沒中獎')

async def main():
    # launch 方法會新建一個 Browser 對象，然後賦值給 browser，然後調用 newPage 方法相當於瀏覽器中新建了一個選項卡，同時新建了一個 Page 對象。
    browser = await launch(devtools=True)  # launch(devtools=True)可以開啟偵錯，讓網頁顯示

    # Page 對象調用了 goto 方法就相當於在瀏覽器中輸入了這個 URL，瀏覽器跳轉到了對應的頁面進行加載
    page = await browser.newPage()

    await page.goto('https://vhpi.5000.gov.tw/')

    while True:
        try:
            week = input("請輸入查詢周次:")
            await page.waitForSelector('#period2')
            await page.click('#period' + week, options={
                'button': 'left',
                'clickCount': 2,  # 1 or 2
                'delay': 500,  # 毫秒
            })
        except Exception:
            print("input error，please try again")
        else:
            break

    doc = pq(await page.content())
    # doc 是 CSS 的選擇器，可以抓取裡面內容
    for i in range(len(dict01)):
        for key, value in dict01[i].items():
            list01.append({key: doc(value).text().split(" ")})

    print(list01)
    bonus5()


asyncio.get_event_loop().run_until_complete(main())



'''
# 請求並接收
# response = requests.get("https://vhpi.5000.gov.tw/")
# response.status_code 回傳狀態 200,404,...
# response.content 回傳內容編碼 (純二進制)
# response.text 回傳Unicode型數據
# 解析內容 (轉為string)
# content = response.content.decode()

# 把string轉為hmtl node tree，回傳根節點
# html = etree.HTML(content)

# 用xpth抓值
# get_bonus = html.xpath("//*[@id='domesticTravel']/li[1]")

# 用regex抓
# get_bonus = re.findall(r'<script>([^winNo].*)</script>', content, re.MULTILINE)
# print(get_bonus)
'''

'''
bonus_str = "".join(get_bonus)
bonus_list = bonus_str.split("var")

for i in range(len(bonus_list) - 1, -1, -1):
    temp_str = "".join(bonus_list[i])
    if temp_str.find(" winNo", 0, len(temp_str)) == -1:
        del bonus_list[i]

del bonus_list[-1]
del bonus_list[-1]

result_list = []
for i in range(len(bonus_list)):
    temp_str = "".join(bonus_list[i])
    temp_list = list(temp_str)
    del temp_list[1:10]
    temp_str02 = " ".join(temp_list)
    result_list.append(temp_str02)

for i in result_list:
    print(i)
'''

'''
for i in bonus_list:
    print(i)

# str to json
json_data = json.loads(get_bonus)


# 印出第一個
print(json_data["data"]["items"][0])
'''
