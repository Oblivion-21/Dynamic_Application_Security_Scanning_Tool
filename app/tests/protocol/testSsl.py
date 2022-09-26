import socket
import ssl
import testManager


async def testDefaultTls(ws, url):
    '''Check a sites default TLS version'''
    try:
        context = ssl.create_default_context()
        with socket.create_connection((url, '443')) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssock:
                tls_version = ssock.version()

        if tls_version == 'TLSv1.3' or tls_version == 'TLSv1.2':
            message = 'PASSED'
        else:
            message = 'FAILED'
    except Exception as e:
        message = f'INCOMPLETE - {e.verify_message}'
    finally:
        await testManager.sendMessage(ws, {"message": message}, True, 'test-protocol-default-tls')


async def testTlsVersion(ws, url, tls_version, port=443):
    '''Check the tls/ssl versions supported by a site'''
    if tls_version == 'SSLv2':
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv2)
        context.maximum_version = ssl.SSLv2
        context.options |= ssl.OP_NO_SSLv3
        context.options |= ssl.OP_NO_TLSv1
        context.options |= ssl.OP_NO_TLSv1_1
        context.options |= ssl.OP_NO_TLSv1_2
        context.options |= ssl.OP_NO_TLSv1_3
    elif tls_version == 'SSLv3':
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
        context.options |= ssl.OP_NO_SSLv2
        context.options |= ssl.OP_NO_TLSv1
        context.options |= ssl.OP_NO_TLSv1_1
        context.options |= ssl.OP_NO_TLSv1_2
        context.options |= ssl.OP_NO_TLSv1_3
    elif tls_version == 'TLSv1.0':
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.options |= ssl.OP_NO_SSLv2
        context.options |= ssl.OP_NO_SSLv3
        context.options |= ssl.OP_NO_TLSv1_1
        context.options |= ssl.OP_NO_TLSv1_2
        context.options |= ssl.OP_NO_TLSv1_3
    elif tls_version == 'TLSv1.1':
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)
        context.options |= ssl.OP_NO_SSLv2
        context.options |= ssl.OP_NO_SSLv3
        context.options |= ssl.OP_NO_TLSv1
        context.options |= ssl.OP_NO_TLSv1_2
        context.options |= ssl.OP_NO_TLSv1_3
    elif tls_version == 'TLSv1.2':
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.options |= ssl.OP_NO_SSLv2
        context.options |= ssl.OP_NO_SSLv3
        context.options |= ssl.OP_NO_TLSv1
        context.options |= ssl.OP_NO_TLSv1_1
        context.options |= ssl.OP_NO_TLSv1_3
    elif tls_version == 'TLSv1.3':
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        #context = ssl.create_default_context()
        context.options |= ssl.OP_NO_SSLv2
        context.options |= ssl.OP_NO_SSLv3
        context.options |= ssl.OP_NO_TLSv1
        context.options |= ssl.OP_NO_TLSv1_1
        context.options |= ssl.OP_NO_TLSv1_2

    try:
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=url)
        conn.connect((url, port))
        if tls_version == 3:
            eval("conn.getpeercert()['version']==3")
        conn.close()
        message = 'PASSED'
    except ssl.SSLError:
        message = 'FAILED'
    except Exception as e:
        message = f'INCOMPLETE - {e}'
    finally:
        await testManager.sendMessage(ws, {"message": message}, True, f'test-protocol-{tls_version}')
