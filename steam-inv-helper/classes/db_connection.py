import mysql.connector

class DbConnection():
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="", database="items_cs")
        self.my_cursor = self.con.cursor(buffered=True)

    # checks if a record with the given assetId exists in the database
    def check_for_existing_records(self, assetId):
        self.my_cursor.execute("SELECT asset_id, COUNT(*) FROM items WHERE asset_id = %s GROUP BY asset_id", (assetId,)) ######
        self.my_cursor.fetchall()
        row_count = self.my_cursor.rowcount ######
        return row_count == 1
    
    def add_new_item(self, CsItem):
        properties = (CsItem.asset_id, CsItem.name, CsItem.inspect_link, CsItem.exterior, CsItem.item_float, CsItem.screenshot_link, CsItem.tradeable)
        self.my_cursor.execute("INSERT INTO items (asset_id, name, inspect_link, exterior, item_float, screenshot_link, tradeable) VALUES (%s, %s, %s, %s, %s, %s, %s)", properties)
        self.con.commit()
