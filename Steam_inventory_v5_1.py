import requests
import time
import datetime
import praw
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector

#patch notes
# - liczenie czy title nie przekracza 300 znaków
# - usuwanie przedmiotów z bazy danych jeżeli nie ma ich w ekwipunku podczas wymiany
# - naprawienie reklamy na steam z naklejkami 
# - usunięcie niepotrzebnych spacji w reklamie steam
# - usunięcie niepotrzebnych bibliotek 
# - dodanie sprawdzania warunku czy przedmiot jest wystarczająco drogi
# - dodanie limitów do reklam steam i reddit

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="przedmioty_cs"
)

mycursor = mydb.cursor(buffered=True)

session = requests.Session()

def check_expensive():
    pom = 0
    mycursor.execute("SELECT items_with_stickers.has_expensive_stickers, stickers_applied.sticker_1, stickers_applied.sticker_2, stickers_applied.sticker_3, stickers_applied.sticker_4, stickers_applied.sticker_5, items_with_stickers.item_id FROM items_with_stickers INNER JOIN stickers_applied ON items_with_stickers.item_id = stickers_applied.item_id WHERE items_with_stickers.has_expensive_stickers = 0",) ############
    myresult = mycursor.fetchall() 
    mycursor.execute("SELECT name from stickers",) ############
    stickers_exp = mycursor.fetchall() 
    for element in myresult:
        for sticker in stickers_exp:
            for i in range(1,6):
                if element[i] in sticker:
                    pom += 1
        mycursor.execute("UPDATE items_with_stickers SET `has_expensive_stickers` = %s WHERE `item_id` = %s", (pom,element[6],))
        mydb.commit()
        break

def check_many():
    many = False
    mycursor.execute("SELECT `market_hash_name` FROM items WHERE price > 1 AND tradeable = 1 ORDER BY price ASC",)
    myresult = mycursor.fetchall() 
    print(myresult)
    print(set(myresult))
    if(len(myresult) != len(set(myresult))):
        many = True
        print("many = True")
    return many

def delete_gone():
    mycursor.execute("SELECT `item_id` FROM items",)
    myresult = mycursor.fetchall() 
    for element in myresult:
        if element not in id_list:
            mycursor.execute("DELETE FROM items WHERE item_id = %s", element)
            mydb.commit()

    mycursor.execute("SELECT `item_id` FROM items_with_stickers",)
    myresult = mycursor.fetchall() 
    for element in myresult:
        if element not in id_list:
            mycursor.execute("DELETE FROM items_with_stickers WHERE item_id = %s", element)
            mydb.commit()

def update_and_find():
    global normal_guns
    stickered_guns = False
    mycursor.execute("SELECT `item_id`,`tradeable`,`tradeable_date`, `price` FROM items",)
    myresult = mycursor.fetchall()
    teraz = datetime.datetime.now().replace(microsecond=0)
    value = None
    pom1 = 0
    pom2 = 0
    for element in myresult:
        if(element[2] != None):
            if(element[2] <= teraz):
                mycursor.execute("UPDATE items SET `tradeable` = 1, `tradeable_date` = %s WHERE `item_id` = %s", (value,element[0],))
                mydb.commit()
        if element[1] == 1 and element[3] >= 3:
            pom1 += 1
        elif element[3] >= 45:
            normal_guns = True
        if pom1 >= 2:
            normal_guns = True

    mycursor.execute("SELECT `item_id`,`tradeable`,`tradeable_date`, `price`, `has_expensive_stickers` FROM items_with_stickers",)
    myresult = mycursor.fetchall()
    print(myresult)
    teraz = datetime.datetime.now().replace(microsecond=0)
    value = None
    print(myresult)
    for element in myresult:
        if(element[2] != None):
            if(element[2] <= teraz):
                mycursor.execute("UPDATE items_with_stickers SET `tradeable` = 1, `tradeable_date` = %s WHERE `item_id` = %s", (value,element[0],))
                mydb.commit()
        elif element[1] == 1 and element[3] > 3:
            if element[4] >= 1:
                pom2 += element[4] 
                if pom2 >= 2:
                    stickered_guns = True
            if element[1] == 1 and element[3] > 45:
                normal_guns = True
            else:
                pom1 += 1  
                if pom1 >= 2:
                    normal_guns = True

    return normal_guns, stickered_guns

