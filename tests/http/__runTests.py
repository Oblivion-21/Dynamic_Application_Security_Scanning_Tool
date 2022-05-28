# Imports all the test files
from .https import https
from .headers import headers


def run(url):
    results = {}
    # Check HTTPS in set
    result = https(url)
    results.update({'HTTPS': result})
    print('HTTPS is enabled: ', result)

    # Check HTTP headers
    headers_result = headers(url)
    for header in headers_result:
        print(f"{header}: {headers_result[header]}")
        results.update({header: headers_result[header]})
