# importing the requests library
import json
import requests

# api-endpoint
URL = "http://localhost/api/receipts/"
USER = 'king'
PASSWORD = 'Fun4Justin'

with open('payload.json', 'r') as f:
    data = dict(json.load(f)[0])
    # data_json = json.dumps(data)
    # data["items"] = [item for item in data["items"]]
    headers = {'Content-type': 'application/json'} #, 'Accept': 'text/plain'}
    # print(data_json)
    r = requests.post(url=URL, json=data, headers=headers, auth=(USER, PASSWORD))

# sending post request and saving response as response object


# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)
