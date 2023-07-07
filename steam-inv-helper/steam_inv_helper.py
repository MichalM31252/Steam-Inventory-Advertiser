import requests
import os
from dotenv import load_dotenv
from threading import Thread
from classes.cs_item import CsItem
from classes.db_connection import DbConnection
from classes.swapgg_interface import SwapGGInterface
from classes.steam_interface import SteamInterface

def main():

    load_dotenv()
    Dbcon = DbConnection()
    InventoryData = SteamInterface.get_inv_info()

    #checks if the request was a success
    try:
        if(InventoryData["success"] != 1):
            print("Request was not realised! Success != 1")
            quit()
    except Exception:
        print("Too many requests, try again later!")
        print(InventoryData)
        quit()

    if(InventoryData["total_inventory_count"] == 0):
        print("There aren't any items in your inventory!")
        quit()

    inventory_packet_assets = InventoryData["assets"]
    inventory_packet_descriptions = InventoryData["descriptions"]

    #create an object which is responsible for communicating with the swappgg api service
    SwapGGClient = SwapGGInterface('https://market-ws.swap.gg/', os.getenv('SWAPGG_API_KEY'))

    def set_up_swapgg(SwapGGClient):
        SwapGGClient.connect()

    Thread(target=set_up_swapgg, daemon=True, args=(SwapGGClient,)).start()

    #unfortunetly the order of items in assets and descriptions don't always correspond with eachother
    correct_item_types = ["Rifle", "Pistol", "SMG", "Sniper Rifle", "Gloves", "Knife", "Shotgun", "Machinegun"]
    for asset in inventory_packet_assets:
        for description in inventory_packet_descriptions:
            if (asset['classid'] == description['classid'] and asset['instanceid'] == description['instanceid']):
                item_type = description["tags"][0]["localized_tag_name"]
                if item_type in correct_item_types: #checks if an item is worth advertising

                    if Dbcon.check_for_existing_records(asset['assetid']):
                        continue

                    CsWeapon = CsItem(asset['assetid'], description['name'], str(description['descriptions'][0]['value'][10:]), os.getenv('STEAM_USERID64'))
                    # sets a special shortened variant of items name to make advertising on different websites easier
                    CsWeapon.set_shorter_name()
                    # sets a special shortened variant of items exterior to make advertising easier
                    CsWeapon.set_shorter_exterior()
                    # sets a special link which is needed to inspect the item as a property
                    CsWeapon.set_inspect_link(description)
                    # checks if item is tradeable and adds a property based on that info
                    CsWeapon.set_tradebility_status(description)
                    # detects every applied sticker and adds it to a list as a property
                    CsWeapon.set_applied_stickers(description)
                    # generates a screenshot and float data of the item 
                    CsWeapon = SwapGGClient.generate_screenshot(CsWeapon)

                    Dbcon.add_new_item(CsWeapon)
                
                    


                

            
    





