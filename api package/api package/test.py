# importing the requests library
import json
from RunForest.core import Controller

# api-endpoint
URL = "http://localhost/api/receipts"
USER = 'admin'
PASSWORD = 'Fun4Justin'


# defining a params dict for the parameters to be sent to the API
#PARAMS = {}

# sending get request and saving the response as response object
#r = requests.get(url=URL, params=PARAMS, auth=(USER, PASSWORD))

# extracting data in json format
#data = r.json()

api = Controller(USER, PASSWORD)

data = api.get_receipts()

with open('data.json', 'w') as f:
    json.dump(data, f)
