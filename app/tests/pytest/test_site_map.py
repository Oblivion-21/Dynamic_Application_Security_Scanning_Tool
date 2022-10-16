import aiohttp
import mock
import pytest

from tests.siteMap import siteMap
pytest_plugins = 'pytest_asyncio'


def getSession():
    return aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False),
        timeout=aiohttp.ClientTimeout(total=60)
    )

@pytest.mark.asyncio
async def test_site_map_pass(mocker):
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await siteMap.siteMap(None, getSession(), {}, 'https://www.basicwebsiteexample.com/', None)
    msg = asyncMock.call_args[0][1]['message']
    content = asyncMock.call_args[0][1]['content']
    assert msg == 'PASSED'
    assert content == {"siteMap":"['https://www.basicwebsiteexample.com/widgets', 'https://www.basicwebsiteexample.com/media', 'https://www.basicwebsiteexample.com/social', 'https://www.basicwebsiteexample.com/arbablog', 'https://www.basicwebsiteexample.com/menu', 'https://www.basicwebsiteexample.com/ecommerce', 'https://www.basicwebsiteexample.com/contact', 'https://www.basicwebsiteexample.com/none', 'https://twitter.com/share?text=This is a widget example.&url=https://www.basicwebsiteexample.com/social', 'https://www.basicwebsiteexample.com/arbablog/10-reasons-you-should-blog', 'https://www.basicwebsiteexample.com/menu#menu-section-12078', 'https://www.basicwebsiteexample.com/menu#menu-section-12081']","failedURLs":"['https://www.basicwebsiteexample.com/none']"}

    # TEARDOWN
    mocker.stopall()

@pytest.mark.asyncio
async def test_site_map_fail(mocker):
    # SETUP
    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    await siteMap.siteMap(None, getSession(), {}, 'bruh', None)
    msg = asyncMock.call_args[0][1]['message']
    content = asyncMock.call_args[0][1]['content']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()