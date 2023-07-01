import requests
import os
from dotenv import load_dotenv
from threading import Thread
from classes.cs_item import CsItem
from classes.db_connection import DBConnection
from classes.swapgg_interface import SwapGGInterface
from classes.steam_interface import SteamInterface

if __name__ == '__main__':

    load_dotenv()

    Dbcon = DBConnection()

    InventoryData = SteamInterface.getInvInfo()

    #checks if the request was a success
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

    #create an object which is responsible for communicating with the swappgg api service
    SwapGGClient = SwapGGInterface('https://market-ws.swap.gg/', os.getenv('SWAPGG_API_KEY'))

    def setUpSwapGG(SwapGGClient):
        SwapGGClient.connect()

    thread = Thread(target=setUpSwapGG, daemon=True, args=(SwapGGClient,)).start()

    readyObjects = []
    nonreadyObjects = []
    #unfortunetly the order of items in assets and descriptions don't always correspond with eachother
    correctItemTypes = ["Rifle", "Pistol", "SMG", "Sniper Rifle", "Gloves", "Knife", "Shotgun", "Machinegun"]
    for asset in inventoryPacketAssets:
        for description in inventoryPacketDescriptions:
            if (asset['classid'] == description['classid'] and asset['instanceid'] == description['instanceid']):
                itemType = description["tags"][0]["localized_tag_name"]
                if itemType in correctItemTypes: #checks if an item is worth advertising

                    if Dbcon.checkForExistingRecords(asset['assetid']):
                        print("CongetAppliedStickerstinue")
                        continue

                    CsWeapon = CsItem(asset['assetid'], description['market_hash_name'], os.getenv('STEAM_USERID64'))
                    #creates a special shortened variant of an items name to make advertising on different websites easier
                    CsWeapon.getMarketHashNameShorter()
                    #sets a special link which is needed to inspect the item as a property
                    CsWeapon.getInspectLink(description)
                    #checks if item is tradeable and adds a property based on that info
                    CsWeapon.getTradebilityStatus(description)
                    #detects every applied sticker and adds it to a list as a property
                    CsWeapon.getAppliedStickers(description)
                    #generates a screenshot and float data of the item 
                    CsWeapon = SwapGGClient.createScreenshot(CsWeapon)

                    print(f"{CsWeapon.marketHashName} - {CsWeapon.screenshotLink}")
                
                    


                

            
    





