# Imports all the test files
from .https import https


def run(url):
    results = {}
    # Check HTTPS in set
    result = https(url)
    results.update({'HTTPS': result})
    print('HTTPS is enabled: ', result)
