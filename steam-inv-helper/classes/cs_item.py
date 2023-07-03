import re

class CsItem():
    def __init__(self, asset_id, market_hash_name, steam_user_id64):
        self.asset_id = asset_id
        self.market_hash_name = market_hash_name
        self.steam_user_id64 = steam_user_id64

    def set_market_hash_name_shorter(self):
            to_shorten = {
                "(Factory New)": "FN",
                "(Minimal Wear)": "MW",
                "(Field-Tested)": "FT",
                "(Well-Worn)": "WW",
                "(Battle-Scarred)":"BS",
                "StatTrak\u2122": "ST",
                "Souvenir": "Souv"
            }

            #there isn't a return because multiple matches can be spotted in the market_hash_name
            for key, value in to_shorten.items():
                if key in self.market_hash_name:
                    self.market_hash_name_shorter = self.market_hash_name.replace(key, value).replace(' | ',' ')
                
    def set_inspect_link(self,description):
        self.inspect_link = description['actions'][0]['link'].replace('%owner_steamid%',self.steam_user_id64).replace(" ", "%20").replace('%assetid%',self.asset_id)
                
    def set_tradebility_status(self, description):
        self.tradeable = 0 if description['tradable'] == 0 else 1

    def set_applied_stickers(self, description):
        sticker_response = description['descriptions'][-1]['value']
        if "sticker" in sticker_response:
            cleaner = re.compile('<.*?>') 
            self.stickers = re.sub(cleaner, '', sticker_response)[9:].split(", ")