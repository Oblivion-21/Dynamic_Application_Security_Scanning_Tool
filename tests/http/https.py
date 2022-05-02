import requests

def https(url):
    try:
        r = requests.get(f"https://{url}")
        if 'https' in r.url:
            return 'PASSED'
        else:
            return 'FAILED'
     except:
         return 'INCOMPLETE'
