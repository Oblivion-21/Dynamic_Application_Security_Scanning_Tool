import aiohttp
import mock
import pytest

from tests.protocol import manager, testHttps, testSsl, testCertificates
pytest_plugins = 'pytest_asyncio'


def getSession():
    return aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False),
        timeout=aiohttp.ClientTimeout(total=60)
    )


@pytest.mark.asyncio
async def test_https_true(mocker):
    '''check the https status against a known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testHttps.testHttps(None, getSession(), 'www.google.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def test_https_false(mocker):
    '''check the https status against a known false'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testHttps.testHttps(None, getSession(), 'httpforever.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


# # @pytest.mark.asyncio
# # async def test_tls_10_true(mocker):
# #     '''check TLSv1.10 is enabled against a known true'''
# #     # SETUP
# #     async_mock = mock.AsyncMock()
# #     mocker.patch('testManager.sendMessage', side_effect=async_mock)

# #     await test_ssl.test_tls_version(None, 'tls-v1-0.badssl.com', 'TLSv1.0')
# #     msg = async_mock.call_args[0][1]['message']
# #     assert msg == 'PASSED'

# #     # TEARDOWN
# #     mocker.stopall()


# # @pytest.mark.asyncio
# # async def test_tls_10_false(mocker):
# #     '''check TLSv1.0 is enabled against a known false'''
# #     # SETUP
# #     async_mock = mock.AsyncMock()
# #     mocker.patch('testManager.sendMessage', side_effect=async_mock)

# #     await test_ssl.test_tls_version(None, 'tls-v1-3.badssl.com', 'TLSv1.0')
# #     msg = async_mock.call_args[0][1]['message']
# #     assert msg == 'FAILED'

# #     # TEARDOWN
# #     mocker.stopall()


# # @pytest.mark.asyncio
# # async def test_tls_11_true(mocker):
# #     '''check TLSv1.1 is enabled against a known true'''
# #     # SETUP
# #     async_mock = mock.AsyncMock()
# #     mocker.patch('testManager.sendMessage', side_effect=async_mock)

# #     await test_ssl.test_tls_version(None, 'tls-v1-1.badssl.com', 'TLSv1.1')
# #     msg = async_mock.call_args[0][1]['message']
# #     assert msg == 'PASSED'

# #     # TEARDOWN
# #     mocker.stopall()


# # @pytest.mark.asyncio
# # async def test_tls_11_false(mocker):
# #     '''check TLSv1.1 is enabled against a known false'''
# #     # SETUP
# #     async_mock = mock.AsyncMock()
# #     mocker.patch('testManager.sendMessage', side_effect=async_mock)

# #     await test_ssl.test_tls_version(None, 'tls-v1-3.badssl.com', 'TLSv1.1')
# #     msg = async_mock.call_args[0][1]['message']
# #     assert msg == 'FAILED'

# #     # TEARDOWN
# #     mocker.stopall()


@pytest.mark.asyncio
async def test_tls_12_true(mocker):
    '''check TLSv1.2 is enabled against a known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testSsl.testTlsVersion(None, 'tls-v1-2.badssl.com', 'TLSv1.2', 1012)
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def test_tls_12_false(mocker):
    '''check TLSv1.2 is enabled against a known false'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testSsl.testTlsVersion(None, 'tls-v1-0.badssl.com', 'TLSv1.2', 1010)
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def test_tls_13_true(mocker):
    '''check TLSv1.3 is enabled against a known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testSsl.testTlsVersion(None, 'www.google.com', 'TLSv1.3')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def test_tls_13_false(mocker):
    '''check TLSv1.3 is enabled against a known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testSsl.testTlsVersion(None, 'tls-v1-0.badssl.com', 'TLSv1.3')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testSelfSignedCertificateFail(mocker):
    '''check self signed certificate aginst known false'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testSelfSignedCertificate(None, 'self-signed.badssl.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testSelfSignedCertificatePass(mocker):
    '''check self signed certificate aginst known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testSelfSignedCertificate(None, 'google.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testSelfSignedCertificateInvalid(mocker):
    '''check self signed certificate aginst known invalid'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testSelfSignedCertificate(None, 'expired.badssl.com')
    msg = async_mock.call_args[0][1]['message']
    assert 'INCOMPLETE' in msg

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testExpiredCertificateFail(mocker):
    '''check expired certificate aginst known false'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testExpiredCertificate(None, 'expired.badssl.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testExpiredCertificatePass(mocker):
    '''check expired certificate aginst known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testExpiredCertificate(None, 'google.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testExpiredCertificateInvalid(mocker):
    '''check expired certificate aginst known invalid'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testExpiredCertificate(None, 'self-signed.badssl.com')
    msg = async_mock.call_args[0][1]['message']
    assert 'INCOMPLETE' in msg

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testWrongHostCertificateFail(mocker):
    '''check wrong host certificate aginst known false'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testWrongHostCertificate(None, 'wrong.host.badssl.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testWrongHostCertificatePass(mocker):
    '''check wrong host certificate aginst known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testWrongHostCertificate(None, 'google.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testWrongHostCertificateInvalid(mocker):
    '''check wrong host certificate aginst known invalid'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testWrongHostCertificate(None, 'self-signed.badssl.com')
    msg = async_mock.call_args[0][1]['message']
    assert 'INCOMPLETE' in msg

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testUntrustedRootCertificateFail(mocker):
    '''check untrusted root certificate aginst known false'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testUntrustedRootCertificate(None, 'untrusted-root.badssl.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'FAILED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testUntrustedRootCertificatePass(mocker):
    '''check untrusted root certificate aginst known true'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testUntrustedRootCertificate(None, 'google.com')
    msg = async_mock.call_args[0][1]['message']
    assert msg == 'PASSED'

    # TEARDOWN
    mocker.stopall()


@pytest.mark.asyncio
async def testUntrustedRootCertificateInvalid(mocker):
    '''check untrusted root certificate aginst known invalid'''
    # SETUP
    async_mock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=async_mock)

    await testCertificates.testUntrustedRootCertificate(None, 'self-signed.badssl.com')
    msg = async_mock.call_args[0][1]['message']
    assert 'INCOMPLETE' in msg

    # TEARDOWN
    mocker.stopall()
