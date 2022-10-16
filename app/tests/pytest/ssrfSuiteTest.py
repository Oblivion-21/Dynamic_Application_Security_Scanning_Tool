import mock
import pytest

from tests.ssrf import testSsrf
pytest_plugins = 'pytest_asyncio'

# Test SSRF against a known True
@pytest.mark.asyncio
async def testSsrfTrue(mocker):

    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testSsrf.testSsrf(None, None, None, 'https://github.com/Oblivion-21/Dynamic_Application_Security_Scanning_Tool/', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'PASSED'

    mocker.stopall()

# Test SSRF against a known False
@pytest.mark.asyncio
async def testSsrfFalse(mocker):

    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testSsrf.testSsrf (None, None, None, 'http://169.254.169.254/', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'FAILED'

    mocker.stopall()

# # Test XSS against a known Incomplete
# @pytest.mark.asyncio
# async def testXssIncomplete(mocker):

#     asyncMock = mock.AsyncMock()
#     mocker.patch('testManager.sendMessage', side_effect=asyncMock)

#     await testXss.testXss(None, None, None, 'https://google.com', False)
#     msg = asyncMock.call_args[0][1]['message']
#     assert 'INCOMPLETE' in msg

#     mocker.stopall()