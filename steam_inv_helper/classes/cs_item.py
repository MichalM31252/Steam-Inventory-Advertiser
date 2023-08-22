class CSItem:
    def __init__(self, asset_id, name, exterior, steam_user_id64):
        self.asset_id = asset_id
        self.name = name
        self.exterior = exterior
        self.steam_user_id64 = steam_user_id64

    async def set_shorter_exterior(self):
        to_shorten = {
            "Factory New": "FN",
            "Minimal Wear": "MW",
            "Field-Tested": "FT",
            "Well-Worn": "WW",
            "Battle-Scarred": "BS",
        }

        self.exterior = self.exterior.replace(" | ", " ")
        for key, value in to_shorten.items():
            if key in self.exterior:
                self.exterior = self.exterior.replace(key, value)
                return

    async def set_inspect_link(self, description):
        self.inspect_link = (
            description["actions"][0]["link"]
            .replace("%owner_steamid%", self.steam_user_id64)
            .replace(" ", "%20")
            .replace("%assetid%", self.asset_id)
        )

    async def set_tradebility_status(self, description):
        self.tradeable = 0 if description["tradable"] == 0 else 1

    def set_screenshot_link(self, swapgg_response):
        self.screenshot_link = swapgg_response["result"]["imageLink"]

    def set_item_float(self, swapgg_response):
        self.item_float = str(swapgg_response["result"]["itemInfo"]["floatvalue"])[:9]

    def set_applied_stickers(self, swapgg_response):
        self.stickers = [None, None, None, None, None]
        sticker_list = swapgg_response["result"]["itemInfo"]["stickers"]
        for element in sticker_list:
            self.stickers[element["slot"]] = element["name"]
