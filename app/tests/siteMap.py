import testManager
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import asyncio
import time
import re


async def siteMap(ws, session, testConfig, url):

    if '://' not in url:
        url = f"http://{url}"

    siteMap = []
    failedURLs = []
    queue = [url]
    
    while len(queue) > 0 and len(siteMap) < 30:
        print("Mapping urls:" + str(queue[:5]) + "\n")
        try:
            responses = await asyncio.gather(
                    *[testManager.getSiteContent(session, reqURL) for reqURL in queue[:5]]
            )
        except Exception as e:
            print(e)
            await testManager.sendMessage(ws, {"message": "Sitemap Requests failed"}, True, "siteMap")
        queue = queue[5:]

        for response, baseURL in responses:
            try:
                parse = BeautifulSoup(response, 'html.parser')

                urls = [link.get('href') for link in parse.findAll('a')]

                for respURL in urls:

                    if '://' not in respURL:
                        respURL = urljoin(baseURL, respURL)
                
                    if (urlparse.urlparse(url).hostname in respURL and respURL not in siteMap and url != respURL and '.png' not in respURL and '.jpg' not in respURL):
                        siteMap.append(respURL)
                        queue.append(respURL)

            except Exception as e:
                print(e)
                print('Could not parse url: ' + baseURL)
                failedURLs.append(baseURL)
                # await testManager.sendMessage(ws, {"message": "Sitemap parse failed"}, True, "siteMap")

        print("Current map:" + str(siteMap) + "\n")
        print('Waiting to avoid rate limiting...')
        time.sleep(10)

    print("Sitemap : " + str(siteMap))
    print(len(siteMap))
    await testManager.sendMessage(ws, {"message": {"siteMap": str(siteMap), "failedURLs": str(failedURLs)}}, True, "siteMap")
    