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
             if 'username' in ['edited_message']['from']:
                chat_id = update['edited_message']['from']['username']
                name = '@'+ chat_id
                return name
             else:
                 firstn = update['message']['from']['first_name']
                 return firstn
    def get_firstname(self, update):
         if 'message' in update:
             if 'first_name' in update['message']['from']:
                chat_id = update['message']['from']['first_name']
                return chat_id
         if 'edited_message' in update:
             if 'first_name' in ['edited_message']['from']:
                chat_id = update['edited_message']['from']['first_name']
                return chat_id
    def get_id(self, update):
         if 'message' in update:
             if 'id' in update['message']['from']:
                chat_id = update['message']['from']['id']
                return chat_id
         if 'edited_message' in update:
             if 'id' in ['edited_message']['from']:
                chat_id = update['edited_message']['from']['id']
                return chat_id
    def forward_mess(self, chat, from_chat, mess):  
        params = {'chat_id': chat, 'from_chat_id': from_chat, 'message_id': mess}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'forwardMessage', params)
        return response
bot = BogdanBot()
players = []
rate = np.empty((20,3), dtype="object")
rate2 = np.empty((20,4), dtype="object")
chadid = 0
objects = None
offst = None
while objects == None:
    bot.get_updates(offst)
    last_updat = bot.last_update()
    if last_updat is None:
        continue
    last_update_i = last_updat['update_id']
    if bot.get_chat_id(bot.last_update()) == 462419708:
        objects = bot.get_message(bot.last_update())
    offst = last_update_i + 1
objects1 = []
for j in objects:
    if j == "|":
        break
    objects1.append(j)
objects2 = []
ok = 0
for j in objects:
    if ok == 1:
        objects2.append(j)
    if j == "|":
        ok = 1
obj = np.empty((60,1), dtype="object")
c = 0 
for i in objects1:
    if obj[c][0] == None and i != ' ':
        obj[c][0] = i
    else:
        if i != ' ':
            obj[c][0] = obj[c][0] + i
        else:
            c = c + 1

countrow = 0
countcolumn = 0
for i in range(len(obj)):
    if countcolumn == 3:
        countcolumn = 0
        countrow = countrow + 1
    if obj[i][0] == 'None':
        rate[countrow][countcolumn] = None
        countcolumn = countcolumn + 1
    else:
        if obj[i][0].isdigit() == True or (obj[i][0].isdigit() == False and '-' in obj[i][0]):
            rate[countrow][countcolumn] = int(obj[i][0])
            countcolumn = countcolumn + 1
        else:
            rate[countrow][countcolumn] = obj[i][0]
            countcolumn = countcolumn + 1

obj = np.empty((80,1), dtype="object")
c = 0 
for i in objects2:
    if obj[c][0] == None and i != ' ':
        obj[c][0] = i
    else:
        if i != ' ':
            obj[c][0] = obj[c][0] + i
        else:
            c = c + 1
countrow = 0
countcolumn = 0
for i in range(len(obj)):
    if countcolumn == 4:
        countcolumn = 0
        countrow = countrow + 1
    if obj[i][0] == 'None':
        rate2[countrow][countcolumn] = None
        countcolumn = countcolumn + 1
    else:
        rate2[countrow][countcolumn] = int(obj[i][0])
        countcolumn = countcolumn + 1
print(rate)
print(rate2)
def basa_add():
    a = ''
    for i in range(len(rate)):
        a = a + str(rate[i][0]) + " " + str(rate[i][1]) + " " + str(rate[i][2]) + " "
    b = ''
    for i in range(len(rate2)):
        b = b + str(rate2[i][0]) + " " + str(rate2[i][1]) + " " + str(rate2[i][2]) + " " + str(rate2[i][3]) + " "
    bot.send_mess(462419708,a + "|" + b)
    return 
def countElement(massive2d, text, countrow, countcolumn):
    countRW = 0
    countCL = 0
    countext = 0
    for i in range(countrow * countcolumn):
        if countCL == countcolumn:
            countCL = 0
            countRW = countRW + 1
        if massive2d[countRW][countCL] == text:
            countext = countext + 1
            countCL = countCL + 1
        else:
            countCL = countCL + 1
    return countext

