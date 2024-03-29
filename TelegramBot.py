import requests
import json
import random
import numpy as np
import threading 
class BogdanBot():
    def __init__(self):
        self.u = "https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/getUpdates"

    def get_updates(self,offset=None, timeout=30):
        params = {'timeout': timeout, 'offset': offset}
        self.url = requests.get(self.u, params)
        jsonresponse = json.loads(self.url.text)
        return jsonresponse

    def last_update(self):
        if 'result' in self.get_updates():
            results = self.get_updates()['result']
            if len(results) > 0:
                last_update = results[-1]
            else:
                last_update = None

            return last_update
        else:
            last_update = None
            return last_update
    
    def get_chat_id(self,update):
        if 'message' in update and (update['message']['chat']['type'] == "group" or update['message']['chat']['type'] == "supergroup" or update['message']['chat']['id'] == 462419708):
            chat_id = update['message']['chat']['id']
            return chat_id
        else:
            return None
        if 'edited_message' in update and (update['edited_message']['chat']['type'] == "group" or update['edited_message']['chat']['type'] == "supergroup"):
            chat_id = update['edited_message']['chat']['id']
            return chat_id
        else:
            return None
    def send_mess(self, chat, text): 
        params = {'chat_id': chat, 'text': text}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'sendMessage', params)
        return response
    
    def resend_mess(self, chat, text, reply):  
        params = {'chat_id': chat, 'text': text, 'reply_to_message_id': reply}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'sendMessage', params)
        return response
    def send_mes(self, chat, text):  
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/sendMessage?chat_id={}&text={}".format(chat, text))
        return response
    def send_voice(self, chat, voice, reply):  
        params = {'chat_id': chat, 'voice': voice , 'reply_to_message_id': reply}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'sendVoice', params)
        return response
    def send_sticker(self, chat, sticker, reply):  
        params = {'chat_id': chat, 'sticker': sticker , 'reply_to_message_id': reply}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'sendSticker', params)
        return response
    def send_stick(self, chat, sticker):  
        params = {'chat_id': chat, 'sticker': sticker}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'sendSticker', params)
        return response
    def get_message(self,update):
        if 'message' in update and (update['message']['chat']['type'] == "group" or update['message']['chat']['type'] == "supergroup" or update['message']['chat']['id'] == 462419708):
            if 'text' in update['message']:
                chat_id = update['message']['text']
                return chat_id
            else:
                no = "non"
                return no
        else:
            no = "non"
            return no
        if 'edited_message' in update and (update['edited_message']['chat']['type'] == "group" or update['edited_message']['chat']['type'] == "supergroup"):
            if 'text' in update['edited_message']:
                chat_id = update['edited_message']['text']
                return chat_id
            else:
                no = "non"
                return no
        else:
            no = "non"
            return no
    def get_message_id(self,update):
        if 'message' in update:
            chat_id = update['message']['message_id']
            return chat_id
        if 'edited_message' in update:
            chat_id = update['edited_message']['message_id']
            return chat_id
    def get_username(self, update):
         if 'message' in update:
             if 'username' in update['message']['from']:
                chat_id = update['message']['from']['username']
                name = '@'+ chat_id
                return name
             else:
                 firstn = update['message']['from']['first_name']
                 return firstn
         if 'edited_message' in update:
             if 'username' in update['edited_message']['from']:
                chat_id = update['edited_message']['from']['username']
                name = '@'+ chat_id
                return name
             else:
                 firstn = update['message']['from']['first_name']
                 return firstn
    def get_id(self, update):
         if 'message' in update:
             if 'id' in update['message']['from']:
                chat_id = update['message']['from']['id']
                return chat_id
         if 'edited_message' in update:
             if 'id' in update['edited_message']['from']:
                chat_id = update['edited_message']['from']['id']
                return chat_id
bot = BogdanBot()
rate = np.zeros((0), dtype = [('name', object),('chatid', object),('id', int)])
rate2 = np.zeros((0), dtype = [('id', int),('wins', int),('kills', int),('losing', int), ('money', int)])
r = requests.get("https://write.as/api/posts/1t7486xtsluj3mg4")
objects = json.loads(r.text)['data']['body']
objects1 = []
objects2 = []
c = 0
k = 0
obj = []
for i in objects:
    if i == "|":
        c += 1
        obj.append(i)
        k = 0
        continue
    if k == 0:
        k = 1
        obj.append(i)
        continue
    if i != ' ':
        obj[c] += i
    else:
        c += 1
        k = 0
ok = 0
for j in obj:
    if j == "|":
        ok = 1
        continue
    if ok == 0:
        objects1.append(j)
    else:
        objects2.append(j)
