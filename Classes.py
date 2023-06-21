import mysql.connector
import os
from dotenv import load_dotenv
import re
import asyncio
import socketio
from websockets.sync.client import connect
import time

load_dotenv()

class DBConnection():
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="", database="przedmioty_cs")
        self.myCursor = self.con.cursor(buffered=True)

    #sprawdzenie czy informacje o przedmiocie znajdują się w bazie danych
    def checkForExistingRecords(self, assetId):
        self.myCursor.execute("SELECT assetId, COUNT(*) FROM useritems WHERE assetId = %s GROUP BY assetId", (assetId,)) ######
        self.myCursor.fetchall()
        row_count = self.myCursor.rowcount ######
        if(row_count == 1):
            return True
        
    def __del__(self):
        self.myCursor.close()
        self.myCursor.close()

class SwapGGInterface():
    def __init__(self) -> None:
        self.url = "https://market-ws.swap.gg/"
        self.marketUrl = "https://market-api.swap.gg"
        self.socket = socketio.Client().connect('https://market-ws.swap.gg/')

    def getWebsocketToken(self, session):
        url = 'https://market-api.swap.gg/v1/user/websocket'
        headers = {
            'Authorization': os.getenv('SWAPGG_API_KEY')
        }
        response = session.get(url=url, headers = headers)
        data = response.json()
        if data['status'] == 'OK':
            return data['result']['token']

    def sendScreenshot(self, session, inspectLink):
        url = f"{self.marketUrl}/v1/screenshot"
        data = {
            "inspectLink": inspectLink
        }
        headers = {
            'Content-type': 'application/json',
            'Authorization': os.getenv('SWAPGG_API_KEY')
        }
        session.post(url=url, json=data, headers=headers)

class CsItem():
    def __init__(self, assetId, marketHashName):
        self.assetId = assetId
        self.marketHashName = marketHashName

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

            #nie ma return ponieważ mogą dla klucze pojawić się w nazwie
            for key, value in toShorten.items():
                if key in self.marketHashName:
                    self.marketHashNameShorter = self.marketHashName.replace(key, value).replace(' | ',' ')
                
    def getInspectLink(self,description):
        self.inspectLink = description['actions'][0]['link'].replace('%owner_steamid%',os.getenv('STEAM_USERID64')).replace(" ", "%20").replace('%assetid%',self.assetId)
                
    def getTradebilityStatus(self, description):
        self.tradeable = 0 if description['tradable'] == 0 else 1

    def getAppliedStickers(self, description):
        stickerResponse = description['descriptions'][-1]['value']
        if "sticker" in stickerResponse:
            cleaner = re.compile('<.*?>') 
            self.stickers = re.sub(cleaner, '', stickerResponse)[9:].split(", ")

#


