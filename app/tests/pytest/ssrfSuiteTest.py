import mock
import pytest
import cloudmersive_validate_api_client

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

# Test SSRF against a known Incomplete
@pytest.mark.asyncio
async def testSsrfIncomplete(mocker):

    asyncMock = mock.AsyncMock()
    mocker.patch('testManager.sendMessage', side_effect=asyncMock)

    configuration = cloudmersive_validate_api_client.Configuration()
    configuration.api_key["Apikey"] = "a"
    # create an instance of the API class
    apiInstance = cloudmersive_validate_api_client.DomainApi(cloudmersive_validate_api_client.ApiClient(configuration))

    await testSsrf.test(None, 'https://github.com/Oblivion-21/Dynamic_Application_Security_Scanning_Tool/', apiInstance, False)
    msg = asyncMock.call_args[0][1]['message']
    assert 'INVALID' in msg

    mocker.stopall()