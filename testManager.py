import aiohttp
import asyncio
import json
import API
from tests import testRequests
from tests.protocol import TestHttps, TestSsl

suit_id = 0


suiteID = 0

async def sendMessage(ws, msg, test=False, test_type=None):
    if test:
        test_finished = {
            "message-type": "TEST_FINISHED",
            "suit-id": suiteID,
            "test": test_type,
            "results": msg
        }
        return await API.sendMessage(ws, json.dumps(test_finished))
    await API.sendMessage(ws, msg)


async def runTests(ws, msg):
    data = json.loads(msg)
    testList = list(data['tests'].keys())
    testConfigs = data['tests']
    testUrl = data['url']
    
    testSuite = await initSuite()

    await sendMessage(ws, createSuite(testList))
    await sendMessage(ws, startSuite(testList))    
    await requests.runSuite(ws, testSuite, testConfigs, testUrl)

def createSuite(testList):
    global suiteID
    suiteID += 1
    suiteCreated = {
        "message-type": "SUITE_CREATED",
        "suit-id": suiteID,
        "tests": testList
    }
    return json.dumps(suiteCreated)


def startSuite(testList):
    suiteStarted = {
        "message-type": "SUITE_STARTED",
        "suit-id": suiteID,
        "tests": testList
    }
    return json.dumps(suiteStarted)

async def initSuite():
    #Initialize test name and function map
    testSuite = {
        #Enter your test functions and names here
        'testTest': TestRequests.testTest,
        'testTestDuplicate': TestRequests.testTestDuplicate
      #  'testProtocolHttps': TestHttps.testHttps
    }

    return testSuite
