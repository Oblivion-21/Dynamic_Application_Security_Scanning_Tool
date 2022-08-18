import json

import API
from tests import TestTest
from tests.protocol import test_https

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
    await test_https.https_test(ws, url)


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
