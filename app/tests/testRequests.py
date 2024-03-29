import testManager


async def testTest(ws, session, testConfig, url, useDatabase=False):
    try:
        testResult = ''
        response = await testManager.sendRequest(session, url)

        if 'https' in str(response.url):
            testResult = 'Passed'
        else:
            testResult = 'Failed'

    except Exception as e:
        print(e)
        testResult = 'Incomplete'

    await testManager.sendMessage(ws, {"message": testResult}, url, True, "testTest", useDatabase)


#Duplicate for async testing
async def testTestDuplicate(ws, session, testConfig, url, useDatabase=False):
    try:
        testResult = ''
        response = await testManager.sendRequest(session, url)

        if 'https' in str(response.url):
            testResult = 'Passed'
        else:
            testResult = 'Failed'

    except Exception as e:
        print(e)
        testResult = 'Incomplete'

    await testManager.sendMessage(ws, {"message": testResult}, url, True, "testTestDuplicate", useDatabase)
