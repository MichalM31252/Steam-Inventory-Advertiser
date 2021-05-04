import requests
import mysql.connector
from time import sleep

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="przedmioty_cs"
)

mycursor = mydb.cursor(buffered=True)

def get_info():
  all_items_in = []
  prices_url = "https://prices.csgotrader.app/latest/prices_v6.json"
  r = requests.get(prices_url)
  paczka_json = r.json()
  mycursor.execute("SELECT `market_hash_name`, `price` FROM all_items",) ############
  myresult = mycursor.fetchall()
  for element in myresult:
    all_items_in.append(element[0])
  mycursor.execute("SELECT `market_hash_name`, `price` from items",) ############
  myresult2 = mycursor.fetchall()
  mycursor.execute("SELECT `market_hash_name`, `price` from items_with_stickers",) ############
  myresult3 = mycursor.fetchall()
  return paczka_json, myresult, myresult2, myresult3, all_items_in

# def adding_items_to_the_table():
#   prices_url = "https://prices.csgotrader.app/latest/prices_v6.json"
#   r = requests.get(prices_url)
#   paczka_json = r.json()

#   for element in paczka_json:
#     if "|" in element:
#       sql = "INSERT INTO all_items VALUES ("
#       sql += '"'+element+'"'
#       sql += ","+str(paczka_json[element]['steam']['last_7d'])+");"
#       mycursor.execute(sql,)
#       mydb.commit()
#       sleep(0.01)

def update_current_items(paczka_json, myresult2, myresult3):
  for element in myresult2:
    element = element[0]
    if paczka_json[element]['steam']['last_7d'] != "null":
      if element[1] != paczka_json[element]['steam']['last_7d']:
        mycursor.execute("UPDATE items SET `price` = %s WHERE `market_hash_name` = %s;", (paczka_json[element]['steam']['last_7d'],element))
        mydb.commit()

  for element in myresult3:
    element = element[0]
    if paczka_json[element]['steam']['last_7d'] != "null":
      if element[1] != paczka_json[element]['steam']['last_7d']:
        mycursor.execute("UPDATE items_with_stickers SET `price` = %s WHERE `market_hash_name` = %s;", (paczka_json[element]['steam']['last_7d'],element))
        mydb.commit()

def updating_the_value(paczka_json,myresult,all_items_in):
  for element in paczka_json:
    if "|" in element:
      for ele in myresult:
        if element in ele:
          if paczka_json[element]['steam']['last_7d'] != "null":
            if float(paczka_json[element]['steam']['last_7d']) != float(ele[1]):
              mycursor.execute("UPDATE all_items SET `price` = %s WHERE `market_hash_name` = %s;", (paczka_json[element]['steam']['last_7d'],element))
              mydb.commit()
              print("Zmieniono: ",element," cena tego przedmiotu: ",ele[1]," na: ",paczka_json[element]['steam']['last_7d'])
      if element not in all_items_in:
        mycursor.execute("INSERT INTO all_items VALUES (%s, %s) ", (element,paczka_json[element]['steam']['last_7d']))
        mydb.commit()

paczka_json, myresult, myresult2, myresult3, all_items_in = get_info()
updating_the_value(paczka_json, myresult, all_items_in)
update_current_items(paczka_json, myresult2, myresult3)