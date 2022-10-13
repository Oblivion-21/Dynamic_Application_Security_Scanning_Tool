import subprocess
import errno
import threading
import time

def timeout(process):
    '''Timer function to kill the DDoS attack after the specified timeout period'''
    if process.poll() is None:
        try:
            process.kill()
        except OSError as e:
            if e.errno != errno.ESRCH:
                raise


def testDdos(ws, session, config, url):
    '''DDoS test against site'''
    message = 'PASSED'
    if '://' not in url:
        url = f"https://{url}"

    print(f"timeout: {config['ddosDuration']}")
    time.sleep(3)

    dos = subprocess.Popen('timeout 3 go run /app/tests/ddos/go.go', shell=True, stderr = subprocess.PIPE)

#    try:
#        outs, errs = dos.communicate(timeout=3)
#    except subprocess.TimeoutExpired as e:
#        dos.kill()
#        outs, errs = dos.communicate()
#        print(outs)
#        print(errs)


#    timer = threading.Timer( int(config['ddosDuration']), timeout, [dos] )

#    timer.start()
#    timer.join()
#    timer.cancel()

    # Test if the website is still up, we get a response back it means it surived the DoS
    # response = await testManager.sendRequest(session, url)

    # except aiohttp.ClientResponseError:
    #     message = 'FAILED'

    # except Exception as e:
    #     message = f'INCOMPLETE - {e}'

    # finally:
    #     await testManager.sendMessage(ws, {"message": message}, True, 'testDdos')

testDdos(None, None, {'ddosDuration': '3'}, 'google.com')