def get_title_reddit(Want_reddit, limit, limit_title):
    title_reddit = ""
    title_string = ""
    pomx = 0
    x = 0
    y = 0
    pom = True
    mycursor.execute("SELECT market_hash_name_shorter, count(*) as name_count, price from items WHERE tradeable = 1 GROUP BY market_hash_name having name_count = 1 UNION ALL SELECT market_hash_name_shorter, count(*) as name_count, price from items_with_stickers WHERE tradeable = 1 AND has_expensive_stickers = 0 GROUP BY market_hash_name having name_count = 1 ORDER BY price DESC")
    myresult = mycursor.fetchall() 
    print(myresult)
    if myresult:
        for xyz in myresult:
            print(xyz[0]) #market_hash_name_shorter
            print(xyz[1]) #name_count
            print(xyz[2]) #price
            print("")

            print("Limit: ",limit)
            if xyz[2] >= limit:
                y += xyz[2]
                x += 1

        print()
        print("limit: ",limit)
        print("x: ",x)
        print("y: ",y)
        print()

        if x > 1:
            Have = str(x) + " items worth around: " + str(y) + "$ "
        if x == 1:
            Have = str(x) + " item worth around: " + str(y) + "$ "

        for xyz in myresult:
            print(xyz[0]) #market_hash_name_shorter
            print(xyz[1]) #name_count
            print(xyz[2]) #price
            print("")

            print("Limit: ",limit)
            if xyz[2] >= limit:
                pomx += 1
                pom_text = ""

                if pom == False:
                    if xyz[1] == 1:
                        pom_text = ", " + str(xyz[0])
                    else:
                        pom_text = ", " + str(xyz[1]) + "x " + str(xyz[0])
                if pom == True:
                    pom = False
                    if xyz[1] == 1:
                        pom_text = str(xyz[0])
                    else:
                        pom_text = str(xyz[1]) + "x " + str(xyz[0])
                
                if pomx < x:
                    pomoc = ["[H] ", Have, "(", title_string ,")", " [W] ", Want_reddit]
                if pomx == x:
                    pomoc = ["[H] ", Have, "(", title_string ,")", " [W] ", Want_reddit]

                a = len(''.join(pomoc))
                if pomx < x:
                    if(a + 5 + len(pom_text) <= limit_title): 
                        title_string += pom_text
                    else:
                        break
                if pomx == x:
                    if(a + len(pom_text) + 1 <= limit_title): 
                        title_string += pom_text
                    else:
                        break
            
        if pomx < x:
            title_reddit = "[H] " + Have + "(" + title_string + " etc." + ")" + " [W] " + Want_reddit
        if pomx == x:
            title_reddit = "[H] " + Have + "(" + title_string + ")" + " [W] " + Want_reddit

        return title_reddit, x, y
    else:
        print("Niestety nie ma żadnych przedmiotów które można zareklamować na reddicie")

