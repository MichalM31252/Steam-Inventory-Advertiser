import requests

def getInvInfo():
    idProfilu = "76561198231636540"
    url = f"http://steamcommunity.com/inventory/{idProfilu}/730/2?"

    params = {
        'l': 'english',
        'count': '5000'
    }    

    return requests.get(url=url, params=params).json()
