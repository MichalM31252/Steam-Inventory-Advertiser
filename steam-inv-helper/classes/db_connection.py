import mysql.connector

class DbConnection():
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="", database="przedmioty_cs")
        self.my_cursor = self.con.cursor(buffered=True)

    # checks if a record with the given assetId exists in the database
    def check_for_existing_records(self, assetId):
        self.my_cursor.execute("SELECT assetId, COUNT(*) FROM useritems WHERE assetId = %s GROUP BY assetId", (assetId,)) ######
        self.my_cursor.fetchall()
        row_count = self.my_cursor.rowcount ######
        return row_count == 1