x = 0
y = 0
while x != len(objects1):
    rate = np.insert(rate, len(rate),(objects1[x],objects1[x+1],objects1[x+2]), axis = 0)
    x += 3
    rate2 = np.insert(rate2, len(rate2),(objects2[y],objects2[y+1],objects2[y+2],objects2[y+3], objects2[y+4]), axis = 0)
    y += 5
print(rate)
print(rate2)
def game(chadid, players):
    def update(token, id, **kwargs):
        data = json.dumps(kwargs)
        p = requests.post('https://write.as/api/posts' + "/%s" % id, data=data,
            headers={"Authorization": "Token %s" % token,
                    "Content-Type":"application/json"})
        if p.status_code != 200:
            return "Error in updatePost(): %s" % p.json()["error_msg"]
    def basa_add():
        a = ''
        for i in range(len(rate)):
            a = a + str(rate[i][0]) + " " + str(rate[i][1]) + " " + str(rate[i][2]) + " "
        b = ''
        for i in range(len(rate2)):
            b = b + str(rate2[i][0]) + " " + str(rate2[i][1]) + " " + str(rate2[i][2]) + " " + str(rate2[i][3]) + " "+ str(rate2[i][4]) + " "
        update('54e5b71b-8113-4381-4819-4b6e942e5b25', '1t7486xtsluj3mg4', body = ("{}|{}".format(a,b)))
        return 
    players3 = np.zeros((0), dtype = [('name', object),('role', object),('died', object),('count', int), ('money', int)])
    for p in range(len(players)):
        players3 = np.insert(players3, len(players3),(players[p],None,None,0,0), axis = 0)
    def storonu():
        for p in range(len(players)):
            players3[p][1] = None
        countPlr = []
        for p in range(len(players)):
            countPlr.append(p)
        allReady = 0
        while 1:
            if allReady == len(players):
                break
            randomPlayer = random.choice(countPlr)
            rand = random.randint(1,3)
            def randRole():
                if rand == 1:
                    if np.count_nonzero("Мєнт" == players3['role']) <= np.count_nonzero("Разбойнік" == players3['role']):
                        players3[randomPlayer][1] = "Мєнт"
                    else:
                        players3[randomPlayer][1] = "Разбойнік"
                if rand == 2:
                    if np.count_nonzero("Мєнт" == players3['role']) >= np.count_nonzero("Разбойнік" == players3['role']):
                        players3[randomPlayer][1] = "Разбойнік"
                    else:
                        players3[randomPlayer][1] = "Мєнт"
            randRole()
            if rand == 3:
                if np.count_nonzero("Мер" == players3['role']) == 0:
                    players3[randomPlayer][1] = "Мер"
                else:
                    rand = random.randint(1,2)
                    randRole()
            countPlr.remove(randomPlayer)
            allReady += 1
    storonu()
    while 1 :
        if len(players) != 2:
            if "Мер" in players3[:][1]:
                break
            else:
                storonu()
        else:
            break
    message = ""
    for k in range(len(players)):
        if players3[k][0] != None:
            message += ("{}%20-%20{}%0A".format(players3[k][0], players3[k][1]))
    bot.send_mes(chadid, message)
    countPlayer = []
    for p in range(len(players)):
        countPlayer.append(p)
    lifeMer = 1
    rabstvo = []
    avtoritet = 0
    for l in countPlayer:
        if players3[l][1] == "Разбойнік":
            avtoritet += 1
    avtoritet_changable = avtoritet + 1
    message = ""
    def raund():
        nonlocal message
        def win(hunter, victim, H1, h1, h2, V1, V2, v2, win_g, win_m):
            rep = random.randint(1,5)
            nonlocal message
            if rep == 1:
                message += ("{}%20{}%20знищив%20очко%20{}%20{}%0A%0A".format(H1, hunter, v2, victim))
            if rep == 2:
                message += ("{}%20{}%20розтарабанив%20очко%20{}%20{}%0A%0A".format(H1, hunter, v2, victim))
            if rep == 3:
                message += ("{}%20{}%20кінчив%20в%20штани%20коли%20його%20їбав%20{}%20{}%0A%0A".format(V1, victim, h1, hunter))
            if rep == 4:
                message += ("{}%20{}%20спіткала%20анальна%20кара%20{}%20{}%0A%0A".format(V2, victim, h2, hunter))
            if rep == 5:
                message += ("Ракета%20{}%20{}%20стрімко%20влетіла%20в%20чорну%20диру%20{}%20{}%0A%0A".format(h2, hunter, v2, victim))
            if win_m:
                message += ("{}%20{}%20потрапив%20в%20анальне%20рабство%20до%20{}%20{}%0A".format(V1, victim, h2, hunter))
                message += ("Анальні%20раби%20{}%20{}:%20".format(h2, hunter))
                for k in rabstvo:
                    message += ("{},%20".format(k))
                message = message[:-4]
                message += "%0A%0A"
            if win_g:
                money = []
                potential_money = [5000, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 75000, 100000]
                for l in range(len(Gangster)):
                    money.append(random.choice(potential_money))
                numb = 0
                players3[p][4] += max(money)
                max_money = max(money)
                money.remove(max(money))
                for l in Gangster:
                    if players3[l][0] != players3[p][0]:
                        players3[l][4] += money[numb]
                        numb += 1
                message += ("{}%20{}%20залутав%20з%20мера%20{}$.%20Гроші%20розділені%20між%20разбойніками%0A".format(H1, hunter, str(sum(money)+max_money)))
                for l in Gangster:
                    message += ("{}%20{}%20тепер%20має%20{}$%0A".format(players3[l][1], players3[l][0], players3[l][4]))
                message += "%0A"
        
        def lose(hunter, victim, H1, h1, h2, H3, V1, v1, v2, V3):
            life = random.randint(1,5)
            nonlocal message
            if life == 1:
                message += ("{}%20{}%20промазав%20своїм%20пенісом%20і%20{}%20{}%20зірвався%20та%20втік%0A%0A".format(H1, hunter, v1, victim))
            if life == 2:
                message += ("{}%20{}%20вдалося%20уникнути%20пеніса%20{}%20{}%0A%0A".format(V3, victim, h2, hunter))
            if life == 3:
                message += ("{}%20{}%20не%20вдалося%20впіймати%20{}%20{}%0A%0A".format(H3, hunter, v2, victim))
            if life == 4:
                message += ('{}%20{}%20в%20останній%20момент%20використав%20"стан"%20і%20втік%20від%20{}%20{}%0A%0A'.format(V1, victim, h2, hunter))
            if life == 5:
                message += ("{}%20{}%20в%20останній%20момент%20насрав%20в%20штани%20і%20{}%20{}%20вимушений%20був%20відступити%0A%0A".format(V1, victim, h1, hunter))
        def result():
            for h in range(len(rate)):
                if rate[h][0] == players[p] and rate[h][1] == str(chadid):
                    rate2[h][2] = rate2[h][2] + 1
                if rate[h][0] == players[i] and rate[h][1] == str(chadid):
                    rate2[h][3] = rate2[h][3] + 1
        countPlayer2 = []
        for p in countPlayer:
            countPlayer2.append(p)
        Mer = []
        Police = []
        Gangster = []
        for l in countPlayer:
            if players3[l][1] == "Мер":
                Mer.append(l)
            if players3[l][1] == "Мєнт":
                Police.append(l)
            if players3[l][1] == "Разбойнік":
                Gangster.append(l)
        timer = 10 
        while 1:
            p = None
            i = None
            cho = [1,2,3]
            if not Mer:
                cho.remove(1)
            if not Police:
                cho.remove(2)
            if not Gangster:
                cho.remove(3)
            choice = random.choice(cho)
            choice2 = random.choice(cho)
                
            if choice == 1 :
                p = random.choice(Mer)
            if choice == 2 :
                p = random.choice(Police)
            if choice == 3 :
                p = random.choice(Gangster)
            if choice2 == 1 :
                i = random.choice(Mer)
            if choice2 == 2 :
                i = random.choice(Police)
            if choice2 == 3 :
                i = random.choice(Gangster)
            timer = timer - 1
            nonlocal avtoritet_changable
            if (choice != choice2 and (players3[p][3] == None or players3[p][3] == 0)) or timer == 0:
                timer = 20

                if players3[p][1] == "Мер":
                    if players3[i][1] == "Мєнт":
                        message += ("Мер%20{}%20помітив мєнта%20{}%0A".format(players[p], players[i]))
                        die = random.randint(1,2)
                        if p in countPlayer2:
                            countPlayer2.remove(p)
                        players3[p][3] = 4
                        for c in range(len(players)):
                            if players3[c][3] != 0 and players3[c][3] != None:
                                players3[c][3] = players3[c][3] - 1
                        if die == 1:
                            rand = random.randint(1,avtoritet)
                            rand2 = random.randint(1,avtoritet_changable)
                            if rand <= rand2:
                                rabstvo.append(players3[i][0])
                                win(players[p], players[i], "Мер", "мер", "мера", "Мєнт", "Мєнта", "мєнта", False, True)
                                players3[i][2] = "Died"
                                countPlayer.remove(i)
                                Police.remove(i)
                                if i in countPlayer2:
                                    countPlayer2.remove(i)
                                result()
                            else:
                                message += ("Меру%20{}%20не%20вистачило%20авторитета%20скористатися%20очком%20мєнта%20{}%0A%0A".format(players[p], players[i]))
                        else:
                            lose(players[p], players[i], "Мер", "мер", "мера", "Меру", "Мєнт", "мєнт", "мєнта", "Мєнту")
                if players3[p][1] == "Мєнт":
                    if players3[i][1] == "Разбойнік":
                        message += ("Мєнт%20{}%20помітив разбойніка%20{}%0A".format(players[p], players[i]))
                        die = random.randint(1,2)
                        if p in countPlayer2:
                            countPlayer2.remove(p)
                        players3[p][3] = 4
                        for c in range(len(players)):
                            if players3[c][3] != 0 and players3[c][3] != None:
                                players3[c][3] = players3[c][3] - 1
                        if die == 1:
                            if players3[i][4] != 0:
                                potential_money = [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,5000,5000,5000,5000,5000,5000,5000,5000,
                                                   10000,10000,10000,10000,10000,10000,10000,15000,15000,15000,15000,15000,15000,20000,20000,20000,20000,20000, 
                                                   25000,25000,25000,25000, 30000,30000,30000, 40000, 40000, 50000, 75000]
                                rands = random.choice(potential_money)
                                if rands < players3[i][4]:
                                    players3[i][4] -= rands
                                    message += ("Разбойнік%20{}%20виплатив%20взятку%20мєнту%20{}%20в%20розмірі%20{}$%0A".format(players[i], players[p], rands))
                                    rands2 = random.randint(1,10)
                                    if rands2 == 1:
                                        message += ("Мєнт%20{}%20наїбав%20разбойніка%20{}%20і%20виїбав%20його%20в%20сраку%0A%0A".format(players[p], players[i]))
                                        players3[i][2] = "Died"
                                        countPlayer.remove(i)
                                        Gangster.remove(i)
                                        if len(Mer) != 0:
                                            avtoritet_changable -= 1
                                            message = message[:-3]
                                            message += ("Авторитет%20мера%20падає%0A%0A")
                                        if i in countPlayer2:
                                            countPlayer2.remove(i)
                                        result()
                                    else:
                                        message +="%0A"
                                else:
                                    message += ("Разбойніку%20{}%20не%20вистачило%20коштів%20на%20взятку%20мєнту%20{},%20тому%20його%20спіткала%20анальна%20кара.%20Розмір%20взятки%20{}$%0A%0A".format(players[i], players[p], rands))
                                    players3[i][2] = "Died"
                                    countPlayer.remove(i)
                                    Gangster.remove(i)
                                    if len(Mer) != 0:
                                        avtoritet_changable -= 1
                                        message = message[:-3]
                                        message += ("Авторитет%20мера%20падає%0A%0A")
                                    if i in countPlayer2:
                                        countPlayer2.remove(i)
                                    result()
                            else:
                                win(players[p], players[i], "Мєнт", "мєнт", "мєнта", "Разбойнік", "Разбойніка", "разбойніка", False, False)
                                if len(Mer) != 0:
                                    message = message[:-3]
                                    message += ("Авторитет%20мера%20падає%0A%0A")
                                    avtoritet_changable -= 1
                                players3[i][2] = "Died"
                                countPlayer.remove(i)
                                Gangster.remove(i)
                                if i in countPlayer2:
                                    countPlayer2.remove(i)
                                result()
                        else:
                            lose(players[p], players[i], "Мєнт", "мєнт", "мєнта", "Мєнту", "Разбойнік", "разбойнік", "разбойніка", "Разбойніку")
                if players3[p][1] == "Разбойнік":
                    if players3[i][1] == "Мер":
                        message += ("Разбойнік%20{}%20помітив мера%20{}%0A".format(players[p], players[i]))
                        die = random.randint(1,2)
                        if p in countPlayer2:
                            countPlayer2.remove(p)
                        players3[p][3] = 4
                        for c in range(len(players)):
                            if players3[c][3] != 0 and players3[c][3] != None:
                                players3[c][3] = players3[c][3] - 1
                        if die == 1:
                            if len(rabstvo) != 0:
                                message += ("Мер%20{}%20переодягнувся%20в%20мєнта%20і%20втік.%20Замість%20нього%20разбойнік%20{}%20трахнув%20раба%20{}%0A%0A".format(players[i],players[p],rabstvo[0]))
                                rabstvo.remove(rabstvo[0])
                            else:
                                players3[i][2] = "Died"
                                win(players[p], players[i], "Разбойнік", "разбойнік", "разбойніка", "Мер", "Мера", "мера", True, False)
                                countPlayer.remove(i)
                                Mer.remove(i)
                                if i in countPlayer2:
                                    countPlayer2.remove(i)
                                result()
                        else:
                            lose(players[p], players[i], "Разбойнік", "разбойнік", "разбойніка", "Разбойніку", "Мер", "мер", "мера", "Меру")
            if len(players) > 4:
                nonlocal lifeMer
                ## rand = random.randint(1,2)
                rand = 1
                for r in range(len(players)):
                    for c in range(3):
                        if players3[r][c] == "Мер" and players3[r][c+1] == "Died" and lifeMer == 1 and rand == 1:
                            players3[r][c+1] = None
                            message += ("Мер%20{}%20платить%20за%20востановлєніє%20свого%20очка%20і%20повертається%20до%20гри%0A%0A".format(players[r]))
                            countPlayer.append(r)
                            lifeMer = 0
            if countPlayer2 == None or len(cho) == 1 or len(countPlayer2) == 2:
                break                           
    raund()
    while 1:
        if np.count_nonzero("Died" == players3['died']) >= (len(players) / 2) :
            for p in range(len(players)):
                if players3[p][2] != "Died":
                    for h in range(len(rate)):
                        if rate[h][0] == players[p] and rate[h][1] == str(chadid):
                            rate2[h][1] = rate2[h][1] + 1
                            if players3[p][1] == "Разбойнік":
                                rate2[h][4] = rate2[h][4] + players3[p][4]
                            break
            bot.send_mes(chadid, message)
            message = ""
            for p in range(len(players)):
                if players3[p][2] != "Died":
                    if players3[p][1] == "Разбойнік" and players3[p][4] != 0:
                        message += ("{}%20{}%20зберіг%20своє%20очко%20та%20{}$%0A".format(players3[p][1], players[p], players3[p][4]))
                    else:
                        message += ("{}%20{}%20зберіг%20своє%20очко%20та%20виграв%0A".format(players3[p][1], players[p]))
                        if players3[p][1] == "Мер" and len(rabstvo) != 0:
                            for j in rabstvo:
                                message += ("{},%20".format(j))
                            message = message[:-4]
                            message += ("%20залишилися(залишився)%20в%20рабстві%20мера%20{}%0A".format(players[p]))
            bot.send_mes(chadid, message)
            basa_add()
            break
            return
        else:
            raund()

