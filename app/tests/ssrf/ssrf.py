from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint
import testManager


#Setup main fuction taking in url as an argument
async def main(ws, url):
   #To do - creat ping test to check if website is up or down, if down immediatly return unclean URL and threat level high :) 

    configuration = cloudmersive_validate_api_client.Configuration()
    configuration.api_key['Apikey'] = 'dd8e000b-9aa3-4991-8925-10835200c34d'
    # create an instance of the API class
    api_instance = cloudmersive_validate_api_client.DomainApi(cloudmersive_validate_api_client.ApiClient(configuration))
    return await test(ws, url,api_instance)




async def test(ws, url,api_instance):
    request = cloudmersive_validate_api_client.UrlSsrfRequestFull(f'{url}')
    try:
        api_response = api_instance.domain_ssrf_check(request)
        return await  testManager.sendMessage(ws, {"message" : str(api_response)} , url , True , "testSSRF")
    except ApiException as e:
        error_exception = ("Exception when calling DomainApi->domain_ssrf_check: %s\n" % e)
        return await testManager.sendMessage(ws, {"message" : error_exception} , url , True , "testSSRF")

