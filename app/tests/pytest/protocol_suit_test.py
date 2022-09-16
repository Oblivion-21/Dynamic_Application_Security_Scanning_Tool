import mock
import pytest

from tests.protocol import test_https, test_ssl
pytest_plugins = 'pytest_asyncio'


@pytest.mark.asyncio
async def test_https_true(mocker):
    '''check the https status against a known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('TestManager.send_msg', side_effect=async_mock)

    await test_https.test_https(None, 'www.google.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def test_https_false(mocker):
    '''check the https status against a known false'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('TestManager.send_msg', side_effect=async_mock)

    await test_https.test_https(None, 'httpforever.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


# @pytest.mark.asyncio
# async def test_tls_10_true(mocker):
#     '''check TLSv1.10 is enabled against a known true'''
#     # SETUP
#     async_mock = mock.AsyncMock()
#     mocker.patch('TestManager.send_msg', side_effect=async_mock)

#     await test_ssl.test_tls_version(None, 'tls-v1-0.badssl.com', 'TLSv1.0')
#     msg = async_mock.call_args[0][1]['message']
#     assert msg == 'PASSED'

#     # TEARDOWN
#     mocker.stopall()


# @pytest.mark.asyncio
# async def test_tls_10_false(mocker):
#     '''check TLSv1.0 is enabled against a known false'''
#     # SETUP
#     async_mock = mock.AsyncMock()
#     mocker.patch('TestManager.send_msg', side_effect=async_mock)

#     await test_ssl.test_tls_version(None, 'tls-v1-3.badssl.com', 'TLSv1.0')
#     msg = async_mock.call_args[0][1]['message']
#     assert msg == 'FAILED'

#     # TEARDOWN
#     mocker.stopall()


# @pytest.mark.asyncio
# async def test_tls_11_true(mocker):
#     '''check TLSv1.1 is enabled against a known true'''
#     # SETUP
#     async_mock = mock.AsyncMock()
#     mocker.patch('TestManager.send_msg', side_effect=async_mock)

#     await test_ssl.test_tls_version(None, 'tls-v1-1.badssl.com', 'TLSv1.1')
#     msg = async_mock.call_args[0][1]['message']
#     assert msg == 'PASSED'

#     # TEARDOWN
#     mocker.stopall()


# @pytest.mark.asyncio
# async def test_tls_11_false(mocker):
#     '''check TLSv1.1 is enabled against a known false'''
#     # SETUP
#     async_mock = mock.AsyncMock()
#     mocker.patch('TestManager.send_msg', side_effect=async_mock)

#     await test_ssl.test_tls_version(None, 'tls-v1-3.badssl.com', 'TLSv1.1')
#     msg = async_mock.call_args[0][1]['message']
#     assert msg == 'FAILED'

#     # TEARDOWN
#     mocker.stopall()


@pytest.mark.asyncio
async def test_tls_12_true(mocker):
    '''check TLSv1.2 is enabled against a known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('TestManager.send_msg', side_effect=async_mock)

    await test_ssl.test_tls_version(None, 'tls-v1-2.badssl.com', 'TLSv1.2', 1012)
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def test_tls_12_false(mocker):
    '''check TLSv1.2 is enabled against a known false'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('TestManager.send_msg', side_effect=async_mock)

    await test_ssl.test_tls_version(None, 'tls-v1-0.badssl.com', 'TLSv1.2', 1010)
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def test_tls_13_true(mocker):
    '''check TLSv1.3 is enabled against a known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('TestManager.send_msg', side_effect=async_mock)

    await test_ssl.test_tls_version(None, 'www.google.com', 'TLSv1.3')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def test_tls_13_false(mocker):
    '''check TLSv1.3 is enabled against a known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('TestManager.send_msg', side_effect=async_mock)

    await test_ssl.test_tls_version(None, 'tls-v1-0.badssl.com', 'TLSv1.3')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()
