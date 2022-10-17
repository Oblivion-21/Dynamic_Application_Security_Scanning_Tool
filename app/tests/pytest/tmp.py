#!/usr/bin/env python3

import socket
import ssl

url = 'https://tls-v1-0.badssl.com'
port = 1010


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.options |= ssl.OP_NO_SSLv2
context.options |= ssl.OP_NO_SSLv3
context.options |= ssl.OP_NO_TLSv1
context.options |= ssl.OP_NO_TLSv1_1
context.options |= ssl.OP_NO_TLSv1_3

conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=url)
conn.connect((url, port))
if tls_version == 3:
    eval("conn.getpeercert()['version']==3")
conn.close()
