import sys
# Imports all the test files
from https import https

results = {}
url = sys.argv[1]

# Check HTTPS in set
result = https(url)
results.update({'HTTPS': result})
print('HTTPS is enabled: ', result)
