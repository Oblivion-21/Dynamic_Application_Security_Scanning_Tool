import json

import API
from tests import TestTest
from tests.protocol import test_https, test_ssl

suit_id = 0


async def send_msg(ws, msg, test=False, test_type=None):
    if test:
        test_finished = {
            "message-type": "TEST_FINISHED",
            "suit-id": suit_id,
            "test": test_type,
            "results": msg
        }
        return await API.send_msg(ws, json.dumps(test_finished))
    await API.send_msg(ws, msg)


async def test_manager(ws, msg):
    data = json.loads(msg)
    test_list = list(data["tests"].keys())

    print(ws)
    url='www.google.com' # This will be the website selected by the user to run the test's against

    await send_msg(ws, create_suite(test_list))
    await send_msg(ws, start_suite(test_list))
    await TestTest.test_test(ws)

    # Protocol tests
    await test_https.test_https(ws, url)
    await test_ssl.test_default_tls(ws, url)
    # await test_ssl.test_tls_version(ws, url, 'SSLv2')   Need to wait until we have a container so we can
    # await test_ssl.test_tls_version(ws, url, 'SSLv3')   compile open SSL without OPENSSL_NO_SSL2/3
    # await test_ssl.test_tls_version(ws, url, 'TLSv1.0') also to suport tls v1.0 and v1.1
    # await test_ssl.test_tls_version(ws, url, 'TLSv1.1')
    await test_ssl.test_tls_version(ws, url, 'TLSv1.2')
    await test_ssl.test_tls_version(ws, url, 'TLSv1.3')


def create_suite(tests):
    global suit_id
    suit_id += 1
    suit_created = {
        "message-type": "SUITE_CREATED",
        "suit-id": suit_id,
        "tests": tests
    }
    return json.dumps(suit_created)


def start_suite(tests):
    suit_started = {
        "message-type": "SUITE_STARTED",
        "suit-id": suit_id,
        "tests": tests
    }
    return json.dumps(suit_started)
