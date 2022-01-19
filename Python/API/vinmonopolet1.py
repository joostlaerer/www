from msilib.schema import Upgrade
import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    
""" parameters = {
    "lat": 40.71,
    "lon": -74
} """

response = requests.get("https://apis.vinmonopolet.no/products/v0/details-normal")


jprint(response.json())