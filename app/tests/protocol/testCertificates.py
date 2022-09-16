import ssl
import socket
from datetime import datetime
from time import strptime
import sys
sys.path.append("/")
from app import testManager

async def getCert(url):
    context = ssl.create_default_context()
    with socket.create_connection((url, '443')) as sock:
        with context.wrap_socket(sock, server_hostname=url) as ssock:
            return ssock.getpeercert(binary_form=False)


async def testSelfSignedCertificate(ws, url):
    '''Check if the SSL certificate is self signed'''
    message = ''
    try:
        cert = await getCert(url)

        if cert['subject'][0][0][1] == cert['issuer'][2][0][1]: # if subject and issuer are the same
            message = 'FAILED'
        else:
            message = 'PASSED'

    except ssl.SSLCertVerificationError as e:
        if e.verify_code == 18:
            # 18 = self signed cert
            message = 'FAILED'
        else:
            message = f'INCOMPLETE - {e.verify_message}'
    except Exception as e:
        message = f'INCOMPLETE - {e}'

    finally:
        await testManager.sendMessage(ws, {"message": message}, True, f'test-self-signed-certificate')



async def testExpiredCertificate(ws, url):
    '''Check if the SSL certificate is expired'''
    message = ''
    try:
        cert = await getCert(url)
        start_time = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y GMT')
        end_time = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')

        if start_time.timestamp() < datetime.utcnow().timestamp() < end_time.timestamp():
            message = 'PASSED'
        else:
            message = 'FAILED'

    except ssl.SSLCertVerificationError as e:
        if e.verify_code == 10:
            # 10 = expired cert
            message = 'FAILED'
        else:
            message = f'INCOMPLETE - {e.verify_message}'

    except Exception as e:
        message = f'INCOMPLETE - {e}'

    finally:
        await testManager.sendMessage(ws, {"message": message}, True, f'test-self-signed-certificate')



# try:
#     url = 'self-signed.badssl.com'
#     context = ssl.create_default_context()
#     with socket.create_connection((url, '443')) as sock:
#         with context.wrap_socket(sock, server_hostname=url) as ssock:
#             cert = ssock.getpeercert(binary_form=False)

# except ssl.SSLCertVerificationError as e:
#     print (e.verify_code)
#     if e.verify_code == 62:
#         print('yes')
