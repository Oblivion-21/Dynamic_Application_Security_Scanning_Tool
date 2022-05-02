import socket, ssl


# Check sites default TLS version
def default_tls_version(url):
    context = ssl.create_default_context()
    with socket.create_connection((url, '443')) as sock:
        with context.wrap_socket(sock, server_hostname = url) as ssock:
            return ssock.version()


# Check if site supports TLS version xx
def tls_version_connection(url, tls_version):
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
        # context = ssl.create_default_context()
        context.options |= ssl.OP_NO_SSLv2
        context.options |= ssl.OP_NO_SSLv3
        context.options |= ssl.OP_NO_TLSv1
        context.options |= ssl.OP_NO_TLSv1_1
        context.options |= ssl.OP_NO_TLSv1_2

    try:
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname = url)
        conn.connect((url, 443))
        if tls_version == 3:
            eval("conn.getpeercert()['version']==3")
        conn.close()
        return 'PASSED'
    except ssl.SSLError:
        return 'FAILED'
    except Exception as e:
        print(e)
        return 'INCOMPLETE'
