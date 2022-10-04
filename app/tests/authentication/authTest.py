import requests
from bs4 import BeautifulSoup
import testManager

#List of passcodes used for brute force
passlist = ["^cH%seY9VP*%f7$k", "ueg+tja(Ush46fJ%", 
"sMcr3tseGnRR3TEf", "K3ffTykBM^yM#yuS", 
"86fKb8zB9HBA*RxX", "HEKFkUbyw4S3h2ug", 
"zh@RQ8Nj69##(@+e", "9YpRkh@vEb6tTRJc", 
"bABAGW+CgXc!h9mt", "&f@Ty7Su(SHmsRqj" ]

async def bruteForceTest(ws, session, testConfigs, url):
    
    #Define Variables
    html = requests.get(url)

    soup = BeautifulSoup(html.content, 'html.parser')

    postformlist = soup.find_all('form')

    posturllist = [] 

    username = testConfigs['username']

    #extracts html data from site to obtain the request_URL
    for postform in postformlist:
        action = postform['action']
        if action == "":
            continue
        elif action[0] == '.':
            action = action.replace('.', url)
        posturllist.append(action)

    #sends username/password combinations to request_URL to detect status code. If the status code alters then the user has been kicked out
    #and the test is a success
    for posturl in posturllist:
        statuscodeinit = 0
        for password in passlist:
            data = {'username':username, 'password':password, "Login":'submit'}
            send_data = requests.post(posturl, data=data)
            statuscode = send_data.status_code
            print(f"Brute Force Test, status code {url}: {statuscode}")
            if statuscodeinit == 0:
                statuscodeinit = statuscode
            if statuscode != statuscodeinit:
                await testManager.sendMessage(ws, {"Message" : "success"}, url, True, "bruteForceTest")
                return
    
    await testManager.sendMessage(ws, {"Message" : "fail"}, url, True, "bruteForceTest")
                
        




