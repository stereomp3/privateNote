from pyppeteer import launch
import asyncio
import requests
from pyquery import PyQuery as pq

'''
url = 'http://quotes.toscrape.com/js/'
response = requests.get(url)
doc = pq(response.text)
print('Quotes:', doc('.quote').length)
'''


async def main():
    # launch 方法會新建一個 Browser 對象，然後賦值給 browser，然後調用 newPage 方法相當於瀏覽器中新建了一個選項卡，同時新建了一個 Page 對象。
    browser = await launch()

    # Page 對象調用了 goto 方法就相當於在瀏覽器中輸入了這個 URL，瀏覽器跳轉到了對應的頁面進行加載
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')

    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)

    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
