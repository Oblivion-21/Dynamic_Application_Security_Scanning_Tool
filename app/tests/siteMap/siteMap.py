import testManager
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import asyncio
import time
import re


async def siteMap(ws, session, testConfig, url, useDatabase):
    await testManager.sendMessage(ws, {"message": "CRAWLING"},url, True, "siteMap", useDatabase)
    if '://' not in url:
        url = f"http://{url}"

    siteMap = []
    failedURLs = []
    queue = [url]
    limit = int(testConfig.get('limit', 30))

    while len(queue) > 0 and len(siteMap) < limit:
        print("Mapping urls:" + str(queue[:5]) + "\n")
        try:
            responses = await asyncio.gather(
                    *[testManager.getSiteContent(session, reqURL) for reqURL in queue[:5]]
            )
        except Exception as e:
            print(e)
            await testManager.sendMessage(ws, {"message": "INCOMPLETE"}, True, "siteMap", useDatabase)
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

        print("Current map:" + str(siteMap) + "\n")
        print('Waiting to avoid rate limiting...')
        time.sleep(10)

    print("Sitemap : " + str(siteMap))
    print(len(siteMap))

    result = 'PASSED' if siteMap != [] else 'FAILED'

    await testManager.sendMessage(ws, {"message": result, "content": {"siteMap": str(siteMap[:limit]), "failedURLs": str(failedURLs)}},url, True, "siteMap", useDatabase)
