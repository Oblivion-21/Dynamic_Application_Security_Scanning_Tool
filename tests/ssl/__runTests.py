# Imports all the test files
from .tls_version import *


def run(url):
    results = {}
    # Check the default TLS version used
    result = default_tls_version(url)
    results.update({'Default TLS version': result})
    print('Default TLS version: ', result)

    # # Check if SSL version 2 is supported
    # result = tls_version_connection(url, 'SSLv2')         # Need to compile open SSL without OPENSSL_NO_SSL2
    # results.update({'SSL 2 Supported': result})
    # print('SSL 2 Supported: ', result)
    #
    # # Check if SSL version 3 is supported
    # result = tls_version_connection(url, 'SSLv3')         # Need to compile open SSL without OPENSSL_NO_SSL3
    # results.update({'SSL 3 Supported': result})
    # print('SSL 3 Supported: ', result)

    # Check if TLS version 1.0 is supported
    result = tls_version_connection(url, 'TLSv1.0')
    results.update({'TLS1.0 Supported': result})
    print('TLS1.0 Supported: ', result)

    # Check if TLS version 1.1 is supported
    result = tls_version_connection(url, 'TLSv1.1')
    results.update({'TLS1.1 Supported': result})
    print('TLS1.1 Supported: ', result)

    # Check if TLS version 1.2 is supported
    result = tls_version_connection(url, 'TLSv1.2')
    results.update({'TLS1.2 Supported': result})
    print('TLS1.2 Supported: ', result)

    # Check if TLS version 1.3 is supported
    result = tls_version_connection(url, 'TLSv1.3')
    results.update({'TLS1.3 Supported': result})
    print('TLS1.3 Supported: ', result)