def game():
    rand = random.randint(1,3)
    players3 = np.empty((20,5), dtype="object")
    for p in range(len(players)):
        players3[p][0] = players[p]
    def storonu():
        for p in range(len(players)):
            players3[p][1] = None
        rand = random.randint(1,3)
        countM = 0
        countPlr = []
        for p in range(len(players)):
            countPlr.append(p)
        while 1:
            allReady = 0
            for p in range(len(players)):
                if players3[p][1] != None:
                    allReady = allReady + 1
            if allReady == len(players):
                break
            randomPlayer = random.choice(countPlr)
            rand = random.randint(1,3)
            if rand == 1:
                if countElement(players3,"Мєнт", 20, 3) <= countElement(players3,"Разбойнік", 20, 3):
                    players3[randomPlayer][1] = "Мєнт"
                else:
                    players3[randomPlayer][1] = "Разбойнік"
            if rand == 2:
                if countElement(players3,"Мєнт", 20, 3) >= countElement(players3,"Разбойнік", 20, 3):
                    players3[randomPlayer][1] = "Разбойнік"
                else:
                    players3[randomPlayer][1] = "Мєнт"
            if rand == 3:
                if countM == 0:
                    players3[randomPlayer][1] = "Мер"
                    countM = countM + 1
                    players3[randomPlayer][4] = 1
                else:
                    rand2= random.randint(1,2)
                    if rand2 == 1:
                        if countElement(players3,"Мєнт", 20, 3) <= countElement(players3,"Разбойнік", 20, 3):
                            players3[randomPlayer][1] = "Мєнт"
                        else:
                            players3[randomPlayer][1] = "Разбойнік"
                    if rand2 == 2:
                        if countElement(players3,"Мєнт", 20, 3) >= countElement(players3,"Разбойнік", 20, 3):
                            players3[randomPlayer][1] = "Разбойнік"
                        else:
                            players3[randomPlayer][1] = "Мєнт"
            countPlr.remove(randomPlayer)
    storonu()
    bb = False
    cc = False
    while 1 :
        if len(players) != 2:
            if len(players)%2 != 0:
                if countElement(players3,"Мєнт", 20, 3) != countElement(players3,"Разбойнік", 20, 3):
                    storonu()
                    cc = False
                else:
                    bb = True
                
                if "Мер" in players3:
                    cc = True
                else:
                    storonu()
                    bb = False
                if bb == True and cc == True:
                   break
            else:
                if countElement(players3,"Мєнт", 20, 3) - 2 == countElement(players3,"Разбойнік", 20, 3) or countElement(players3,"Мєнт", 20, 3) == countElement(players3,"Разбойнік", 20, 3) - 2 :                
                    storonu()
                    cc = False
                else:
                    bb = True
                
                if "Мер" in players3:
                    cc = True
                else:
                    storonu()
                    bb = False
                if bb == True and cc == True:
                   break
                
        else:
            break

    for k in range(len(players)):
        if players3[k][0] != None and players3[k][1] != None:
            bot.send_mess(chadid, players3[k][0] + " - " + players3[k][1])
    countPlayer = []
    for p in range(len(players)):
        countPlayer.append(p)
    def raund():
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
            if (choice != choice2 and (players3[p][3] == None or players3[p][3] == 0)) or timer == 0:
                timer = 20

                if players3[p][1] == "Мер":
                    if players3[i][1] == "Мєнт":
                        bot.send_mess(chadid, "Мер " + players[p] + " помітив мєнта " + players[i])
                        die = random.randint(1,2)
                        if p in countPlayer2:
                            countPlayer2.remove(p)
                        players3[p][3] = 4
                        for c in range(len(players)):
                            if players3[c][3] != 0 and players3[c][3] != None:
                                players3[c][3] = players3[c][3] - 1
                        if die == 1:
                            rep = random.randint(1,5)
                            if rep == 1:
                                bot.send_mess(chadid, "Мер " + players[p] + " знищив очко мєнта " + players[i])
                            if rep == 2:
                                bot.send_mess(chadid, "Мер " + players[p] + " розтарабанив очко мєнта " + players[i])
                            if rep == 3:
                                bot.send_mess(chadid, "Мєнт " + players[i] + " кінчив в штани коли його їбав мер " + players[p])
                            if rep == 4:
                                bot.send_mess(chadid, "Мєнта " + players[i] + " спіткала анальна кара мера " + players[p])
                            if rep == 5:
                                bot.send_mess(chadid, "Ракета мера " + players[p] + " стрімко влетіла в чорну диру мєнта " + players[i])
                            players3[i][2] = "Died"
                            countPlayer.remove(i)
                            Police.remove(i)
                            if i in countPlayer2:
                                countPlayer2.remove(i)
                            if players[p] in rate:
                                for h in range(len(rate)):
                                    if rate[h][0] == players[p]:
                                        rate2[h][2] = rate2[h][2] + 1
                                        break
                            if players[i] in rate:
                                for h in range(len(rate)):
                                    if rate[h][0] == players[i]:
                                        rate2[h][3] = rate2[h][3] + 1
                                        break
                        else:
                            life = random.randint(1,5)
                            if life == 1:
                                bot.send_mess(chadid, "Мер " + players[p] + " промазав своїм пенісом і мєнт " + players[i] + " зірвався та втік")
                            if life == 2:
                                bot.send_mess(chadid, "Мєнту " + players[i] + " вдалося уникнути пеніса мера " + players[p])
                            if life == 3:
                                bot.send_mess(chadid, "Меру " + players[p] + " не вдалося піймати мєнта " + players[i])
                            if life == 4:
                                bot.send_mess(chadid, "Мєнт " + players[i] + " в останній момент використав 'стан' і втік від мера " + players[p])
                            if life == 5:
                                bot.send_mess(chadid, "Мєнт " + players[i] + " в останній момент насрав в штани і мер " + players[p + " змушений був відступити"])
                if players3[p][1] == "Мєнт":
                    if players3[i][1] == "Разбойнік":
                        bot.send_mess(chadid, "Мєнт " + players[p] + " помітив разбойніка " + players[i])
                        die = random.randint(1,2)
                        if p in countPlayer2:
                            countPlayer2.remove(p)
                        players3[p][3] = 4
                        for c in range(len(players)):
                            if players3[c][3] != 0 and players3[c][3] != None:
                                players3[c][3] = players3[c][3] - 1
                        if die == 1:
                            rep = random.randint(1,5)
                            if rep == 1:
                                bot.send_mess(chadid, "Мєнт " + players[p] + " знищив очко разбойніка " + players[i])
                            if rep == 2:
                                bot.send_mess(chadid, "Мєнт " + players[p] + " розтарабанив очко разбойніка " + players[i])
                            if rep == 3:
                                bot.send_mess(chadid, "Разбойнік " + players[i] + " кінчив в штани коли його їбав мєнт " + players[p])
                            if rep == 4:
                                bot.send_mess(chadid, "Разбойніка " + players[i] + " спіткала анальна кара мєнта " + players[p])
                            if rep == 5:
                                bot.send_mess(chadid, "Ракета мєнта " + players[p] + " стрімко влетіла в чорну диру разбойніка " + players[i])
                            
                            players3[i][2] = "Died"
                            countPlayer.remove(i)
                            Gangster.remove(i)
                            if i in countPlayer2:
                                countPlayer2.remove(i)
                            if players[p] in rate:
                                for h in range(len(rate)):
                                    if rate[h][0] == players[p]:
                                        rate2[h][2] = rate2[h][2] + 1
                                        break
                            if players[i] in rate:
                                for h in range(len(rate)):
                                    if rate[h][0] == players[i]:
                                        rate2[h][3] = rate2[h][3] + 1
                                        break
                        else:
                            life = random.randint(1,5)
                            if life == 1:
                                bot.send_mess(chadid, "Мєнт " + players[p] + " промазав своїм пенісом і разбойнік " + players[i] + " зірвався та втік")
                            if life == 2:
                                bot.send_mess(chadid, "Разбойніку " + players[i] + " вдалося уникнути пеніса мєнта " + players[p])
                            if life == 3:
                                bot.send_mess(chadid, "Мєнту " + players[p] + " не вдалося піймати разбойніка " + players[i])
                            if life == 4:
                                bot.send_mess(chadid, "Разбойнік " + players[i] + " в останній момент використав 'стан' і втік від мєнта " + players[p])
                            if life == 5:
                                bot.send_mess(chadid, "Разбойнік " + players[i] + " в останній момент насрав в штани і мєнт " + players[p + " змушений був відступити"])
                if players3[p][1] == "Разбойнік":
                    if players3[i][1] == "Мер":
                        bot.send_mess(chadid, "Разбойнік " + players[p] + " помітив мера " + players[i])
                        die = random.randint(1,2)
                        if p in countPlayer2:
                            countPlayer2.remove(p)
                        players3[p][3] = 4
                        for c in range(len(players)):
                            if players3[c][3] != 0 and players3[c][3] != None:
                                players3[c][3] = players3[c][3] - 1
                        if die == 1:
                            rep = random.randint(1,5)
                            if rep == 1:
                                bot.send_mess(chadid, "Разбойнік " + players[p] + " знищив очко мера " + players[i])
                            if rep == 2:
                                bot.send_mess(chadid, "Разбойнік " + players[p] + " розтарабанив очко мера " + players[i])
                            if rep == 3:
                                bot.send_mess(chadid, "Мер " + players[i] + " кінчив в штани коли його їбав разбойнік " + players[p])
                            if rep == 4:
                                bot.send_mess(chadid, "Мера " + players[i] + " спіткала анальна кара разбойніка " + players[p])
                            if rep == 5:
                                bot.send_mess(chadid, "Ракета разбойніка " + players[p] + " стрімко влетіла в чорну диру мера " + players[i])
                            players3[i][2] = "Died"
                            countPlayer.remove(i)
                            Mer.remove(i)
                            if i in countPlayer2:
                                countPlayer2.remove(i)
                            if players[p] in rate:
                                for h in range(len(rate)):
                                    if rate[h][0] == players[p]:
                                        rate2[h][2] = rate2[h][2] + 1
                                        break
                            if players[i] in rate:
                                for h in range(len(rate)):
                                    if rate[h][0] == players[i]:
                                        rate2[h][3] = rate2[h][3] + 1
                                        break
                        else:
                            life = random.randint(1,5)
                            if life == 1:
                                bot.send_mess(chadid, "Разбойнік " + players[p] + " промазав своїм пенісом і мер " + players[i] + " зірвався та втік")
                            if life == 2:
                                bot.send_mess(chadid, "Меру " + players[i] + " вдалося уникнути пеніса разбойніка " + players[p])
                            if life == 3:
                                bot.send_mess(chadid, "Разбойніку " + players[p] + " не вдалося піймати мера " + players[i])
                            if life == 4:
                                bot.send_mess(chadid, "Мер " + players[i] + " в останній момент використав 'стан' і втік від разбойніка " + players[p])
                            if life == 5:
                                bot.send_mess(chadid, "Мер " + players[i] + " в останній момент насрав в штани і разбойнік " + players[p + " змушений був відступити"])
            if len(players) > 5:
                for r in range(len(players)):
                    for c in range(3):
                        if players3[r][c] == "Мер":
                            if players3[r][c+1] == "Died":
                                if players3[r][4] == 1:
                                    rand = random.randint(1,2)
                                    if rand == 1:
                                        players3[r][c+1] = None
                                        bot.send_mess(chadid, "Мер " + players[r] + " платить за востановлєніє свого очка і повертається до гри")
                                        countPlayer.append(r)
                                        players3[r][4] = 0
            if countPlayer2 == None or len(cho) == 1 or len(countPlayer2) == 2:
                break                           
    raund()
    while 1:
        if countElement(players3,"Died", 20, 3) >= (len(players) / 2) :
            for p in range(len(players)):
                if players[p] in rate:
                    if players3[p][2] != "Died":
                        for h in range(len(rate)):
                            if rate[h][0] == players[p]:
                                rate2[h][1] = rate2[h][1] + 1
                                break
                    
            for p in range(len(players)):
                if players3[p][2] != "Died":
                    bot.send_mess(chadid, players3[p][1] + " " + players[p] + " зберіг своє очко та виграв" )
            players.clear()
            basa_add()
            break
            return
        else:
            raund()
    

