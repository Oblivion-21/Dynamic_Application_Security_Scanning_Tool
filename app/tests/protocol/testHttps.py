import requests
import sys
sys.path.append("/")
from app import testManager


async def testHttps(ws, session, url):
    '''Check if HTTPS is enabled on site'''
    try:
        response = await testManager.sendRequest(session, url)

        if 'https' in str(response.url):
            message = 'PASSED'
        else:
            message = 'FAILED'
    except Exception as e:
        message = f'INCOMPLETE - {e}'
    finally:
        await testManager.sendMessage(ws, {"message": message}, True, 'testProtocolHttps')
