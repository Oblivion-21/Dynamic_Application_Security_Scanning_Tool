import mock
import pytest

from tests.xss import testXss
pytest_plugins = 'pytest_asyncio'

# Test XSS against a known True
@pytest.mark.asyncio
async def testXssTrue(mocker):

    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testXss.testXss(None, None, None, 'https://github.com/Oblivion-21/Dynamic_Application_Security_Scanning_Tool/', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'PASSED'

    mocker.stopall()

# Test XSS against a known False
@pytest.mark.asyncio
async def testXssFalse(mocker):

    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testXss.testXss(None, None, None, 'https://xss-game.appspot.com/level1/frame', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'FAILED'

    mocker.stopall()

# Test XSS against a known Incomplete
@pytest.mark.asyncio
async def testXssIncomplete(mocker):

    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testXss.testXss(None, None, None, 'https://google.com', False)
    msg = asyncMock.call_args[0][1]['message']
    assert 'INCOMPLETE' in msg

    mocker.stopall()