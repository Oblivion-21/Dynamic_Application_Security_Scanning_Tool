import json

import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
import requests
import testManager


#Setup main fuction taking in url as an argument
async def testSsrf(ws, session, testConfigs, url, useDatabase):
    

    configuration = cloudmersive_validate_api_client.Configuration()
    configuration.api_key["Apikey"] = "dd8e000b-9aa3-4991-8925-10835200c34d"
    # create an instance of the API class
    apiInstance = cloudmersive_validate_api_client.DomainApi(cloudmersive_validate_api_client.ApiClient(configuration))
    await test(ws, url, apiInstance, useDatabase)


async def test(ws, url, apiInstance, useDatabase):
    request = cloudmersive_validate_api_client.UrlSsrfRequestFull(f"{url}")
    try:
        apiResponse = apiInstance.domain_ssrf_check(request)
        if apiResponse.clean_url and apiResponse.threat_level == "None":
            await testManager.sendMessage(ws, {"message": "PASSED"}, url, True, "testSSRF", useDatabase)
            return
        await testManager.sendMessage(ws, {"message": "FAILED"}, url, True, "testSSRF", useDatabase)
    except ApiException as e:
        await testManager.sendMessage(ws, {"message": f"INVALID - {e}"}, url, True, "testSSRF", useDatabase)
