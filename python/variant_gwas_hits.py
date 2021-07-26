''' two ways to find tracks in which a variant has genome-wide significance'''
import requests
import json
from os.path import join

import constants as C

def submit_request(uri, params):
  ''' submit the request / check for error in response'''
  response = requests.get(uri, params=params)
  if response.status_code == C.SUCCESS:
    rjson = response.json()
    return rjson
  else:
    print("ERROR", str(response.status_code) + ": ", response.content.decode())

def variant_gwas_hits_service(variant):
    '''
    use the variant top hits service to set your own threshold for genome-wide significance
    and retrieve data track information and p-values for all hits meeting your query criteria
    '''

    endpoint = 'variant/gwas/hits'
    payload = { 'id': variant, 'pvalueCutoff': 5e-8}
    requestUri = join(C.SERVICE_URI, endpoint)

    print("Variant GWAS Hits Service")    
    rjson = submit_request(requestUri, payload)
    return rjson

def variant_lookup_service(variant):
    ''' 
    use the variant lookup service to retrieve the tracks in which 
    the variant has genome-wide significance (p <= 5e-8); this will
    also include curated GWAS catalogs 
    '''

    endpoint = 'variant' 
    requestUri = join(C.SERVICE_URI, endpoint)
    payload = {'id': variant}
    
    print("Variant Lookup Service")
    rjson = submit_request(requestUri, payload)
    return rjson['result'][C.VARIANT]['flagged_genomicsdb_datasets'] if rjson else None

if __name__ == "__main__":
    result = variant_lookup_service(C.VARIANT)
    print("Variant Lookup Result", result)

    result = variant_gwas_hits_service(C.VARIANT)
    print("Variant GWAS Hits Result:")
    print(json.dumps(result, indent=4, sort_keys=True))

    # print("Result (JSON) keys:", result.keys())
    


