import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    await page.waitForSelector('.item .name')
    await page.click('.item .name', options={
        'button': 'left',
        'clickCount': 1,  # 1 or 2
        'delay': 1000,  # 毫秒
    })
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
