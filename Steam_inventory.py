import json
import requests
import time

session = requests.Session()

url = "http://steamcommunity.com/profiles/76561198231636540/inventory/json/730/2"

steamid = 76561198231636540

params = {
    'l': 'english',
    'key': '799A514B28CF4BCE9F53B4F0272BD8F9',
    'steamid': steamid
}    

r = requests.get(url=url, params=params)

paczka_json = r.json()

print(json.dumps(paczka_json, indent=2))

time.sleep(180)