import TestManager
import requests


async def https_test(ws, url):
    try:
        r = requests.get(f"https://{url}")
        if 'https' in r.url:
            message = 'PASSED'
        else:
            message = 'FAILED'
    except:
        message = 'INCOMPLETE'
    finally:
        await TestManager.send_msg(ws, {"message": message}, True, 'https-test')
