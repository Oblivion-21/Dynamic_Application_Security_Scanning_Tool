import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
# from pprint import pprint

# When provided with a URL returns number of forms present
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Extracts HTML form information 
def get_form_details(form):  
    details = {}
    action = form.attrs.get("action", "").lower()   # Retrieve form action, e.g. target URL
    method = form.attrs.get("method", "get").lower()    # Retrieve form method e.g. POST, GET
    
    # Retrieve form input data
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    
    # Returns all data into a dictionary 
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    
    return details

# Submits form defined in form_details
def submit_form(form_details, url, value):
    
    target_url = urljoin(url, form_details["action"]) # Creates an absolute URL if input was relative
   
    inputs = form_details["inputs"] # Retrieves form inputs
    
    data = {}
    for input in inputs: # Replace all text and search values
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")

        if input_name and input_value: # If input name and value are not null add to form submission 
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Determine site vulnerability
def scan_xss(url):
    
    # Retrieve all forms from the submitted URL
    forms = get_all_forms(url)
    print(f"Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('xss')</script>"
    is_vulnerable = False
    for form in forms: 
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            # print(f"XSS Detected on {url}")
            # print(f"Form details:")
            # pprint(form_details)
            is_vulnerable = True
            print("XSS Vulnerability Detected?") 
        return is_vulnerable

if __name__ == "__main__":
    url = input("Please input a URL: ")
    print(scan_xss(url))