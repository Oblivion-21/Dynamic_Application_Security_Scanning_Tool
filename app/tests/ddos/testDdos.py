import subprocess
import testManager
import errno
import threading
import time


async def testDdos(ws, session, config, url, useDatabase):
    '''DDoS test against site'''
    message = 'PASSED'
    try:
        if '://' not in url:
            url = f"https://{url}"
        dos = subprocess.Popen(f"timeout {config['ddosDuration']} go run /app/hulk/hulk.go -site {url}", shell=True, stderr = subprocess.PIPE)

        time.sleep(int(config['ddosDuration']) + 3)
        # Test if the website is still up, we get a response back it means it surived the DoS
        response = await testManager.sendRequest(session, url)

        message = 'PASSED'

    # except aiohttp.ClientResponseError:
    #     message = 'FAILED'

    except Exception as e:
        message = f'INCOMPLETE - {e}'

    finally:
        await testManager.sendMessage(ws, {"message": message}, True, 'testDdos', useDatabase)
