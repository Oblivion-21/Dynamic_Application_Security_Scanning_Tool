import mock
import pytest
from tests.protocol import test_https
pytest_plugins = 'pytest_asyncio'


@pytest.mark.asyncio
async def test_https_true(mocker):
    '''check the https status against a known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('TestManager.send_msg', side_effect=async_mock)

    await test_https.https_test(None, 'www.google.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'
    # TEARDOWN
    mocker.stopall()
