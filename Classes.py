import mysql.connector
import os
from dotenv import load_dotenv
import re
import asyncio
import socketio
import requests
import threading
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

class SwapGGInterface:
    def __init__(self, url, authorizationToken, session):
        self.socket = socketio.Client()
        self.url = url
        self.authorizationToken = authorizationToken
        self.session = session
        self.screenshot_ready = False
        self.currentItem = None

        self.socket.on('screenshot:ready', self.onScreenshotReady)

    def disconnect(self):
        self.socket.disconnect()

    def onScreenshotReady(self, data):
        if hasattr(self.currentItem, "inspectLink") and data['inspectLink'] == self.currentItem.inspectLink:
            self.screenshot_ready = True

    def waitForScreenshot(self, CsWeapon):
        threading.Thread(target=self.socket).start()
        
        # jest to jedyne rozwiązanie które nie wykorzystuje 90% procesora
        while self.screenshot_ready == False:
            time.sleep(1)
        return CsWeapon

    def connect(self):
        self.socket.connect(self.url)

    def createScreenshot(self, CsWeapon):
        self.currentItem = CsWeapon
        url = "https://market-api.swap.gg/v1/screenshot"
        data = {
            "inspectLink": CsWeapon.inspectLink.replace("%20", " "),
        }
        headers = {
            'Content-type': 'application/json',
            'Authorization': self.authorizationToken
        }
        r = self.session.post(url=url, json=data, headers=headers)
        if r.status_code == 200:
            if r.json()['result']['state'] == 'COMPLETED':
                CsWeapon.screenshotLink, CsWeapon.item_float = r.json()['result']['imageLink'], str(r.json()['result']["itemInfo"]["floatvalue"])[:9]
            elif r.json()['result']['state'] == 'IN_QUEUE':
                #cekaj aż w odpowiedzi z websocketa pojawi się odpowiedni inspectlink
                CsWeapon = self.waitForScreenshot(self.currentItem)
            elif r.json()['result']['state'] in ['FAILED', 'ERROR']:
                raise Exception("Wystąpił błąd podczas tworzenia screenshota")
        self.currentItem = None
        return CsWeapon

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

            #nie ma return ponieważ może się pojawić kilka kluczy w nazwie
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
