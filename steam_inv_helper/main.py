import config
import os
import asyncio
from dotenv import load_dotenv
from threading import Thread
from classes.cs_item import CSItem
from classes.db_connection import DbConnection
from classes.swapgg_interface import SwapGGInterface
from classes.steam_interface import SteamInterface


async def main():
    Dbcon = DbConnection()
    # next time make a string that has all the data from the inv and make it a backup to test the program once you get
    # rate limited so you don't waste multiple hours waiting until you get access to the service
    InventoryData = SteamInterface.get_inv_info(config.STEAM_USERID64)

    # dirname = os.path.dirname(__file__)
    # # 1-3 different files for example_data
    # filename = os.path.join(dirname, "example_data/example_inventory_data_1.json")
    # with open(filename, "r", encoding="utf8") as f:
    #     InventoryData = json.load(f)

    # checks if the request was a success
    try:
        if InventoryData["success"] != 1:
            print("Request was not realised! Success != 1")
            quit()
    except Exception:
        print("Too many requests, try again later!")
        quit()

    if InventoryData["total_inventory_count"] == 0:
        print("There aren't any items in your inventory!")
        quit()

    inventory_packet_assets = InventoryData["assets"]
    inventory_packet_descriptions = InventoryData["descriptions"]

    # create an object which is responsible for communicating with the swappgg api service
    load_dotenv()
    SwapGGClient = SwapGGInterface(
        "https://market-ws.swap.gg/", os.getenv("SWAPGG_API_KEY")
    )

    def set_up_swapgg(SwapGGClient):
        SwapGGClient.connect()

    Thread(target=set_up_swapgg, daemon=True, args=(SwapGGClient,)).start()

    asset_id_list_to_delete, placeholders = Dbcon.get_asset_id_list_to_delete(
        inventory_packet_assets
    )

    Dbcon.delete_items("items", asset_id_list_to_delete, placeholders)
    Dbcon.delete_items("applied_stickers", asset_id_list_to_delete, placeholders)

    # unfortunetly the order of items in assets and descriptions don't always correspond with eachother
    # place this where constants are stored
    correct_item_types = config.CORRECT_ITEM_TYPES
    for asset in inventory_packet_assets:
        for description in inventory_packet_descriptions:
            if (
                asset["classid"] == description["classid"]
                and asset["instanceid"] == description["instanceid"]
            ):
                item_type = description["tags"][0]["localized_tag_name"]
                if (
                    item_type in correct_item_types
                ):  # checks if an item is worth advertising
                    if Dbcon.check_for_existing_records(asset["assetid"]):
                        continue

                    CSWeapon = CSItem(
                        asset["assetid"],
                        description["name"],
                        str(description["descriptions"][0]["value"][10:]),
                        os.getenv("STEAM_USERID64"),
                    )

                    # sets a special shortened variant of items exterior to make advertising easier
                    await CSWeapon.set_shorter_exterior()
                    # sets a special link which is needed to inspect the item as a property
                    await CSWeapon.set_inspect_link(description)
                    # checks if item is tradeable and adds a property based on that info
                    await CSWeapon.set_tradebility_status(description)

                    # create an asynchronus for loop
                    # there already needs to be an event listener in this part of the code

                    swapgg_response = SwapGGClient.fetch_screenshot_info(CSWeapon)
                    if SwapGGClient.get_screenshot_status(swapgg_response):
                        CSWeapon.set_item_float(swapgg_response)
                        CSWeapon.set_screenshot_link(swapgg_response)
                    else:
                        SwapGGClient.wait_for_screenshot()
                        swapgg_response = SwapGGClient.fetch_screenshot_info(CSWeapon)
                        # function that waits untill the screenshot is completed
                        # function that gets swapgg response again
                        # set the object here again

                    await CSWeapon.set_applied_stickers(swapgg_response)
                    # adds the item to the database
                    Dbcon.add_new_item(CSWeapon)
                    # adds the stickers of the item to the database
                    Dbcon.add_applied_stickers(CSWeapon)


# add an asynchronic for loop
# make getting the screenshot asynchronic

if __name__ == "__main__":
    asyncio.run(main())