def mytimer():
    global players
    if len(players) >= 2:
       chadid = chats[timechat[0]]
       game(chadid, players[players['chatid'] == chadid]['name'])
       players = players[np.where(players['chatid'] != bot.get_chat_id(last_update))]
       chats[timechat[0] + 1] = 1
       chats[timechat[0] + 2] = 0
       timechat.remove(timechat[0])
    else:
       bot.send_mess(chats[timechat[0]], "Достатня кількість учасників не набралась, гру відмінено")
       chats[timechat[0] + 1] = 1
       players = players[np.where(players['chatid'] != chats[timechat[0]])]
       chats[timechat[0] + 2] = 0
       timechat.remove(timechat[0])
def topplayer(r):
    b = np.sort(rate2[np.where(rate['chatid'] == str(bot.get_chat_id(last_update)))], order = r)
    if len(b) < 3:
        return 0, 0, 0, 'Ніхто', 'Ніхто','Ніхто'
    return b[-1][r], b[-2][r], b[-3][r], rate[b[-1][0]][0], rate[b[-2][0]][0], rate[b[-3][0]][0]
offset = None
chats = []
time = 0
timechat = []
players = np.zeros((0), dtype = [('name', object),('chatid', object)])
while 1:
    bot.get_updates(offset)
    last_update = bot.last_update()
    if last_update is None:
        continue
    print(last_update)
    indx = 0
    last_update_id = last_update['update_id']
    if bot.get_chat_id(last_update) != chats:
        chats.append(bot.get_chat_id(last_update))
        chats.append(1)
        chats.append(0)
    indx = chats.index(bot.get_chat_id(last_update))
    if chats[indx + 1] == 1:
        if bot.get_message(last_update) == "/game" or bot.get_message(last_update) == "/game@BogdanKarmanBot":
            chats[indx + 2] = 1
            chats[indx + 1] = 0
            timechat.append(indx)
            time = threading.Timer(7200.0, mytimer)
            time.start()
            bot.send_mes(bot.get_chat_id(last_update), 'Почалася%20гра%20"Мер,%20Мєнти%20та%20Разбойніки".%0A%0AПравила%20гри:%0AМЕР(Мер%20може%20бути%20тільки%20один)%20повинен%20трахнути%20МЄНТІВ,%20МЄНТИ%20повинні%20трахнути%20РОЗБІЙНИКІВ,%20РОЗБІЙНИКИ%20повинні%20трахнути%20МЕРА.%20Кожен%20повинен%20зберегти%20своє%20очко.%20Хто%20зберіг%20своє%20очко%20-%20той%20виграв.%20Якщо%20кількість%20гравців%20буде%20більше%205,%20то%20мер%20отримує%20шанс%201%20раз%20воскреснути.%20Все%20відбувається%20рандомно.%20Ви%20можете%20тіки%20подивитись%20результати.%0A%0AГра%20автоматично%20почнеться%20або%20буде%20припинена%20через%202%20години!!!%0A%0AЩоб%20прийняти%20участь%20в%20грі%20відправте:%20{}%20.%0A%0AЩоб%20почати%20гру(коли%20наберуться%20учасники)%20відправте:%20/start%0A%0AЩоб%20закінчити%20гру:%20/stop%0A%0A/list%20-%20подивиться%20список%20учасників%0A%0A/statistic%20-%20подивиться%20статискику%0A%0A/top3%20-%20подивиться%20топ3.'.format('"Плюс"'))
        if bot.get_username(last_update) == "@wotrex":
            bogdan = ["Согласен", "Поддержую"]
            bot.resend_mess(bot.get_chat_id(last_update), random.choice(bogdan) ,bot.get_message_id(last_update))
        if bot.get_username(last_update) == "@Shadow_99":
            bot.send_voice(bot.get_chat_id(last_update), "https://upload.wikimedia.org/wikipedia/commons/a/a7/Memes.ogg", bot.get_message_id(last_update))
        if bot.get_username(last_update) == "@handsome_qitfis":
            shputya = ["Коля поїш гамна", "Я єбав тебе в рот, Коля", "Коля дебіл, шо за флешка?","Коля блять","продам тебе циганам","це декан так сказав?","Коля гавно своє їсть","в рот собі насри",
                       "ти обісраний", "Хай коля отсосе", "Коля, ти блатний як двері", "а уїбать", "Коля ти овощ", "Коля ти тупий", "Ти дебіл коля",
                       "Завали їбало", "Пашол нахуй Коля", "Ти підарастіческа хуйня їбана", "Ти кріпак засраний, іди сіно кидай", "ти загноение  підзалупного міра", "Шкода що такого божества в японській міфології не було, чи звідки там Колі беруться", "Ти став схожим не на Колю,  а на людину", "Коля слішком скіловий, я не можу", 
                       "Коля слабоумний", "Коля хуєблядска піздопройобіна"]
            shputyaVoice = ["https://upload.wikimedia.org/wikipedia/commons/4/42/Voice1.ogg", "https://upload.wikimedia.org/wikipedia/commons/c/cb/Voice2.ogg",
                            "https://upload.wikimedia.org/wikipedia/commons/2/2e/Voice3.ogg", "https://upload.wikimedia.org/wikipedia/commons/b/b0/Voice4.ogg",
                            "https://upload.wikimedia.org/wikipedia/commons/b/bf/Voice5.ogg"]
            shputyaSticker = ["CAACAgIAAxkBAAMLXk2JdD3e2ofsBDLlagIzUwaTHXoAAhkAA_z2jxuxgnHkHXK-oRgE", "CAACAgIAAxkBAAMMXk2KENg_--cBz-PQarldNjh5RZcAAh4AA_z2jxu3VCMC9M_xsRgE",
                              "CAACAgIAAxkBAAMNXk2KSCpnTJ_KdG3R-5_D5krV1jgAAhYAA_z2jxsapXncRh_8JBgE", "CAACAgIAAxkBAAMOXk2KkQbgieGHmSSbC7yDZig5_eMAAhcAA_z2jxsfunL3I_azCBgE",
                              "CAACAgIAAxkBAAMPXk2K2S4x7TQNMNlApek7wtEvzE8AAhoAA_z2jxs18TpPKoBrkRgE", "CAACAgIAAxkBAAMQXk2LMFh_VyOv2MWnYfM1iWvxHcIAAiAAA_z2jxsr0peTWHBxFhgE",
                              "CAACAgIAAxkBAAMRXk2MEdLmfm8Y2AOrAgABtwoTVqaXAAJeAQACzcBIGJ_GOFgleipFGAQ", "CAACAgIAAxkBAAMSXk2MYj04L-zmPrWW3qYeD0QOtsMAAhwAA-b8Dxmrv56G5K6GqhgE",
                              "CAACAgIAAxkBAAMTXk2MoukYFa1k5OyKHI0BhH4AAR8GAAIxAAPm_A8ZNUSF17VXQ_sYBA", "CAACAgIAAxkBAAMUXk2M0vFtF97w6kWrwjLkvcrPfj8AAjQAA-b8Dxl0Kmt-bE6nvxgE",
                              "CAACAgIAAxkBAAMVXk2NAAE8WeT9tKg-AaACyvYhjRq_AAI4AAPm_A8Zo8L_zAxh4NIYBA", "CAACAgIAAxkBAAMWXk2NeiHTcue4AwrRBZ7nhpKu2lgAAvEAA_NWPxcqR0IBe-SHxhgE",
                              "CAACAgIAAxkBAAMXXk2N3kpBhcD3sZWhiHQrrReJOpkAAiIAA3lx3hbdu_UH5ZkpgxgE"]
            rand = random.randint(1,3)
            if rand == 1:
                bot.resend_mess(bot.get_chat_id(last_update), random.choice(shputya) ,bot.get_message_id(last_update))
            if rand == 2 :
                bot.send_voice(bot.get_chat_id(last_update), random.choice(shputyaVoice), bot.get_message_id(last_update))
            if rand == 3 :
                bot.send_sticker(bot.get_chat_id(last_update), random.choice(shputyaSticker), bot.get_message_id(last_update))
    if chats[indx + 1] == 1 or chats[indx + 2] == 1:
        if bot.get_message(last_update) == "/statistic" or bot.get_message(last_update) == "/statistic@BogdanKarmanBot":
            flag = 0
            for p in range(len(rate)):
                if rate[p][0] == bot.get_username(last_update) and rate[p][1] == str(bot.get_chat_id(last_update)):
                    flag = 1
                    bot.send_mes(bot.get_chat_id(last_update), "{}%20:%0AВиграв%20ігор%20-%20{}%0AКількість%20знищених%20ворожих%20анусів%20-%20{}%0AКількість%20разів%20коли%20втратив%20анальну%20дєвствєнность%20-%20{}%0AЗагальна%20кількість%20виграних%20грошей%20-%20{}$".format(str(rate[p][0]),rate2[p][1],rate2[p][2],rate2[p][3],rate2[p][4]))
                    break
            if flag == 0:
                bot.resend_mess(bot.get_chat_id(last_update),"В тебе намеє статистики", bot.get_message_id(last_update))
        if bot.get_message(last_update) == "/top3" or bot.get_message(last_update) == "/top3@BogdanKarmanBot":
            top1 = topplayer('wins')
            top2 = topplayer('kills')
            top3 = topplayer('losing')
            top4 = topplayer('money')
            bot.send_mes(bot.get_chat_id(last_update),'Топ%203%20побідітєлєй:%0A1.%20{}%20виграв%20{}%20раз(a).%0A2.%20{}%20виграв%20{}%20раз(a).%0A3.%20{}%20виграв%20{}%20раз(a).'.format(top1[3],str(top1[0]),top1[4],str(top1[1]),top1[5],str(top1[2])))
            bot.send_mes(bot.get_chat_id(last_update),'Топ%203%20анальних%20винищувачів:%0A1.%20{}%20знищив%20{}%20анусів.%0A2.%20{}%20знищив%20{}%20анусів.%0A3.%20{}%20знищив%20{}%20анусів.'.format(top2[3],str(top2[0]),top2[4],str(top2[1]),top2[5],str(top2[2])))
            bot.send_mes(bot.get_chat_id(last_update),'Три%20самі%20пасивні%20гея:%0A1.%20{}%20втратив%20анальну%20дєвствєнность%20{}%20раз(a).%0A2.%20{}%20втратив%20анальну%20дєвствєнность%20{}%20раз(a).%0A3.%20{}%20втратив%20анальну%20дєвствєнность%20{}%20раз(a).'.format(top3[3],str(top3[0]),top3[4],str(top3[1]),top3[5],str(top3[2])))     
            bot.send_mes(bot.get_chat_id(last_update),'Топ%203%20магната:%0A1.%20{}%20-%20{}$%20%0A2.%20{}%20-%20{}$%20%0A3.%20{}%20-%20{}$%20'.format(top4[3],str(top4[0]),top4[4],str(top4[1]),top4[5],str(top4[2])))
        if bot.get_message(last_update) == "/off" or bot.get_message(last_update) == "/off@BogdanKarmanBot":
            if chats[indx + 2] == 1:
                time.cancel()
                timechat.remove(indx)
            bot.send_mess(bot.get_chat_id(last_update),"Вимушений відлучитись, іду срать")
            offset = None
            chats[indx + 1] = 0
            chats[indx + 2] = 0
    if chats[indx + 1] == 0 and chats[indx + 2] == 0:
        if bot.get_message(last_update) == "/on" or bot.get_message(last_update) == "/on@BogdanKarmanBot" :
            bot.send_mess(bot.get_chat_id(last_update),"Я посрав, де Шпецюк блять")
            chats[indx + 1] = 1
    if chats[indx + 2] == 1:
        plys = ["+","плюс","Плюс","го","Го","go","Go"]
        game_add_res = None
        frasi_minus = ["Шо самий умний?", "В жопу свій мінус засунь", "ти довбойоб?", "мінуси тільки підари ставлять", "ще раз мінус поставиш - я приїду і виїбу тебе в очко"]
        for i in range(len(bot.get_message(last_update))):
            if bot.get_message(last_update)[i-1] == "-":
                bot.resend_mess(bot.get_chat_id(last_update), random.choice(frasi_minus) ,bot.get_message_id(last_update))
            if bot.get_message(last_update)[i-1] in plys or (bot.get_message(last_update)[i-1] + bot.get_message(last_update)[i]) in plys:
                game_add_res = bot.get_message(last_update)[i-1]
                break
            if i+2 < len(bot.get_message(last_update)):
                if (bot.get_message(last_update)[i-1] + bot.get_message(last_update)[i] + bot.get_message(last_update)[i+1] + bot.get_message(last_update)[i+2]) in plys:
                    game_add_res = bot.get_message(last_update)[i-1]
                    break    
        if game_add_res != None:
            co = 0
            for li in range(len(rate)):
                if rate[li][2] == bot.get_id(last_update) and rate[li][1] == str(bot.get_chat_id(last_update)):
                    co = 1
                    break
            if co == 0:
                rate = np.insert(rate, len(rate),(bot.get_username(last_update), str(bot.get_chat_id(last_update)),bot.get_id(last_update)), axis = 0)
                rate2 = np.insert(rate2, len(rate2),(len(rate2),0,0,0), axis = 0)
            if bot.get_username(last_update) in players['name']:
                bot.send_mess(bot.get_chat_id(last_update), bot.get_username(last_update) + ", ти вже приймаєш участь в грі")
            else:
                players = np.insert(players, len(players),(bot.get_username(last_update),bot.get_chat_id(last_update)), axis = 0)
                bot.send_mess(bot.get_chat_id(last_update), bot.get_username(last_update) + " бере участь в грі")
            if bot.get_id(last_update) in rate['id']:
                if bot.get_username(last_update) in rate[:][0]:
                    a = True
                else:
                    for u in range(len(rate)):
                        if rate[u][2] == bot.get_id(last_update):
                            rate[u][0] = bot.get_username(last_update)
        if bot.get_message(last_update) == "/list" or bot.get_message(last_update) == "/list@BogdanKarmanBot":
            pl = ""
            for s in range(len(players)):
                pl += players[s]['name'] + '%0A'
            if pl != "":
                bot.send_mes(bot.get_chat_id(last_update), "Список%20гравців:%0A{}".format(pl))
            else:
                bot.send_mes(bot.get_chat_id(last_update), "Немає%20гравців")
        if bot.get_message(last_update) == "/start" or bot.get_message(last_update) == "/start@BogdanKarmanBot":
           if len(players) >= 2:
               chadid = bot.get_chat_id(last_update)
               game(chadid, players[players['chatid'] == chadid]['name'])
               time.cancel()
               timechat.remove(indx)
               players = players[np.where(players['chatid'] != bot.get_chat_id(last_update))]
               chats[indx + 1] = 1
               chats[indx + 2] = 0
           else:
               bot.resend_mess(bot.get_chat_id(last_update), "Мало гравців(Мінімум 2)", bot.get_message_id(last_update))
        if bot.get_message(last_update) == "/stop" or bot.get_message(last_update) == "/stop@BogdanKarmanBot":
            bot.send_mess(bot.get_chat_id(last_update), "Гру відмінено")
            players = players[np.where(players['chatid'] != bot.get_chat_id(last_update))]
            chats[indx + 1] = 1
            chats[indx + 2] = 0
            time.cancel()
            timechat.remove(indx)
    offset = last_update_id + 1
