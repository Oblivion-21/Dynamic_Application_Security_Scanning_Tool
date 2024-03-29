import subprocess
import testManager


async def testDdos(ws, session, config, url, useDatabase):
    '''DDoS test against site'''
    message = 'PASSED'
    try:
        if '://' not in url:
            url = f"https://{url}"
        dos = subprocess.Popen(
            f"timeout {config['ddosDuration']} go run /app/hulk/hulk.go -site {url}",
            shell=True,
            stderr=subprocess.PIPE
        )
        dos.wait()

        # Test if the website is still up, we get a response back it means it survived the DoS
        res = await testManager.sendRequest(session, url)
        message = 'PASSED'
        if not res:
            message = 'FAILED'
    except Exception as e:
        message = f'INCOMPLETE - {e}'

    finally:
        await testManager.sendMessage(ws, {"message": message}, url, True, 'testDdos', useDatabase)