def adv_main_reddit(limit, subreddit_limit, many):

    if(many == True):
        reddit_text = "Amount | Market Name | Float | Screenshot | Inspectlink | \n :--|:--:|:--:|:--:|--: \n"
    if(many == False):
        reddit_text = "Market Name | Float | Screenshot | Inspectlink | \n :--|:--:|:--:|:--:|--: \n"
    
    global normal_guns
    mycursor.execute("SELECT market_hash_name_short, market_hash_name_shorter, inspect_link, item_float, screenshot, price, count(*) as name_count from items WHERE tradeable = 1 GROUP BY market_hash_name having name_count = 1 UNION ALL SELECT market_hash_name_short, market_hash_name_shorter, inspect_link, item_float, screenshot, price, count(*) as name_count from items_with_stickers WHERE tradeable = 1 AND has_expensive_stickers = 0 GROUP BY market_hash_name having name_count = 1 ORDER BY price DESC")
    myresult = mycursor.fetchall() 
    if myresult:
        for xyz in myresult:
            print(xyz[0]) #market_hash_name_short
            print(xyz[1]) #market_hash_name_shorter
            print(xyz[2]) #inspect_link
            print(xyz[3]) #item_float
            print(xyz[4]) #screenshot
            print(xyz[5]) #price
            print(xyz[6]) #name_count
            print("")

            add_to_selftext = ""
            pomoc = [reddit_text, buyout, ending, str(xyz[5]), "x | ", xyz[0], " | ", str(xyz[3]), " | [screenshot](", xyz[4], ") | [inspectlink](", xyz[2], ") \n"]
            a = sum(len(i) for i in pomoc)
            if a <= subreddit_limit:
                if xyz[5] >= limit:
                    if(xyz[6] != 1):
                        add_to_selftext += str(xyz[5]) + "x | " + xyz[0] + " | " + str(xyz[3]) + " | [screenshot](" + xyz[4] + ") | [inspectlink](" + xyz[2] + ") \n"
                    if(xyz[6] == 1):
                        add_to_selftext += xyz[0] + " | " + str(xyz[3]) + " | [screenshot](" + xyz[4] + ") | [inspectlink](" + xyz[2] + ") \n"
                    normal_guns = True
            if a > subreddit_limit:
                limit += 0.1
                adv_main_reddit(limit,subreddit_limit)

            reddit_text += add_to_selftext

    return reddit_text

def adv_main_steam_normal(element):
    normal_dod = ""
    if element:
        #print()
        #print(element[0]) #market_hash_name_shorter
        #print(element[1]) #name_count
        #print(element[2]) #price
        #print("")

        if element[1] == 1:
            normal_dod = "[H] " + element[0] + "\n"
        else:
            normal_dod = "[H] " + element[1] + "x " + element[0] + "\n"

    return normal_dod

def adv_main_steam_stickers(stickers_all_exp,element):
    sticker_normal_text_dod = ""
    if element:
        #print(element[0]) #sticker_1
        #print(element[1]) #sticker_2
        #print(element[2]) #sticker_3
        #print(element[3]) #sticker_4
        #print(element[4]) #sticker_5
        #print(element[5]) #market_hash_name_shorter
        #print("")

        sticker_names = []
        first = True
        for n in range(0,5):
            pom = str(element[n])
            if pom != "":
                for element2 in stickers_all_exp:
                    if pom in element2:
                        pom = pom.replace("Katowice","Kato")
                        pom = pom.replace("20","")
                        pom = pom.replace(" | "," ")
                        pom = pom.replace(".com","")
                        if first == True:   
                            sticker_names.append(pom)
                            first = False
                        elif first == False:
                            sticker_names.append(", " + pom)
            else:
                continue
        sticker_names = ''.join(sticker_names) 
        sticker_normal_text_dod = "[H] " + element[5] + " w/ " + sticker_names + "\n"

    return sticker_normal_text_dod

