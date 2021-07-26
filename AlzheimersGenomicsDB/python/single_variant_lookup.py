''' lookup a single variant'''
import requests
import json
from os.path import join
from sys import exit

import constants as C

endpoint = 'variant'
requestUri = join(C.SERVICE_URI, endpoint)

payload = {'id': 'rs429358'}

response = requests.get(requestUri, params=payload)
if response.status_code == C.SUCCESS:
    rjson = response.json()
else:
    print("ERROR", str(response.status_code) + ": ", response.content.decode())
    exit()

print(json.dumps(rjson, indent=4, sort_keys=True))
