import requests
import time
import datetime
import praw
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SteamApiCalls import getInvInfo
from Classes import DBConnection, CsItem

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

#Niestety kolejność przedmiotów w assets i descriptions nie musi być ze sobą powiązana dlatego algorytm ma złożoność kwadratową

correctItemTypes = ["Rifle", "Pistol", "SMG", "Sniper Rifle", "Gloves", "Knife", "Shotgun", "Machinegun"]
for asset in inventoryPacketAssets:
    for description in inventoryPacketDescriptions:
        if (asset['classid'] == description['classid'] and asset['instanceid'] == description['instanceid']):
            itemType = description["tags"][0]["localized_tag_name"]
            if itemType in correctItemTypes: #sprawdzenie czy przedmiot należy do przedmiotów które można zareklamować

                if Dbcon.checkForExistingRecords(asset['assetid']):
                    print("Continue")
                    continue

                CsWeapon = CsItem(asset['assetid'], description['market_hash_name'], description['actions'][0]['link'])
                CsWeapon.getMarketHashNameShorter()

                print(CsWeapon.inspectlink)
                
            
                


                

            
    





