import requests

class SteamInterface():
    def get_inv_info(self, profile_id):
        url = f"http://steamcommunity.com/inventory/{profile_id}/730/2?"
        params = {
            'l': 'english',
            'count': '5000'
        }    

        return requests.get(url=url, params=params).json()
