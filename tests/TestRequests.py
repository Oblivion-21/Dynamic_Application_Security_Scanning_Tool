import TestManager
from lib.requests import sendRequest

async def testTest(ws, session, testConfig, url):
    try:
        testResult = ''
        response = await sendRequest(session, url)

        if 'https' in str(response.url):
            testResult = 'Passed'
        else:
            testResult = 'Failed'

    except Exception as e:
        print(e)
        testResult = 'Incomplete'
        

    await TestManager.sendMessage(ws, {"message": testResult}, True, "test-test")


#Duplicate for async testing
async def testTestDuplicate(ws, session, testConfig, url):
    try:
        testResult = ''
        response = await sendRequest(session, url)

        if 'https' in str(response.url):
            testResult = 'Passed'
        else:
            testResult = 'Failed'

    except Exception as e:
        print(e)
        testResult = 'Incomplete'
        

    await TestManager.sendMessage(ws, {"message": testResult}, True, "test-test")
