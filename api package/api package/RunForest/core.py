# importing the requests library
import json
import requests
import qrcode

# api-endpoint
Domain = "receiptforest.com"
URL = "http://" + Domain + "/api/receipts/"

class Controller():
    def __init__(self, username = "", password = ""):
        self.user = username
        self.password = password
        self.pk = 0

    def change_user(self, username):
        self.user = username

    def change_password(self, password):
        self.password = password

    def get_receipt(self, receipt_id):
        PARAMS = {'receipt_id': receipt_id}
        r = requests.get(url=URL, params=PARAMS, auth=(self.user, self.password))
        # print(r.text)
        return r.json()

    def get_receipts(self):
        PARAMS = {}
        r = requests.get(url=URL, params=PARAMS, auth=(self.user, self.password))
        # print(r.text)
        return r.json()

    def make_receipt(self, filestream = "", payload_path = ""):
        if filestream:
            try:
                data = dict(json.load(filestream)[0])
            except:
                data = dict(json.load(filestream))
        elif payload_path:
            try:
                with open(payload_path, 'r') as f:
                    data = dict(json.load(f))
            except:
                with open(payload_path, 'r') as f:
                    data = dict(json.load(f)[0])
        else:
            return 0
        headers = {'Content-type': 'application/json'}
        r = requests.post(url=URL, json=data, headers=headers, auth=(self.user, self.password))
        #print(r.text)
        if "pk" in r.json():
            self.pk = r.json()["pk"]
        else:
            self.pk = input("pk?")
        return self.pk

    def return_url(self):
        return "http://" + Domain + "/receipts/" + str(self.pk)
        
    def pkqr(self, pk):
        qrcode.make("http://" + Domain + "/receipts/" + pk).show()

    def qr(self):
        qrcode.make(self.return_url()).show()