import testManager
import urllib.parse as urlparse
import asyncio
import time
import re


async def siteMap(ws, session, testConfig, url):
    siteMap = []
    queue = [url]
    
    while len(queue) > 0:
        print("Mapping urls:" + str(queue) + "\n")
        try:
            responses = await asyncio.gather(
                    *[testManager.getSiteContent(session, reqURL) for reqURL in queue[-5:]]
            )
        except Exception as e:
            print(e)
            await testManager.sendMessage(ws, {"message": "Sitemap Requests failed"}, True, "siteMap")
        queue = []

        for response in responses:
            try:
                urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', response)
                for respURL in urls:
                    if (urlparse.urlparse(url).hostname in respURL and respURL not in siteMap and url != respURL):
                        siteMap.append(respURL)
                        queue.append(respURL)

            except Exception as e:
                print(e)
                await testManager.sendMessage(ws, {"message": "Sitemap parse failed"}, True, "siteMap")

        print("Current map:" + str(siteMap) + "\n")
        print('Waiting to avoid rate limiting...')
        time.sleep(5)

    print("Sitemap : " + str(siteMap))

    await testManager.sendMessage(ws, {"message": str(siteMap)}, True, "siteMap")
    