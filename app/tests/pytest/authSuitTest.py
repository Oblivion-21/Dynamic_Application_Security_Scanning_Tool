import mock
import pytest
from tests.authentication import testBruteForce

@pytest.mark.asyncio
async def testBruteForceFalse(mocker):
    '''check the https status against a known false'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testBruteForce.testBruteForce(None, None, {"username": "admin"}, 'www.team17.com/wp-login.php', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()

@pytest.mark.asyncio
async def testBruteForceTrue(mocker):
    '''check the https status against a known false'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testBruteForce.testBruteForce(None, None, {"username": "admin"}, 'https://s1.swin.edu.au/eStudent/login.aspx', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()

@pytest.mark.asyncio
async def testBruteForceInvalid(mocker):
    '''check the https status against a known false'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testBruteForce.testBruteForce(None, None, {"username": "admin"}, 'google.com', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'INVALID'

    # TEARDOWN
    mocker.stopall()