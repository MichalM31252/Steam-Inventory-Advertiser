import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


class DBConnection():
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="", database="przedmioty_cs")
        self.cur = self.con.cursor(buffered=True)

    #sprawdzenie czy informacje o przedmiocie znajdują się w bazie danych
    def checkForExistingRecords(self, assetId):
        self.cur.execute("SELECT assetId, COUNT(*) FROM useritems WHERE assetId = %s GROUP BY assetId", (assetId,)) ######
        self.cur.fetchall()
        row_count = self.cur.rowcount ######
        if(row_count == 1):
            return True
        
    def __del__(self):
        self.cur.close()
        self.con.close()

class CsItem():
    def __init__(self, assetId, marketHashName, inspectlinkRaw):
        self.assetId = assetId
        self.marketHashName = marketHashName
        self.inspectlink = inspectlinkRaw.replace('%owner_steamid%',os.getenv('STEAM_USERID64')).replace(" ", "%20").replace('%assetid%',self.assetId)

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

            for key, value in toShorten.items():
                if key in self.marketHashName:
                    self.marketHashNameShorter = self.marketHashName.replace(key, value).replace(' | ',' ')
                    return
                

    #def getStickers():

    #def getStatus():    i tradeable i marketable

