import requests
import testManager
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

async def testXss(ws, session, testConfigs, url, useDatabase):
    try:
        xssResult = scanXss(url)
        if xssResult:
            await testManager.sendMessage(ws, {"message": "FAILED"}, url, True, "xss", useDatabase)
        else:
            await testManager.sendMessage(ws, {"message": "PASSED"}, url, True, "xss", useDatabase)
        
    except Exception as e:
        await testManager.sendMessage(ws, {"message": f"INCOMPLETE - {e}"}, url, True, "xss", useDatabase)
              
# When provided with a URL returns number of forms present
def getAllForms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Extracts HTML form information 
def getFormDetails(form):
    details = {}
    action = form.attrs.get("action", "").lower()   # Retrieve form action, e.g. target URL
    method = form.attrs.get("method", "get").lower()    # Retrieve form method e.g. POST, GET
    
    # Retrieve form input data
    inputs = []
    for inputTag in form.find_all("input"):
        inputType = inputTag.attrs.get("type", "text")
        inputName = inputTag.attrs.get("name")
        inputs.append({"type": inputType, "name": inputName})
    
    # Returns all data into a dictionary 
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    
    return details

# Submits form defined in formDetails
def submitForm(formDetails, url, value):
    targetUrl = urljoin(url, formDetails["action"]) # Creates an absolute URL if input was relative
   
    inputs = formDetails["inputs"] # Retrieves form inputs
    
    data = {}
    for input in inputs: # Replace all text and search values
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        inputName = input.get("name")
        inputValue = input.get("value")

        if inputName and inputValue: # If input name and value are not null add to form submission 
            data[inputName] = inputValue

    if formDetails["method"] == "post":
        return requests.post(targetUrl, data=data)
    else:
        return requests.get(targetUrl, params=data)

# Determine site vulnerability
def scanXss(url):
    # Retrieve all forms from the submitted URL
    forms = getAllForms(url)
    print(f"\nDetected {len(forms)} forms on {url}.")
    jsScript = "<script>alert('')</script>"
    isVulnerable = False
    for form in forms: 
        formDetails = getFormDetails(form)
        content = submitForm(formDetails, url, jsScript).content.decode()
        if jsScript in content:
            isVulnerable = True
            return isVulnerable 
    return isVulnerable
