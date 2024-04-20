import asyncio
from pyppeteer import launch


async def main():
   browserObj =await launch({"headless": False})
   url = await browserObj.newPage()
   await url.goto('https://scrapeme.live/shop/')


   ## Get HTML
   htmlContent = await url.content()
   await browserObj.close()
   return htmlContent


response = asyncio.get_event_loop().run_until_complete(main())
print(response)
