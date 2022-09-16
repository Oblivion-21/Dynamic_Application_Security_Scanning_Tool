import testManager
import requests


async def testHttps(ws, url):
    '''Check if HTTPS is enabled on site'''
    try:
        r = requests.get(f"https://{url}")
        if 'https' in r.url:
            message = 'PASSED'
        else:
            message = 'FAILED'
    except Exception as e:
        message = f'INCOMPLETE - {e}'
    finally:
        await TestManager.sendMessage(ws, {"message": message}, True, 'testProtocolHttps')
