import requests
from bs4 import BeautifulSoup
import testManager


# List of passcodes used for brute force
passList = ["^cH%seY9VP*%f7$k", "ueg+tja(Ush46fJ%",
    "sMcr3tseGnRR3TEf", "K3ffTykBM^yM#yuS",
    "86fKb8zB9HBA*RxX", "HEKFkUbyw4S3h2ug",
    "zh@RQ8Nj69##(@+e", "9YpRkh@vEb6tTRJc",
    "bABAGW+CgXc!h9mt", "&f@Ty7Su(SHmsRqj"
]

async def testBruteForce(ws, session, testConfigs, url, useDatabase):
    if "://" not in url:
        url = f"https://{url}"

    # Define Variables
    html = requests.get(url)

    soup = BeautifulSoup(html.content, 'html.parser')

    postFormList = soup.find_all('form')

    postUrlList = []

    username = testConfigs['username']

    # extracts html data from site to obtain the request_URL

    #TODO: Fix PostForm block to accept all sites
    for postForm in postFormList:
        action = postForm['action']
        if action == "":
            continue
        elif action[0] == '.':
            action = action.replace('.', url)
        elif action[0] == '/':
            action = url + action
        elif "://" not in action:
            action = url
        postUrlList.append(action)

    for scripts in soup.find_all("script"):
        
        if scripts.has_attr("src") and "https://www.google.com/recaptcha/api.js" in scripts["src"]:
            await testManager.sendMessage(ws, {"message": "PASSED"}, url, True, "bruteForceTest", useDatabase)
            return

    # sends username/password combinations to request_URL to detect status code. If the status code alters then the user has been kicked out
    # and the test is a success
    try:
        for postUrl in postUrlList:
            statusCodeInit = 0
            for password in passList:
                data = {'username': username, 'password': password, "Login": 'submit'}
                sendData = requests.post(postUrl, data=data)
                statusCode = sendData.status_code
                print(f"Brute Force Test, status code {url}: {statusCode}")
                if statusCodeInit == 0:
                    statusCodeInit = statusCode
                if statusCodeInit == 405:
                    await testManager.sendMessage(ws, {"message": "INVALID"}, url, True, "bruteForceTest", useDatabase)
                    return
                if statusCode != statusCodeInit:
                    await testManager.sendMessage(ws, {"message": "PASSED"}, url, True, "bruteForceTest", useDatabase)
                    return
        
        await testManager.sendMessage(ws, {"message": "FAILED"}, url, True, "bruteForceTest", useDatabase)
    except Exception as e:
        await testManager.sendMessage(ws, {"message": f"INCOMPLETE - {e}"}, url, True, "bruteForceTest", useDatabase)
