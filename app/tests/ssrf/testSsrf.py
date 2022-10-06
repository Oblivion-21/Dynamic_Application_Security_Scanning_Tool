import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
import requests
import testManager


#Setup main fuction taking in url as an argument
async def testSsrf(ws, session, testConfigs, url):
    try:
        if "://" not in url:
            url = f"https://{url}"
        requests.get(url) 
    except Exception as e:
        return await testManager.sendMessage(ws, {"message": "The URL you have entered either does not exist or is not responding"}, url, True, "testSSRF")

    configuration = cloudmersive_validate_api_client.Configuration()
    configuration.api_key["Apikey"] = "dd8e000b-9aa3-4991-8925-10835200c34d"
    # create an instance of the API class
    apiInstance = cloudmersive_validate_api_client.DomainApi(cloudmersive_validate_api_client.ApiClient(configuration))
    await test(ws, url, apiInstance)


async def test(ws, url, apiInstance):
    request = cloudmersive_validate_api_client.UrlSsrfRequestFull(f"{url}")
    try:
        apiResponse = apiInstance.domain_ssrf_check(request)
        await testManager.sendMessage(ws, {"message": str(apiResponse)}, url, True, "testSSRF")
    except ApiException as e:
        errorException = ("Exception when calling DomainApi->domain_ssrf_check: %s\n" % e)
        await testManager.sendMessage(ws, {"message": str(errorException)}, url, True, "testSSRF")
