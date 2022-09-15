import testManager


async def testTest(ws, session, testConfig, url):
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
        

    await testManager.sendMessage(ws, {"message": testResult}, True, "testTest")


#Duplicate for async testing
async def testTestDuplicate(ws, session, testConfig, url):
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
        

    await testManager.sendMessage(ws, {"message": testResult}, True, "testTestDuplicate")
