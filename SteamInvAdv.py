import requests
import time
import datetime
import praw
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector
from SteamApiCalls import getInvInfo

session = requests.Session()

InventoryData = getInvInfo()

#Sprawdzenie czy zapytanie o zawartości ekwipunku zostało poprawnie wykonane i czy istnieje możliwość zareklamowania go
try:
    if(InventoryData["success"] != 1):
        print("Zapytanie nie zostało zrealizowane! Success != 1")
        quit()
except Exception:
    print("Zbyt wiele zapytań, spróbuj ponownie później!")

if(InventoryData["total_inventory_count"] == 0):
    print("W ekwipunktu nie znaleziono żacnych przedmiotów!")
    quit()

inventoryPacketAssets = InventoryData["assets"]
inventoryPacketDescriptions = InventoryData["descriptions"]

#Niestety kolejność przedmiotów w assets i descriptions nie musi być ze sobą powiązana dlatego algorytm ma złożoność kwadratową

numberOfAssets = len(inventoryPacketAssets)

i, j = 0, 0
#zastosowano while ponieważ lista elementów zmienia się dynamicznie a range w pętli for jest wyznaczany tylko raz
while i < len(inventoryPacketAssets):
    while j < len(inventoryPacketDescriptions):
        itemType = inventoryPacketDescriptions[j]["tags"][0]["localized_tag_name"]
# sourcery skip: merge-nested-ifs
        if (inventoryPacketAssets[i]['classid'] == inventoryPacketDescriptions[j]['classid'] and inventoryPacketAssets[i]['instanceid'] == inventoryPacketDescriptions[j]['instanceid']):
            if itemType in [
                "Rifle",
                "Pistol",
                "SMG",
                "Sniper Rifle",
                "Gloves",
                "Knife",
                "Shotgun",
                "Machinegun",
            ]:
                print(itemType)
            else:
                inventoryPacketDescriptions.remove(inventoryPacketDescriptions[j])
        j += 1
    i += 1

print(inventoryPacketDescriptions)

            
    





