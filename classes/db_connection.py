import mysql.connector

class DBConnection():
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="", database="przedmioty_cs")
        self.myCursor = self.con.cursor(buffered=True)

    #sprawdzenie czy informacje o przedmiocie znajdują się w bazie danych
    def checkForExistingRecords(self, assetId):
        self.myCursor.execute("SELECT assetId, COUNT(*) FROM useritems WHERE assetId = %s GROUP BY assetId", (assetId,)) ######
        self.myCursor.fetchall()
        row_count = self.myCursor.rowcount ######
        return row_count == 1