import requests
import ssl
from urllib.parse import urlparse
import http.client


def headers(url):
    ctx = ssl._create_stdlib_context()
    conn = http.client.HTTPSConnection(url, context = ctx )
    conn.request('HEAD', '')
    res = conn.getresponse()
    headers = res.getheaders()

    # Ideal header response
    ideal_headers = {
    'X-Frame-Options': ['sameorigin', 'deny'],
    'X-XXS-Protection': ['1', '1; mode=block', '1; report=<reporting-URI>'],
    'Strict-Transport-Security': ['max-age'] # there is no poor config with this header

    }

    results = {}

    # Check the returned header against the idea header
    for ideal_header in ideal_headers:
        for header in headers:
            if header[0] == ideal_header and header[1].lower() in ideal_headers[ideal_header]:
                results.update({ideal_header: 'PASSED'})
                break
        if ideal_header not in results:
            results.update({ideal_header: 'FALIED'})

    return results
