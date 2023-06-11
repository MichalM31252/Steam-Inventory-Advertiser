import json
import requests
import time

session = requests.Session()


idProfilu = "76561198231636540"

url = f"http://steamcommunity.com/inventory/{idProfilu}/730/2?"

print(url)

params = {
    'l': 'english',
    'count': '5000'
}    

r = requests.get(url=url, params=params)

paczka_json = r.json()

#print(json.dumps(paczka_json, indent=2))