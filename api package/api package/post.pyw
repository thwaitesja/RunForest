import json
from RunForest.core import Controller

# api-endpoint

USER = 'kings'
PASSWORD = 'Fun4Sooper'

api = Controller(USER, PASSWORD)

# print(api.get_receipts())


with open('payload.json', 'r') as f:
	api.make_receipt(filestream = f)
	api.qr()