''' get top hits & associated features from a GWAS summary statistics data track'''
import requests
import json
from os.path import join

import constants as C

endpoint = 'dataset/gwas/top'
requestUri = join(C.SERVICE_URI, endpoint)
payload = {'track': C.TRACK}

response = requests.get(requestUri, params=payload)
if response.status_code == C.SUCCESS:
    rjson = response.json()
else:
    print("ERROR", str(response.status_code) + ": ", response.content.decode())
    exit()

# find the genes
genes = [hit for hit in rjson if hit['feature_type'] == 'gene']
print(json.dumps(genes, indent=4, sort_keys=True))

