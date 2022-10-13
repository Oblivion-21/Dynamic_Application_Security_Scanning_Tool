import aiohttp
import mock
import pytest

from tests.xss import testXss
pytest_plugins = 'pytest_asyncio'


@pytest.mark.asyncio
async def testHttpsTrue(mocker):
    '''check the https status against a known true'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testHttps.testHttps(None, getSession(), 'www.google.com', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testHttpsFalse(mocker):
    '''check the https status against a known false'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testHttps.testHttps(None, getSession(), 'httpforever.com', False)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testSelfSignedCertificateInvalid(mocker):
    '''check self signed certificate aginst known invalid'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testCertificates.testSelfSignedCertificate(None, 'expired.badssl.com', False)
    msg = asyncMock.call_args[0][1]['message']
    assert 'INCOMPLETE' in msg

    # TEARDOWN
    mocker.stopall()