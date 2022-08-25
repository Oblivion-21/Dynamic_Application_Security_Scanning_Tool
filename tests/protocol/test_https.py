import TestManager
import requests


async def test_https(ws, url):
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
        await TestManager.send_msg(ws, {"message": message}, True, 'test-https')
