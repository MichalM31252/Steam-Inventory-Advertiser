import requests

class SteamInterface():
    def get_inv_info():
        profileId = "76561198231636540"
        url = f"http://steamcommunity.com/inventory/{profileId}/730/2?"
        params = {
            'l': 'english',
            'count': '5000'
        }    

        return requests.get(url=url, params=params).json()
