import subprocess
import testManager
import errno
import threading


async def timeout(process):
    '''Timer function to kill the DDoS attack after the specified timeout period'''
    if process.poll() is None:
        try:
            process.kill()
        except OSError as e:
            if e.errno != errno.ESRCH:
                raise


async def testDdos(ws, session, config, url):
    '''DDoS test against site'''
    message = 'PASSED'
    try:
        if '://' not in url:
            url = f"https://{url}"
        dos = subprocess.Popen(f'go run /app/hulk/hulk.go -site {url}', shell=True)
        timer = await threading.Timer( int(config['ddosDuration']), timeout, [dos] )

        timer.start()
        timer.join()
        timer.cancel()

        # Test if the website is still up, we get a response back it means it surived the DoS
        response = await testManager.sendRequest(session, url)

    # except aiohttp.ClientResponseError:
    #     message = 'FAILED'

    except Exception as e:
        message = f'INCOMPLETE - {e}'

    finally:
        await testManager.sendMessage(ws, {"message": message}, True, 'testDdos')
