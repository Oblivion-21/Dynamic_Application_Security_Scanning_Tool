import requests
import bs4
import mock
import pytest

@pytest.mark.asyncio
async def BruteForceFalse(mocker):
    '''check the https status against a known false'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testBruteForce.testBruteForce(None, None, None, 'www.team17.com/wp-login.php', False)
    msg = asyncMock.call_args[0][1]['Message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()

@pytest.mark.asyncio
async def BruteForceTrue(mocker):
    '''check the https status against a known false'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testBruteForce.testBruteForce(None, None, None, 'https://s1.swin.edu.au/eStudent/login.aspx', False)
    msg = asyncMock.call_args[0][1]['Message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()

@pytest.mark.asyncio
async def BruteForceInvalid(mocker):
    '''check the https status against a known false'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testBruteForce.testBruteForce(None, None, None, 'google.com', False)
    msg = asyncMock.call_args[0][1]['Message']
    assert msg == 'INVALID'

    # TEARDOWN
    mocker.stopall()