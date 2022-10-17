import storageManager

ignoreSet = (
    "url",
    "tests",
    "suiteID",
    "messageType"
)


def analyse(url):
    rawRes = storageManager.showWithURL(url)
    runCount = len(rawRes)
    testCountMap = {
        "bruteForceTest": 0,
        "testDdos": 0,
        "xss": 0,
        "testSSRF": 0,
        "testProtocols": 0,
        "testLogging": 0
    }
    msgCountMap = {
        "PASSED": 0,
        "FAILED": 0,
        "INCOMPLETE": 0,
        "INVALID": 0
    }

    try:
        for run in rawRes:
            for key in run.keys():
                msgCount(key, run, msgCountMap)
            for test in run["tests"]:
                testCount(test, testCountMap)
    except Exception as e:
        print(f"ERROR: Data is malformed, please drop database and retry... exiting: {e}")

    reChartTestList = [{"name": itemPair[0], "value": itemPair[1]} for itemPair in testCountMap.items()]
    reChartMsgList = [{"name": itemPair[0], "value": itemPair[1]} for itemPair in msgCountMap.items()]
    overallScore = int((msgCountMap["PASSED"] / (msgCountMap["PASSED"] + msgCountMap["FAILED"])) * 100)
    return {
        "url": url,
        "overallScore": overallScore,
        "runCount": runCount,
        "testCount": reChartTestList,
        "msgCount": reChartMsgList
    }


def msgCount(key, run, msgCountMap):
    if key in ignoreSet:
        return
    msg = run[key]["message"]
    if key == "testProtocolTLSv1.1":
        if msg == "PASSED":
            msgCountMap["FAILED"] += 1
        elif msg == "FAILED":
            msgCountMap["PASSED"] += 1
    elif msg == "PASSED":
        msgCountMap[msg] += 1
    elif msg == "FAILED":
        msgCountMap[msg] += 1
    elif "INVALID" in msg:
        msgCountMap["INVALID"] += 1
    elif "INCOMPLETE" in msg:
        msgCountMap["INCOMPLETE"] += 1


def testCount(testData, testCountMap):
    if testData == "bruteForceTest":
        testCountMap["bruteForceTest"] += 1
    elif testData == "testDdos":
        testCountMap["testDdos"] += 1
    elif testData == "xss":
        testCountMap["xss"] += 1
    elif testData == "testSSRF":
        testCountMap["testSSRF"] += 1
    elif testData == "testProtocols":
        testCountMap["testProtocols"] += 1
