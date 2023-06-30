import requests
import os
from dotenv import load_dotenv
from SteamApiCalls import getInvInfo
from Classes import DBConnection, CsItem, SwapGGInterface
from threading import Thread

load_dotenv()

Dbcon = DBConnection()

session = requests.Session()

InventoryData = getInvInfo()

#Sprawdzenie czy zapytanie o zawartości ekwipunku zostało poprawnie wykonane i czy istnieje możliwość zareklamowania go
try:
    if(InventoryData["success"] != 1):
        print("Zapytanie nie zostało zrealizowane! Success != 1")
        quit()
except Exception:
    print("Zbyt wiele zapytań, spróbuj ponownie później!")
    print(InventoryData)
    quit()

if(InventoryData["total_inventory_count"] == 0):
    print("W ekwipunktu nie znaleziono żacnych przedmiotów!")
    quit()

inventoryPacketAssets = InventoryData["assets"]
inventoryPacketDescriptions = InventoryData["descriptions"]

#utworzenie objektu odpowiadającego za komunikacje z serwisem swap gg w odzdzielnym threadzie
SwapGGClient = SwapGGInterface('https://market-ws.swap.gg/', os.getenv('SWAPGG_API_KEY'), session)

def setUpSwapGG(SwapGGClient):
    SwapGGClient.connect()

thread = Thread(target=setUpSwapGG, daemon=True, args=(SwapGGClient,)).start()

readyObjects = []
nonreadyObjects = []
#Niestety kolejność przedmiotów w assets i descriptions nie musi być ze sobą powiązana dlatego algorytm ma złożoność kwadratową
correctItemTypes = ["Rifle", "Pistol", "SMG", "Sniper Rifle", "Gloves", "Knife", "Shotgun", "Machinegun"]
for asset in inventoryPacketAssets:
    for description in inventoryPacketDescriptions:
        if (asset['classid'] == description['classid'] and asset['instanceid'] == description['instanceid']):
            itemType = description["tags"][0]["localized_tag_name"]
            if itemType in correctItemTypes: #sprawdzenie czy przedmiot należy do przedmiotów które można zareklamować

                if Dbcon.checkForExistingRecords(asset['assetid']):
                    print("CongetAppliedStickerstinue")
                    continue

                CsWeapon = CsItem(asset['assetid'], description['market_hash_name'], os.getenv('STEAM_USERID64'))
                #tworzy specjalny wariant nazwy ułatwiający reklame na różnych platformach społecznościowych
                CsWeapon.getMarketHashNameShorter()
                #tworzy link potrzebny do obejrzenia broni
                CsWeapon.getInspectLink(description)
                #sprawdza czy przedmiot jest gotowy na wymiane
                CsWeapon.getTradebilityStatus(description)
                #wykrywa wszystkie naklejki naklejone na broń i przechowuje je w liście
                CsWeapon.getAppliedStickers(description)
                #wysyła zapytanie o screenshot, reklama jest możliwa dopiero gdy wszystkie przedmioty są gotowe stąd ten wybór
                CsWeapon = SwapGGClient.createScreenshot(CsWeapon)

                print(f"{CsWeapon.marketHashName} - {CsWeapon.screenshotLink}")
            
                


                

            
    