def adv_main_steam_all(myresult_normal,stickers_all_exp,myresult_stickers_applied,steam_group_limit,title_normal):
    
    normal_text = ""
    sticker_normal_text = ""
    selftext_normal = ""

    for element in myresult_normal:
        normal_text += adv_main_steam_normal(element)
    for element in myresult_stickers_applied:
        sticker_normal_text += adv_main_steam_stickers(stickers_all_exp,element)

    if len(normal_text) + len(sticker_normal_text) + len(title_normal) > steam_group_limit:
        if len(myresult_normal) > len(myresult_stickers_applied):
            myresult_normal = myresult_normal[:-1]
            return adv_main_steam_all(myresult_normal,stickers_all_exp,myresult_stickers_applied,steam_group_limit,title_normal)
        elif len(myresult_normal) <= len(myresult_stickers_applied):
            myresult_stickers_applied = myresult_stickers_applied[:-1]
            return adv_main_steam_all(myresult_normal,stickers_all_exp,myresult_stickers_applied,steam_group_limit,title_normal)

    if len(normal_text) + len(sticker_normal_text) + len(title_normal) < steam_group_limit:
        if(normal_text == "" and sticker_normal_text != ""):
            selftext_normal = sticker_normal_text + ending
        if(sticker_normal_text == "" and normal_text != ""):
            selftext_normal = normal_text + ending
        else:
            selftext_normal = normal_text + "\n" + sticker_normal_text + ending      

    return selftext_normal

def advertisment_reddit(title_reddit,selftext_reddit):
    reddit = praw.Reddit(client_id='lIA2AeFihJSYfw',
                        client_secret='F-s_pg3PYM0KDd896dZruXPl1tM',
                        user_agent='my user agent',
                        username='szun3',
                        password='C~HQ6<K84~zb7g(')
                        
    reddit.validate_on_submit = True
    reddit.subreddit('GlobalOffensiveTrade').submit(title=title_reddit, selftext=selftext_reddit) #GlobalOffensiveTrade test
    time.sleep(4)
    print("Reddit post has been created")

def advertisment_discussion_tab(title,selftext):
    try:
        driver.get("https://steamcommunity.com/app/730/tradingforum/")
        time.sleep(random.uniform(5.1, 10.0))
        driver.find_element_by_class_name("responsive_OnClickDismissMenu").click()
        time.sleep(1)
        topic = driver.find_element_by_class_name("forum_topic_input")
        topic.click()
        topic.send_keys(title)
        description = driver.find_element_by_class_name("forumtopic_reply_textarea")
        description.click()
        description.send_keys(selftext)
        button = driver.find_element_by_class_name("btn_green_white_innerfade")
        button.click()
    except:
        print("Wystąpił błąd z publikacją posta w sekcji dyskusji")

def advertisment_steam_groups(title,selftext,url):
    global nick
    try:
        time.sleep(random.uniform(5.1, 8.0))
        driver.get(url)
        comments_other = driver.find_elements_by_tag_name("bdi")
        for element in comments_other:
            element = element.get_attribute('innerHTML')
            if(element == nick):
                return 
        comment_area = driver.find_element_by_class_name("commentthread_textarea")
        comment_area.click()
        comment_area.send_keys(title,selftext)
        submit = driver.find_element_by_class_name("btn_green_white_innerfade")
        submit.click()
    except:
        print("Wystąpił błąd w linijce z url: "+url)

