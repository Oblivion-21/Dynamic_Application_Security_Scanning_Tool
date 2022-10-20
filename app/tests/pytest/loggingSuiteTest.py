import mock
import pytest

from tests.logging import testLogging

pytest_plugins = 'pytest_asyncio'

# Test logging against a known True
@pytest.mark.asyncio
async def testLoggingTrue(mocker):

    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testLogging.testLogging(None, None, None, 'google.com', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'PASSED'

    mocker.stopall()

# Test logging against a known False
@pytest.mark.asyncio
async def testLoggingFalse(mocker):

    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testLogging.testLogging (None, None, None, 'https://liveswinburneeduau-my.sharepoint.com/:u:/g/personal/102568843_student_swin_edu_au/Efh1aNATAp9Avm_9N4-EUFIBEfS7q6VWpkE7byjxRZr_ug?e=h71kNn', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'FAILED'

    mocker.stopall()

# Test logging against a known Incomplete
@pytest.mark.asyncio
async def testLoggingIncomplete(mocker):

    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testLogging.testLogging(None, None, None, 'badwebsite.com', False)
    msg = asyncMock.call_args[0][1]['message']
    assert 'INVALID' in msg

    mocker.stopall()