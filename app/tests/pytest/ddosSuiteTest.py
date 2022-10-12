import aiohttp
import mock
import pytest

from tests.ddos import testDdos
pytest_plugins = 'pytest_asyncio'


def getSession():
    return aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False),
        timeout=aiohttp.ClientTimeout(total=60)
    )

@pytest.mark.asyncio
async def testDdosTrue(mocker):
    '''run a ddos attack against a know resistant target'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testDdos.testDdos(None, getSession(), {'ddosDuration': '30'}, 'www.google.com', None)
    msg = asyncMock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()

@pytest.mark.asyncio
async def testDdosIncomplete(mocker):
    '''run a ddos attack against a none existant target'''
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await testDdos.testDdos(None, getSession(), {'ddosDuration': '30'}, 'www.gdsadsadsadsaoogle.com', None)
    msg = asyncMock.call_args[0][1]['message']
    assert 'INCOMPLETE' in msg

    # TEARDOWN
    mocker.stopall()
