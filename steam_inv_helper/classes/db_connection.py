import mysql.connector


class DbConnection:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost", user="root", password="", database="items_cs"
        )
        self.my_cursor = self.con.cursor(buffered=True)

    # checks if a record with the given assetId exists in the database
    def check_for_existing_records(self, asset_id) -> int:
        self.my_cursor.execute(
            "SELECT asset_id, COUNT(*) FROM items WHERE asset_id = %s GROUP BY asset_id",
            (asset_id,),
        )  ######
        self.my_cursor.fetchall()
        row_count = self.my_cursor.rowcount  ######
        return row_count == 1

    def add_new_item(self, CsItem) -> None:
        properties = (
            CsItem.asset_id,
            CsItem.name,
            CsItem.inspect_link,
            CsItem.exterior,
            CsItem.item_float,
            CsItem.screenshot_link,
            CsItem.tradeable,
        )
        self.my_cursor.execute(
            "INSERT INTO items (asset_id, name, inspect_link, exterior, item_float, screenshot_link, tradeable) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            properties,
        )
        self.con.commit()

    def add_applied_stickers(self, CsItem) -> None:
        properties = (
            CsItem.asset_id,
            CsItem.stickers[0],
            CsItem.stickers[1],
            CsItem.stickers[2],
            CsItem.stickers[3],
            CsItem.stickers[4],
        )
        self.my_cursor.execute(
            "INSERT INTO applied_stickers (asset_id, sticker_1, sticker_2, sticker_3, sticker_4, sticker_5) VALUES (%s, %s, %s, %s, %s, %s)",
            properties,
        )
        self.con.commit()

    def get_asset_id_list_to_delete(self, inventory_packet_assets) -> tuple(list, str):
        asset_id_list_to_delete = [
            element["assetid"] for element in inventory_packet_assets
        ]
        placeholder = "%s"
        placeholders = ", ".join(placeholder for _ in asset_id_list_to_delete)
        return asset_id_list_to_delete, placeholders

    def delete_items(self, table_name, asset_id_list_to_delete, placeholders) -> None:
        query = f"DELETE FROM {table_name} WHERE asset_id NOT IN ({placeholders})"
        self.my_cursor.execute(query, asset_id_list_to_delete)
        self.con.commit()
