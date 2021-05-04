import json
import requests
import time

url = "https://api.pricempire.com/v1/getAllItems"

steamid = 76561198231636540

params = {
    'token': 'b1ae9a77-3e46-4f66-be4f-98283279c74d'
}    

r = requests.get(url=url, params=params)

paczka_json = r.json()

print(json.dumps(paczka_json,indent=2))

time.sleep(2000)
    
