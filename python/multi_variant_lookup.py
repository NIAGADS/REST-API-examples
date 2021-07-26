''' script looks up multiple variants'''
import requests
import json
from os.path import join
from sys import exit

import constants as C

def submit_request(uri, params):
  ''' submit the request / check for error in response'''
  response = requests.get(uri, params=params)
  if response.status_code == C.SUCCESS:
    rjson = response.json()
    return rjson
  else:
    print("ERROR", str(response.status_code) + ": ", response.content.decode())
    exit()

if __name__ == "__main__":
  endpoint = 'variant'
  requestUri = join(C.SERVICE_URI, endpoint)
  payload = {'id':  C.VARIANT_LIST}

  variants = C.VARIANT_LIST.split(',')
  print("Number variants in lookup:", len(variants))

  rjson = submit_request(requestUri, payload)

  # response is paged / how many pages do we expect:
  print("Paging: ", json.dumps(rjson['paging']))
  numPages = rjson['paging']['total_pages']

  # TODO: iterate over pages & perform some operation 
  for p in range(1, numPages + 1): # ranges not inclusive end
    print("Requesting Page ", p, "of", numPages)
    payload = {'id': C.VARIANT_LIST, 'page': p}
    rjson = submit_request(requestUri, payload)
    # print(json.dumps(rjson))
  

