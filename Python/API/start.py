from msilib.schema import Upgrade
import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)




response = requests.get("https://helsetankenapi.azurewebsites.net/swagger/v1/swagger.json")
jprint(response.json()) 