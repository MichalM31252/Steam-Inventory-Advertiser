import re

class CsItem():
    def __init__(self, assetId, marketHashName, steamUserId64):
        self.assetId = assetId
        self.marketHashName = marketHashName
        self.steamUserId64 = steamUserId64

    def getMarketHashNameShorter(self):
            toShorten = {
                "(Factory New)": "FN",
                "(Minimal Wear)": "MW",
                "(Field-Tested)": "FT",
                "(Well-Worn)": "WW",
                "(Battle-Scarred)":"BS",
                "StatTrak\u2122": "ST",
                "Souvenir": "Souv"
            }

            #nie ma return ponieważ może się pojawić kilka kluczy w nazwie
            for key, value in toShorten.items():
                if key in self.marketHashName:
                    self.marketHashNameShorter = self.marketHashName.replace(key, value).replace(' | ',' ')
                
    def getInspectLink(self,description):
        self.inspectLink = description['actions'][0]['link'].replace('%owner_steamid%',self.steamUserId64).replace(" ", "%20").replace('%assetid%',self.assetId)
                
    def getTradebilityStatus(self, description):
        self.tradeable = 0 if description['tradable'] == 0 else 1

    def getAppliedStickers(self, description):
        stickerResponse = description['descriptions'][-1]['value']
        if "sticker" in stickerResponse:
            cleaner = re.compile('<.*?>') 
            self.stickers = re.sub(cleaner, '', stickerResponse)[9:].split(", ")