import storageManager
from tests import testRequests
<<<<<<< HEAD
from tests.ddos import testDdos
=======
from tests.xss import testXss
from tests.protocol import protocolManager
>>>>>>> main
import aiohttp
import asyncio
import json
import API
from tests.authentication import testBruteForce
from tests.ssrf import testSsrf

suiteID = 0


def setSuiteID():
    global suiteID
    temp = storageManager.currentIdentity()
    print(f"Setting suiteID from database: {temp}")
    suiteID = temp


async def sendMessage(ws, msg, url="", test=False, testType=None, useDatabase=False):
    if test:
        testFinished = {
            "messageType": "TEST-FINISHED",
            "url": url,
            "suiteID": suiteID,
            "test": testType,
            "results": msg
        }
        if useDatabase:
            storageManager.testUpdate(suiteID, testType, json.dumps(msg))
        return await API.sendMessage(ws, json.dumps(testFinished))
    await API.sendMessage(ws, msg)


async def runTests(ws, msg, useDatabase=False):
    data = json.loads(msg)
    testList = list(data['tests'].keys())
    testConfigs = data['tests']
    testUrl = data['url']

    testSuite = await initSuite(testList)

    await sendMessage(ws, createSuite(testUrl, testList, useDatabase))
    await sendMessage(ws, startSuite(testUrl, testList, useDatabase))
    await runSuite(ws, testSuite, testConfigs, testUrl, useDatabase)

def createSuite(testUrl, testList, useDatabase=False):
    global suiteID
    suiteID += 1
    suiteCreated = {
        "messageType": "SUITE-CREATED",
        "url": testUrl,
        "suiteID": suiteID,
        "tests": testList
    }
    jsonData = json.dumps(suiteCreated)
    if useDatabase:
        storageManager.insert(suiteID, testUrl, jsonData)
    return jsonData


def startSuite(testUrl, testList, useDatabase=False):
    suiteStarted = {
        "messageType": "SUITE-STARTED",
        "url": testUrl,
        "suiteID": suiteID,
        "tests": testList
    }
    jsonData = json.dumps(suiteStarted)
    if useDatabase:
        storageManager.update(suiteID, jsonData)
    return jsonData


def stringToFunc(testStr):
    if testStr == "testTest":
        return testRequests.testTest
    elif testStr == "testTestDuplicate":
        return testRequests.testTestDuplicate
    elif testStr == "testDdos":
        return testDdos.testDdos
    elif testStr == "bruteForceTest":
        return testBruteForce.testBruteForce
    elif testStr == "xss":
        return testXss.testXss
    elif testStr == "testSSRF":
        return testSsrf.testSsrf
    elif testStr == "testProtocols":
        return protocolManager.testToRun

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
async def runSuite(ws, testSuite, testConfigs, url, useDatabase=False):
    #Stasrt async session
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False),
        timeout=aiohttp.ClientTimeout(total=60)) as session:

        try:
            #Call all tests asynchronously
            await asyncio.gather(
                *[testSuite[test](ws, session, testConfigs[test], url, useDatabase) for test in testConfigs.keys()]
            )
        except Exception as e:
            print(e)
            await sendMessage(ws, {"message": f"Invalid test type supplied: {e}"}, url, True, "Other")
