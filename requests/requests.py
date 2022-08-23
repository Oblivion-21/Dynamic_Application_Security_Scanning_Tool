import aiohttp
import asyncio

#Send singular request with existing asynchronous session
async def sendRequest(session, url):
    try:
        #Fetch individual request content
        async with session.get(url) as response:
            if response.status != 200:
                raise aiohttp.ClientResponseError()

            #Return awaited response content
            return response

    except Exception as e:
        return 'Request Failed: ' + 'Error code ' + response.status

#Run suite of tests asynchronously
async def runSuite(ws, testSuite, testConfigs, url):
    #Stasrt async session
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False),
        timeout=aiohttp.ClientTimeout(total=60)) as session:

        #Call all tests asynchronously 
        await asyncio.gather(
            *[testSuite[test](ws, session, testConfigs[test], url) for test in testConfigs.keys()]
        )