offset = None
chats = []
igra = "Гра Ігра Игра Game Грать Плей Играть Іграть play гра ігра игра game грать плей играть іграть play"
off = "Богдан, завали єбало Соси cоси Закрий єбало Завали єбало Богдан, закрий єбало Богдан, єбало офф Єбало офф off Пішов Богдан, нахуй ашол Богдан, нахуй пішов нахуй Пашол нахуй Іди нах Богдан, іди нах Іди нахуй Богдан, іди нахуй Богдан, сосни Сосни Богдан, пососи Пососи"
on = "Бодька Богдан Бодя Бодька ти тут? Богдан ти тут? Бодя ти тут? Бодька проснись Богдан проснись Бодя проснись Бодька, ти тут? Богдан, ти тут? Бодя, ти тут? Бодька, проснись Богдан, проснись Бодя, проснись "
plys = "+ плюс Плюс го Го"
lict = "List list лист Лист список Список ліст Ліст"
statis = "Стат Стати Статы Статистика Stats стат стати статы статистика stats"
ton = "Top top Топ топ"
startt = "start Start Старт старт начать Начать"
stopp = "Stop stop Стоп стоп"
time = 0
timechat = []
while 1:
    bot.get_updates(offset)
    last_update = bot.last_update()
    if last_update is None:
        continue
    last_update_id = last_update['update_id']
    r = random.randint(1,36)
    rb = random.randint(1,3)
    if bot.get_chat_id(bot.last_update()) != chats:
        chats.append(bot.get_chat_id(bot.last_update()))
        chats.append(1)
        chats.append(0)
    indx = chats.index(bot.get_chat_id(bot.last_update()))
    if chats[indx + 1] == 1:
        if bot.get_message(bot.last_update()) in igra:
            chats[indx + 2] = 1
            chats[indx + 1] = 0
            timechat.append(indx)
            def mytimer():
                if len(players) >= 2:
                   chadid = chats[timechat[0]]
                   game()
                   chats[timechat[0] + 1] = 1
                   chats[timechat[0] + 2] = 0
                   timechat.remove(timechat[0])
                else:
                   bot.send_mess(chats[timechat[0]], "Достатня кількість учасників не набралась, гру відмінено")
                   chats[timechat[0] + 1] = 1
                   chats[timechat[0] + 2] = 0
                   timechat.remove(timechat[0])
            time = threading.Timer(7200.0, mytimer)
            time.start()
            bot.send_mes(bot.get_chat_id(bot.last_update()), 'Почалася%20гра%20"Мер,%20Мєнти%20та%20Разбойніки".%0A%0AПравила%20гри:%0AМЕР(Мер%20може%20бути%20тільки%20один)%20повинен%20трахнути%20МЄНТІВ,%20МЄНТИ%20повинні%20трахнути%20РОЗБІЙНИКІВ,%20РОЗБІЙНИКИ%20повинні%20трахнути%20МЕРА.%20Кожен%20повинен%20зберегти%20своє%20очко.%20Хто%20зберіг%20своє%20очко%20-%20той%20виграв.%20Якщо%20кількість%20гравців%20буде%20більше%205,%20то%20мер%20отримує%20шанс%201%20раз%20воскреснути.%20Все%20відбувається%20рандомно.%20Ви%20можете%20тіки%20подивитись%20результати.%0A%0AГра%20автоматично%20начнеться%20або%20буде%20припинена%20через%202%20години!!!%0A%0AЩоб%20прийняти%20участь%20в%20грі%20відправте:%20{}%20.%0A%0AЩоб%20почати%20гру(коли%20наберуться%20учасники)%20відправте:%20"Старт"%20або%20"Start".%0A%0AЩоб%20закінчити%20гру:%20"Стоп"%20або%20"Stop".%0A%0A"list"%20-%20подивиться%20список%20учасників%0A%0A"Статистика"%20-%20подивиться%20статискику%0A%0A"Топ"%20-%20подивиться%20топ3.'.format('"Плюс"'))
        if bot.get_username(bot.last_update()) == "@zagin177":
            if rb == 1:
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"+", bot.get_message_id(bot.last_update()))
            if rb == 2:
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Согласен", bot.get_message_id(bot.last_update()))
            if rb == 3:
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Поддержую", bot.get_message_id(bot.last_update()))
        if bot.get_username(bot.last_update()) == "@shputya":
            if r == 1 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпецюк поїш гамна", bot.get_message_id(bot.last_update()))
            if r == 2 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Я єбав тебе в рот, Шпетюк", bot.get_message_id(bot.last_update()))
            if r == 3 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпетюк блять", bot.get_message_id(bot.last_update()))
            if r == 4 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"продам тебе циганам", bot.get_message_id(bot.last_update()))
            if r == 5 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпетюк гавно своє їсть", bot.get_message_id(bot.last_update()))
            if r == 6 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"в рот собі насри", bot.get_message_id(bot.last_update()))
            if r == 7 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"ти обісраний", bot.get_message_id(bot.last_update()))
            if r == 8 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Хай шпетюк отсосе", bot.get_message_id(bot.last_update()))
            if r == 9 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпецюк", bot.get_message_id(bot.last_update()))
                bot.send_mess(bot.get_chat_id(bot.last_update()),"Ти блатний як двері")
            if r == 10 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"а уїбать", bot.get_message_id(bot.last_update()))
            if r == 11 :
                bot.send_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/4/42/Voice1.ogg", bot.get_message_id(bot.last_update()))
            if r == 12 :
                bot.send_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/c/cb/Voice2.ogg", bot.get_message_id(bot.last_update()))
            if r == 13 :
                bot.send_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/2/2e/Voice3.ogg", bot.get_message_id(bot.last_update()))
            if r == 14 :
                bot.send_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/b/b0/Voice4.ogg", bot.get_message_id(bot.last_update()))
            if r == 15 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"@wotrex, ти овощ", bot.get_message_id(bot.last_update()))
            if r == 16 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпитя ти тупий", bot.get_message_id(bot.last_update()))
            if r == 17 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Ти дебіл шпитя", bot.get_message_id(bot.last_update()))
            if r == 18 :
                bot.send_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/b/bf/Voice5.ogg", bot.get_message_id(bot.last_update()))
            if r == 19 :                
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Завали їбало", bot.get_message_id(bot.last_update()))
            if r == 20 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Пашол нахуй Шпитюк", bot.get_message_id(bot.last_update()))
            if r == 21 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Ти підарастіческа хуйня їбана", bot.get_message_id(bot.last_update()))
            if r == 22 : 
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"Ти кріпак засраний", bot.get_message_id(bot.last_update()))
                bot.send_mess(bot.get_chat_id(bot.last_update()),"Іди сіно кидай")
            if r == 23 :
                bot.resend_mess(bot.get_chat_id(bot.last_update()),"ти загноение  підзалупного міра", bot.get_message_id(bot.last_update()))
            if r == 24 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMLXk2JdD3e2ofsBDLlagIzUwaTHXoAAhkAA_z2jxuxgnHkHXK-oRgE", bot.get_message_id(bot.last_update()))              
            if r == 25 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMMXk2KENg_--cBz-PQarldNjh5RZcAAh4AA_z2jxu3VCMC9M_xsRgE", bot.get_message_id(bot.last_update()))              
            if r == 26 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMNXk2KSCpnTJ_KdG3R-5_D5krV1jgAAhYAA_z2jxsapXncRh_8JBgE", bot.get_message_id(bot.last_update()))               
            if r == 27 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMOXk2KkQbgieGHmSSbC7yDZig5_eMAAhcAA_z2jxsfunL3I_azCBgE", bot.get_message_id(bot.last_update()))                
            if r == 28 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMPXk2K2S4x7TQNMNlApek7wtEvzE8AAhoAA_z2jxs18TpPKoBrkRgE", bot.get_message_id(bot.last_update()))                
            if r == 29 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMQXk2LMFh_VyOv2MWnYfM1iWvxHcIAAiAAA_z2jxsr0peTWHBxFhgE", bot.get_message_id(bot.last_update()))                
            if r == 30 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMRXk2MEdLmfm8Y2AOrAgABtwoTVqaXAAJeAQACzcBIGJ_GOFgleipFGAQ", bot.get_message_id(bot.last_update()))                
            if r == 31 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMSXk2MYj04L-zmPrWW3qYeD0QOtsMAAhwAA-b8Dxmrv56G5K6GqhgE", bot.get_message_id(bot.last_update()))               
            if r == 32 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMTXk2MoukYFa1k5OyKHI0BhH4AAR8GAAIxAAPm_A8ZNUSF17VXQ_sYBA", bot.get_message_id(bot.last_update()))                
            if r == 33 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMUXk2M0vFtF97w6kWrwjLkvcrPfj8AAjQAA-b8Dxl0Kmt-bE6nvxgE", bot.get_message_id(bot.last_update()))                
            if r == 34 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMVXk2NAAE8WeT9tKg-AaACyvYhjRq_AAI4AAPm_A8Zo8L_zAxh4NIYBA", bot.get_message_id(bot.last_update()))                
            if r == 35 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMWXk2NeiHTcue4AwrRBZ7nhpKu2lgAAvEAA_NWPxcqR0IBe-SHxhgE", bot.get_message_id(bot.last_update()))               
            if r == 36 :
                bot.send_sticker(bot.get_chat_id(bot.last_update()),"CAACAgIAAxkBAAMXXk2N3kpBhcD3sZWhiHQrrReJOpkAAiIAA3lx3hbdu_UH5ZkpgxgE", bot.get_message_id(bot.last_update()))
            
        if bot.get_message(bot.last_update()) in off :
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Ок")
            offset = None
            chats[indx + 1] = 0
    if chats[indx + 1] == 0 and chats[indx + 2] == 0:
        if bot.get_message(bot.last_update()) in on :
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Де Шпецюк блять")
            chats[indx + 1] = 1
    if chats[indx + 2] == 1: 
        if bot.get_message(bot.last_update()) in plys:
            if bot.get_username(bot.last_update()) in players:
                bot.send_mess(bot.get_chat_id(bot.last_update()), bot.get_username(bot.last_update()) + ", ти вже приймаєш участь в грі")
            else:
                players.append(bot.get_username(bot.last_update()))
                bot.send_mess(bot.get_chat_id(bot.last_update()), bot.get_username(bot.last_update()) + " бере участь в грі")
            if bot.get_id(bot.last_update()) in rate:
                if bot.get_username(bot.last_update()) in rate:
                    a = True
                else:
                    for u in range(len(rate)):
                        if rate[u][2] == bot.get_id(bot.last_update()):
                            rate[u][0] = bot.get_username(bot.last_update())
            else:
                for u in range(len(rate)):
                    if rate[u][0] == None:
                        rate[u][0] = bot.get_username(bot.last_update())
                        rate[u][2] = bot.get_id(bot.last_update())
                        rate[u][1] = bot.get_chat_id(bot.last_update())
                        rate2[u][0] = u
                        rate2[u][1] = 0
                        rate2[u][2] = 0
                        rate2[u][3] = 0
                        break
            for l in range(len(rate)):
                if rate[l][0] == bot.get_username(bot.last_update())
                    rate[l][1] = bot.get_chat_id(bot.last_update())
                    break
        if bot.get_message(bot.last_update()) in lict:
            pl = None
            for s in range(len(players)):
                if pl == None:
                    pl = '%0A'+ players[s]
                else:
                    pl = pl + '%0A'+ players[s]
            bot.send_mes(bot.get_chat_id(bot.last_update()), "Список%20гравців:{}".format(pl))
        if bot.get_message(bot.last_update()) in statis:
            bot.send_mess(bot.get_chat_id(bot.last_update()), "Статистика гравців:")
            for p in range(len(rate)):
                if rate[p][0] != None and rate[p][1] == bot.get_chat_id(bot.last_update()) :
                    r1=str(rate[p][0])
                    r2=rate2[p][1]
                    r3=rate2[p][2]
                    r4=rate2[p][3]
                    bot.send_mes(bot.get_chat_id(bot.last_update()), "{}%20:%0AВиграв%20ігор%20-%20{}%0AКількість%20знищених%20ворожих%20анусів%20-%20{}%0AКількість%20разів%20коли%20втратив%20анальну%20дєвствєнность%20-%20{}".format(r1,r2,r3,r4))
        if bot.get_message(bot.last_update()) in ton:
            c = [0,0,0]
            j = [None, None, None]
            for p in range(len(rate)):
                if rate[p][0] != None and rate[p][1] == bot.get_chat_id(bot.last_update()) :
                    if rate2[p][1] > c[0]:                  
                        c[0] = rate2[p][1]
                        j[0] = rate[p][0]
                    else:
                        if rate2[p][1] > c[1]:
                            c[1] = rate2[p][1]
                            j[1] = rate[p][0]
                        else:
                            if rate2[p][1] > c[2]:
                                c[2] = rate2[p][1]
                                j[2] = rate[p][0]
            bot.send_mes(bot.get_chat_id(bot.last_update()),'Топ%203%20побідітєлєй:%0A1.%20{}%20виграв%20{}%20раз(a).%0A2.%20{}%20виграв%20{}%20раз(a).%0A3.%20{}%20виграв%20{}%20раз(a).'.format(j[0],str(c[0]),j[1],str(c[1]),j[2],str(c[2])))
            c = [0,0,0]
            j = [None, None, None]
            for p in range(len(rate)):
                if rate[p][0] != None and rate[p][1] == bot.get_chat_id(bot.last_update()):
                    if rate2[p][2] > c[0]:                  
                        c[0] = rate2[p][2]
                        j[0] = rate[p][0]
                    else:
                        if rate2[p][2] > c[1]:
                            c[1] = rate2[p][2]
                            j[1] = rate[p][0]
                        else:
                            if rate2[p][2] > c[2]:
                                c[2] = rate2[p][2]
                                j[2] = rate[p][0]
            bot.send_mes(bot.get_chat_id(bot.last_update()),'Топ%203%20анальних%20винищувачів:%0A1.%20{}%20знищив%20{}%20анусів.%0A2.%20{}%20знищив%20{}%20анусів.%0A3.%20{}%20знищив%20{}%20анусів.'.format(j[0],str(c[0]),j[1],str(c[1]),j[2],str(c[2])))
            c = [0,0,0]
            j = [None, None, None]
            for p in range(len(rate)):
                if rate[p][0] != None and rate[p][1] == bot.get_chat_id(bot.last_update()):
                    if rate2[p][3] > c[0]:                  
                        c[0] = rate2[p][3]
                        j[0] = rate[p][0]
                    else:
                        if rate2[p][3] > c[1]:
                            c[1] = rate2[p][3]
                            j[1] = rate[p][0]
                        else:
                            if rate2[p][3] > c[2]:
                                c[2] = rate2[p][3]
                                j[2] = rate[p][0]
            bot.send_mes(bot.get_chat_id(bot.last_update()),'Три%20самі%20пасивні%20гея:%0A1.%20{}%20втратив%20анальну%20дєвствєнность%20{}%20раз(a).%0A2.%20{}%20втратив%20анальну%20дєвствєнность%20{}%20раз(a).%0A3.%20{}%20втратив%20анальну%20дєвствєнность%20{}%20раз(a).'.format(j[0],str(c[0]),j[1],str(c[1]),j[2],str(c[2])))
            
        if bot.get_message(bot.last_update()) in startt:
           if len(players) >= 2:
               chadid = bot.get_chat_id(bot.last_update())
               game()
               time.cancel()
               timechat.remove(indx)
               chats[indx + 1] = 1
               chats[indx + 2] = 0
           else:
               bot.resend_mess(bot.get_chat_id(bot.last_update()), "Мало гравців(Мінімум 2)", bot.get_message_id(bot.last_update()))


        if bot.get_message(bot.last_update()) in stopp:
            bot.send_mess(bot.get_chat_id(bot.last_update()), "Гру відмінено")
            players.clear()
            chats[indx + 1] = 1
            chats[indx + 2] = 0
            time.cancel()
            timechat.remove(indx)
    offset = last_update_id + 1
    