class CSGO_item():
    def __init__(self,item_id,market_hash_name,market_hash_name_short,market_hash_name_shorter,price,inspect_link,sticker_list,sticker_1,sticker_2,sticker_3,sticker_4,sticker_5,has_expensive_stickers,screenshot,screenshot_requestId,item_float,exterior,tradeable,tradeable_date):
        self.item_id = item_id
        self.market_hash_name = market_hash_name
        self.market_hash_name_short = market_hash_name_short
        self.market_hash_name_shorter = market_hash_name_shorter
        self.price = price
        self.inspect_link = inspect_link
        self.sticker_list = sticker_list
        self.sticker_1 = sticker_1
        self.sticker_2 = sticker_2
        self.sticker_3 = sticker_3
        self.sticker_4 = sticker_4
        self.sticker_5 = sticker_5
        self.has_expensive_stickers = has_expensive_stickers
        self.screenshot = screenshot
        self.screenshot_requestId = screenshot_requestId
        self.item_float = item_float
        self.exterior = exterior
        self.tradeable = tradeable
        self.tradeable_date = tradeable_date

    def screenshot_post(self,inspect_link):
        url = "https://market-api.swap.gg/v1/screenshot"
        data = {
            "inspectLink": self.inspect_link.replace("%20", " ")
        } 
        headers = {
            'Content-type': 'application/json',
            'Authorization': '82fd7fee-819a-49d4-af0d-dda2a499eac6' #bardzo możliwe, że to powinno być w auth header
        }
        response_screenshot = session.post(url=url, json=data, headers=headers) # json=data
        if(response_screenshot.json()['status'] == "OK"):
            print(response_screenshot.json())
            if(response_screenshot.json()['result']["state"] == "COMPLETED"):
                self.screenshot = response_screenshot.json()['result']["imageLink"]
                self.item_float = str(response_screenshot.json()['result']["itemInfo"]["floatvalue"])[:9] #usuń pobieranie tylko 8 pierwszych znakow

                stickers = response_screenshot.json()['result']["itemInfo"]["stickers"]
                if stickers:
                    if(len(stickers) >= 1):
                        objekt.sticker_1 = response_screenshot.json()['result']["itemInfo"]["stickers"][0]["name"]
                        if(len(stickers) >= 2):
                            objekt.sticker_2 = response_screenshot.json()['result']["itemInfo"]["stickers"][1]["name"]
                            if(len(stickers) >= 3):
                                objekt.sticker_3 = response_screenshot.json()['result']["itemInfo"]["stickers"][2]["name"]
                                if(len(stickers) >= 4):
                                    objekt.sticker_4 = response_screenshot.json()['result']["itemInfo"]["stickers"][3]["name"]
                                    if(len(stickers) >= 5):
                                        objekt.sticker_5 = response_screenshot.json()['result']["itemInfo"]["stickers"][4]["name"]

                    mycursor.execute("INSERT INTO items_with_stickers (item_id, market_hash_name, market_hash_name_short, market_hash_name_shorter, price, inspect_link, has_expensive_stickers, exterior, item_float, screenshot, tradeable, tradeable_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (objekt.item_id, objekt.market_hash_name, objekt.market_hash_name_short, objekt.market_hash_name_shorter, objekt.price, objekt.inspect_link, objekt.has_expensive_stickers, objekt.exterior, objekt.item_float, objekt.screenshot, objekt.tradeable, objekt.tradeable_date))
                    mydb.commit() 

                    mycursor.execute("INSERT INTO stickers_applied (item_id, sticker_1, sticker_2, sticker_3, sticker_4, sticker_5) VALUES (%s, %s, %s, %s, %s, %s)", (objekt.item_id, objekt.sticker_1, objekt.sticker_2, objekt.sticker_3, objekt.sticker_4, objekt.sticker_5))
                    mydb.commit()

                else:
                    mycursor.execute("INSERT INTO items (item_id, market_hash_name, market_hash_name_short, market_hash_name_shorter, price, inspect_link, exterior, item_float, screenshot, tradeable, tradeable_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (objekt.item_id, objekt.market_hash_name, objekt.market_hash_name_short, objekt.market_hash_name_shorter, objekt.price, objekt.inspect_link, objekt.exterior, objekt.item_float, objekt.screenshot, objekt.tradeable, objekt.tradeable_date))
                    mydb.commit() 

            elif(response_screenshot.json()['result']["state"] == "IN_QUEUE"):
                print("IN_QUEUE \n")
                time.sleep(150)
                self.screenshot_post(inspect_link)
            elif(response_screenshot.json()['result']["state"] == "FAILED"):
                print("FAILED \n")              
            elif(response_screenshot.json()['result']["state"] == "ERROR"):
                print("error")
                time.sleep(300)  #program na discordzie ktory mnie pinguje## #############################################################
                self.screenshot_post(inspect_link)
            time.sleep(3)
val = []
black_list = []
title_list = []
reddit_text = ""
objekty = {}
id_list = []

url = "http://steamcommunity.com/profiles/76561198231636540/inventory/json/730/2"

steamid = 76561198231636540

params = {
    'l': 'english',
    'key': '492EE6A0BD7968AFE46FEC5CCC84666D',
    'steamid': steamid
}    

r = requests.get(url=url, params=params)

paczka_json = r.json()

try:
    success = str(paczka_json["success"])
except TypeError:
    print("Występują problemy z api steama. Spróbuj ponownie poźniej")
    raise SystemExit(0)

if paczka_json["success"] == False:
    print("Występują problemy z api steama. Spróbuj ponownie poźniej")
    raise SystemExit(0)

if not paczka_json["rgInventory"]:
    print("Nie masz żadnych przedmiotów w ekwipunku")
    raise SystemExit(0)

paczka_inv_dict = paczka_json["rgInventory"]

paczka_des_dict = paczka_json["rgDescriptions"]

paczka_inv_list = list(paczka_inv_dict)

paczka_des_list = list(paczka_des_dict)

if(success == "True"): # pokazuje czy poprawnie wykonano zapytanie
    print("Wykonano poprawne zapytanie")
else:
    print("Wykonano niepoprawne zapytanie")  #Zrób tu powiadomienie na telefon
    raise SystemExit(0)

print("\n \n")

nick = "The Rice Dealer"
go = 0
j = 0
i = 0
x = 0
y = 0

normal_guns = False
subreddit_limit = 30000
steam_group_limit = 1000

for element1 in paczka_inv_dict:
    sticker_list = []
    screenshot = "This item is too cheap"
    item_float = "This item is too cheap"
    tradeable_date = ""
    has_expensive_stickers = 0
    price = 0
    sticker_1 = ""
    sticker_2 = ""
    sticker_3 = ""
    sticker_4 = ""
    sticker_5 = ""

    class_id_inv = paczka_inv_dict[element1]['classid']
    instance_id_inv = paczka_inv_dict[element1]['instanceid']
    item_id = paczka_inv_dict[element1]['id']

    for element2 in paczka_des_dict:
        item_type = paczka_des_dict[element2]['tags'][0]['name']
        if(item_type == "Container" or item_type == "Sticker" or item_type == "Agent" or item_type == "Collectible" or item_type == "Tool" or item_type == "Music Kit"):
            continue
            
        if(item_type == "Rifle" or item_type == "Pistol" or item_type == "SMG" or item_type == "Sniper Rifle" or item_type == "Gloves" or item_type == "Knife" or item_type == "Shotgun" or item_type == "Machinegun"):
            class_id_des = paczka_des_dict[element2]['classid']
            instance_id_des = paczka_des_dict[element2]['instanceid']

            if(class_id_inv == class_id_des and instance_id_inv == instance_id_des):

                id_list.append(tuple((item_id,)))

                name = paczka_des_dict[element2]['name']
                market_hash_name = paczka_des_dict[element2]['market_hash_name']
                market_hash_name_short = market_hash_name.replace(' | ',' ')

                mycursor.execute("SELECT item_id, COUNT(*) FROM items WHERE item_id = %s GROUP BY item_id", (item_id,)) ######
                mycursor.fetchall()
                row_count = mycursor.rowcount ######
                if(row_count == 1):
                    print("continue")
                    continue

                mycursor.execute("SELECT item_id, COUNT(*) FROM items_with_stickers WHERE item_id = %s GROUP BY item_id", (item_id,)) ######
                mycursor.fetchall()
                row_count = mycursor.rowcount ######
                if(row_count == 1):
                    print("continue")
                    continue
                
                if(market_hash_name not in black_list):
                    market_hash_name_shorter = market_hash_name_short.replace("(Factory New)","FN")
                    market_hash_name_shorter = market_hash_name_shorter.replace("(Minimal Wear)","MW")
                    market_hash_name_shorter = market_hash_name_shorter.replace("(Field-Tested)","FT")
                    market_hash_name_shorter = market_hash_name_shorter.replace("(Well-Worn)","WW")
                    market_hash_name_shorter = market_hash_name_shorter.replace("(Battle-Scarred)","BS")
                    market_hash_name_shorter = market_hash_name_shorter.replace("StatTrak\u2122","ST")

                    inspectlink_alfa = paczka_des_dict[element2]['actions'][0]['link']
                    inspectlink_beta = inspectlink_alfa.replace('%owner_steamid%',str(steamid))
                    inspectlink_gamma = inspectlink_beta.replace(" ", "%20")
                    inspect_link = inspectlink_gamma.replace('%assetid%',str(element1))

                    tradeable = paczka_des_dict[element2]['tradable'] 
                    if('cache_expiration' in paczka_des_dict[element2]):
                        cache_expiration = paczka_des_dict[element2]['cache_expiration']
                        tradeable_date = datetime.datetime.strptime(cache_expiration,"%Y-%m-%dT%H:%M:%SZ")

                    if('cache_expiration' not in paczka_des_dict[element2]):
                        tradeable = paczka_des_dict[element2]['tradable']  
                        tradeable_date = ""             
                    
                    descriptions_length = len(paczka_des_dict[element2]['descriptions'])
                    sticker_response = paczka_des_dict[element2]['descriptions'][descriptions_length-1]['value'] #to jest string napewno
                    exterior = paczka_des_dict[element2]['tags'][5]['name']

                    mycursor.execute("SELECT name FROM stickers",)
                    myresult = mycursor.fetchall() 
                    for lista in myresult:
                        for element in lista:
                            if(element in sticker_response):
                                sticker_list.append(element)
                                has_expensive_stickers += 1
                    
                    marketable = paczka_des_dict[element2]['marketable']
                    if(marketable==1):
                        time.sleep(3)
                        url = "https://steamcommunity.com/market/priceoverview/"
                        params = {
                            'currency': 1,
                            'appid': 730,
                            'market_hash_name': market_hash_name
                        } 
                        s = requests.get(url=url, params=params)
                        cena_json = s.json()
                        if(cena_json['success'] == True):
                            try:
                                cena = cena_json["median_price"].replace("$","")
                                price = round(float(cena),2)
                            except:
                                cena = cena_json["lowest_price"].replace("$","")
                                price = round(float(cena),2)
                            
                        elif(cena_json['success'] == False):
                            print("Nie udalo sie pobrac ceny")
                            pass
                            
                        time.sleep(4)

                        screenshot_requestId = ""
                        if(market_hash_name in objekty.keys()):
                            objekty[market_hash_name].append(CSGO_item(item_id, market_hash_name, market_hash_name_short, market_hash_name_shorter, price, inspect_link, sticker_list, sticker_1, sticker_2, sticker_3, sticker_4, sticker_5, has_expensive_stickers, screenshot, screenshot_requestId, item_float, exterior, tradeable, tradeable_date))
                            break
                        objekty[market_hash_name] = [CSGO_item(item_id, market_hash_name, market_hash_name_short, market_hash_name_shorter, price, inspect_link, sticker_list, sticker_1, sticker_2, sticker_3, sticker_4, sticker_5, has_expensive_stickers, screenshot, screenshot_requestId, item_float, exterior, tradeable, tradeable_date)]         

for name, lista_obj in objekty.items():
    for objekt in lista_obj:
        objekt.screenshot_post(objekt.inspect_link)

delete_gone()

check_expensive()

normal_guns, stickered_guns = update_and_find()

bo = "HellRaisers (Holo) | Katowice 2014 on AWP Redline MW Second Best Pos"
Want_normal = "Katowice 2014 Normal/Holo, Katowice 2015, Crown, Howling Dawn Stickers Applied On Guns "
Want_reddit = Want_normal + "B/O " + bo #nie zmieniaj
ending = "\nYou can add me if you want I don't bite :D \n \ntradelink: https://steamcommunity.com/tradeoffer/new/?partner=271370812&token=eHAwcnd9" #nie zmieniaj
title_normal = "[W] "+ Want_normal + "\n \n"

if(normal_guns == True):
    buyout = "\n \n B/O " + bo + "\n \n" #dodać program
    selftext_reddit = ""
    many = check_many()
    title_reddit, x, y = get_title_reddit(Want_reddit, 3, 300)
    print(title_reddit)
    reddit_text = adv_main_reddit(3, 30000, many)
    selftext_reddit = buyout + reddit_text + ending + "\n \nThe prices are negotiable"#nie zmieniaj
    # advertisment_reddit(title_reddit,selftext_reddit)
    time.sleep(5)

if(stickered_guns > 0 or normal_guns == True):
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument("--start-maximized")
    options.add_argument(r"user-data-dir=C:\Users\Michal\AppData\Local\Google\Chrome\User Data\Profile 1")
    driver = webdriver.Chrome(executable_path=r'C:\Users\Michal\Desktop\projekty\chromedriver.exe', options = options)

    mycursor.execute("SELECT market_hash_name_shorter, count(market_hash_name) as name_count, price from items WHERE tradeable = 1 AND price >= 3 GROUP BY market_hash_name having name_count = 1 UNION ALL SELECT market_hash_name_shorter, count(*) as name_count, price from items_with_stickers WHERE tradeable = 1 AND has_expensive_stickers = 0 AND price >= 3 GROUP BY market_hash_name having name_count = 1 ORDER BY price DESC",)
    myresult_normal = mycursor.fetchall() 
    mycursor.execute("SELECT name FROM stickers",)
    stickers_all_exp = mycursor.fetchall() 
    mycursor.execute("SELECT stickers_applied.sticker_1, stickers_applied.sticker_2, stickers_applied.sticker_3, stickers_applied.sticker_4, stickers_applied.sticker_5, items_with_stickers.market_hash_name_shorter FROM stickers_applied JOIN items_with_stickers ON (stickers_applied.item_id = items_with_stickers.item_id AND items_with_stickers.has_expensive_stickers > 0 AND items_with_stickers.tradeable = 1) ORDER BY items_with_stickers.has_expensive_stickers DESC",)
    myresult_stickers_applied = mycursor.fetchall() 

    selftext_normal = adv_main_steam_all(myresult_normal,stickers_all_exp,myresult_stickers_applied,steam_group_limit,title_normal)

    advertisment_discussion_tab(title_normal,selftext_normal)
    time.sleep(5)

    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/tradecenter2016")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CSGOTrader")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/csgolounge")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/katowicestickerclub")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/csmoneytrade")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/katowice2014stickercollectors")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/ibuypower")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/Original_Traders_Group")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/SGTTB")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CykaKatowice")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/TeamKato14")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/Katowice2014")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CsDealsOfficial")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/freeetrade")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CSGOTRADEme")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/BibanatorCommunity")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/1BUYPOWER")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/polandgotrade")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/Trading-Lounge")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/gergelyszabotrading")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/WorldTradersGroup")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/theglobalparadise")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/steamanalyst")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/iTraders")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/TradingRevolution")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CSGOFGT")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/SkinProfit")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/OpiumPulsesTrading")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/csgointernationaltradings")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/csgotradeherre")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CSGOSellCom")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/LitTrading")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CSGOSkinTradingAndMore")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/casedropeu")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/tradesmart")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/tdm_jesus")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/realCSGO64")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/SkinTrade")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/globaltradeandplay")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/Trade-City")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/LitNetwork")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/csgotradesss")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/community_market")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/csgotradebot")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/rewardsgg")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/titan")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CSGOTradesGroup")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/csgotradeskinscaseWorld")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CSGOTradeHub")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/FACEITcom")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/thetradingmasters")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/TheTradeCenter")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/otrade")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CABUYSELLOfficial")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/csgo_traders")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/csgosum")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/wymieniamy-skiny")
    advertisment_steam_groups(title_normal,selftext_normal,"https://steamcommunity.com/groups/CROWNBOYS")

    driver.quit()