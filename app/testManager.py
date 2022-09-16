from tests import testRequests
import aiohttp
import asyncio
import json
import API


suiteID = 0

async def sendMessage(ws, msg, test=False, testType=None):
    if test:
        testFinished = {
            "message-type": "TEST-FINISHED",
            "suit-id": suiteID,
            "test": testType,
            "results": msg
        }
        return await API.sendMessage(ws, json.dumps(testFinished))
    await API.sendMessage(ws, msg)


async def runTests(ws, msg):
    data = json.loads(msg)
    testList = list(data['tests'].keys())
    testConfigs = data['tests']
    testUrl = data['url']

    testSuite = await initSuite(testList)

    await sendMessage(ws, createSuite(testList))
    await sendMessage(ws, startSuite(testList))
    await runSuite(ws, testSuite, testConfigs, testUrl)

def createSuite(testList):
    global suiteID
    suiteID += 1
    suiteCreated = {
        "message-type": "SUITE-CREATED",
        "suiteID": suiteID,
        "tests": testList
    }
    return json.dumps(suiteCreated)


def startSuite(testList):
    suiteStarted = {
        "message-type": "SUITE-STARTED",
        "suiteID": suiteID,
        "tests": testList
    }
    return json.dumps(suiteStarted)


def stringToFunc(testStr):
    if testStr == "testTest":
        return testRequests.testTest
    elif testStr == "testTestDuplicate":
        return testRequests.testTestDuplicate

async def initSuite(testList):
    #Initialize test name and function map
    testSuite = {testStr: stringToFunc(testStr) for testStr in testList}
    return testSuite

#Send singular request with existing asynchronous session
async def sendRequest(session, url):
    try:
        if "://" not in url:
            url = f"https://{url}"
        #Fetch individual request content
        async with session.get(url) as response:
            if response.status < 200 or response.status > 299:
                raise aiohttp.ClientResponseError()

            #Return awaited response content
            return response

    except Exception as e:
        print(e)

        return response

#Run suite of tests asynchronously
async def runSuite(ws, testSuite, testConfigs, url):
    #Stasrt async session
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False),
        timeout=aiohttp.ClientTimeout(total=60)) as session:

        try:
            #Call all tests asynchronously
            await asyncio.gather(
                *[testSuite[test](ws, session, testConfigs[test], url) for test in testConfigs.keys()]
            )
        except Exception as e:
            print(e)
            await sendMessage(ws, {"message": "Invalid test type supplied"}, True, "Other")
