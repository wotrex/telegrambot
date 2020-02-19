import requests
import json
import random
import numpy as np

class BogdanBot():

    def __init__(self):
        self.u = "https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/getUpdates"

    def get_updates(self,offset=None, timeout=30):
        params = {'timeout': timeout, 'offset': offset}
        self.url = requests.get(self.u, params)
        jsonresponse = json.loads(self.url.text)
        return jsonresponse

    def last_update(self):  
        results = self.get_updates()['result']
        if len(results) > 0:
            last_update = results[-1]
        else:
            last_update = None

        return last_update 
    
    def get_chat_id(self,update):
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            return chat_id
        if 'edited_message' in update:
            chat_id = update['message']['chat']['id']
            return chat_id
    
    def send_mess(self, chat, text):  
        params = {'chat_id': chat, 'text': text}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'sendMessage', params)
        return response
    def resend_mess(self, chat, text, reply):  
        params = {'chat_id': chat, 'text': text, 'reply_to_message_id': reply}
        response = requests.post("https://api.telegram.org/bot1074489281:AAGtlJU5Aw1MuEljMucVl40HjlqxgZfauK0/" + 'sendMessage', params)
        return response
    def send_mes(self, chat, text):  
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/sendMessage?chat_id={}&text={}".format(chat, text))
        return response
    def send_voice(self, chat, voice):  
        params = {'chat_id': chat, 'voice': voice}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'sendVoice', params)
        return response
    def get_message(self,update):
        if 'message' in update:
            if 'text' in update['message']:
                chat_id = update['message']['text']
                return chat_id
            else:
                no = "non"
                return no
        if 'edited_message' in update:
            if 'text' in update['edited_message']:
                chat_id = update['edited_message']['text']
                return chat_id
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
                return chat_id
             else:
                 firstn = update['message']['from']['first_name']
                 return firstn
         if 'edited_message' in update:
             if 'username' in ['edited_message']['from']:
                chat_id = update['edited_message']['from']['username']
                return chat_id
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
    def forward_mess(self, chat, from_chat, mess):  
        params = {'chat_id': chat, 'from_chat_id': from_chat, 'message_id': mess}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'forwardMessage', params)
        return response    
        

bot = BogdanBot()
players = []
rate = np.empty((20,1), dtype="object")
rate2 = np.empty((20,4), dtype="object")
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
            
def game_start() :
    offset = None
    bot.send_mes(bot.get_chat_id(bot.last_update()), 'Почалася%20гра%20"Мер,%20Мєнти%20та%20Разбойніки".%0A%0AПравила%20гри:%0AМЕР%20повинен%20трахнути%20МЄНТІВ,%20МЄНТИ%20повинні%20трахнути%20РОЗБІЙНИКІВ,%20РОЗБІЙНИКИ%20повинні%20трахнути%20МЕРА.%20Кожен%20повинен%20зберегти%20своє%20очко.%20Хто%20зберіг%20своє%20очко%20-%20той%20виграв.%20Все%20відбувається%20рандомно.%20Ви%20можете%20тіки%20подивитись%20результати.%0A%0AЩоб%20прийняти%20участь%20в%20грі%20відправте:%20{}%20.%0A%0AЩоб%20почати%20гру(коли%20наберуться%20учасники)%20відправте:%20"Старт"%20або%20"Start".%0A%0AЩоб%20закінчити%20гру:%20"Стоп"%20або%20"Stop".%0A%0A"list"%20-%20подивиться%20список%20учасників%0A%0A"Статистика"%20-%20подивиться%20статискику%0A%0A"Топ"%20-%20подивиться%20топ3.'.format('"Плюс"'))
    while 1:
        bot.get_updates(offset)
        last_update = bot.last_update()
        if last_update is None:
            continue
        last_update_id = last_update['update_id']
        plys = "+ плюс Плюс го Го"
        if bot.get_message(bot.last_update()) in plys:
            if bot.get_username(bot.last_update()) in players:
                bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + bot.get_username(bot.last_update()) + ", ти вже приймаєш участь в грі")
            else:
                players.append(bot.get_username(bot.last_update()))
                bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + bot.get_username(bot.last_update()) + " бере участь в грі")
            if bot.get_username(bot.last_update()) in rate:
                a = True
            else:
                for u in range(len(rate)):
                    if rate[u][0] == None:
                        rate[u][0] = bot.get_username(bot.last_update())
                        rate2[u][0] = u
                        rate2[u][1] = 0
                        rate2[u][2] = 0
                        rate2[u][3] = 0
                        break
                    
        lict = "List list лист Лист список Список ліст Ліст"
        if bot.get_message(bot.last_update()) in lict:
            pl = None
            for s in range(len(players)):
                if pl == None:
                    pl = '%0A@'+ players[s]
                else:
                    pl = pl + '%0A@'+ players[s]
            bot.send_mes(bot.get_chat_id(bot.last_update()), "Список%20гравців:{}".format(pl))
        statis = "Стат Стати Статы Статистика Stats стат стати статы статистика stats"
        if bot.get_message(bot.last_update()) in statis:
            bot.send_mess(bot.get_chat_id(bot.last_update()), "Статистика гравців:")
            for p in range(len(rate)):
                if rate[p] != None and rate2[p][1] != None and rate2[p][2] != None and rate2[p][3] != None:
                    r1=str(rate[p][0])
                    r2=rate2[p][1]
                    r3=rate2[p][2]
                    r4=rate2[p][3]
                    bot.send_mes(bot.get_chat_id(bot.last_update()), "@{}%20:%0AВиграв%20ігор%20-%20{}%0AКількість%20знищених%20ворожих%20анусів%20-%20{}%0AКількість%20разів%20коли%20втратив%20анальну%20дєвствєнность%20-%20{}".format(r1,r2,r3,r4))
        ton = "Top top Топ топ"
        if bot.get_message(bot.last_update()) in ton:
            c = [0,0,0]
            j = [None, None, None]
            for p in range(len(rate)):
                if rate[p] != None and rate2[p][1] != None and rate2[p][2] != None and rate2[p][3] != None:
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
            bot.send_mes(bot.get_chat_id(bot.last_update()),'Топ%203%20побідітєлєй:%0A1.%20@{}%20виграв%20{}%20раз(a).%0A2.%20@{}%20виграв%20{}%20раз(a).%0A3.%20@{}%20виграв%20{}%20раз(a).'.format(j[0],str(c[0]),j[1],str(c[1]),j[2],str(c[2])))
            c = [0,0,0]
            j = [None, None, None]
            for p in range(len(rate)):
                if rate[p] != None and rate2[p][1] != None and rate2[p][2] != None and rate2[p][3] != None:
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
            bot.send_mes(bot.get_chat_id(bot.last_update()),'Топ%203%20анальних%20винищувачів:%0A1.%20@{}%20знищив%20{}%20анусів.%0A2.%20@{}%20знищив%20{}%20анусів.%0A3.%20@{}%20знищив%20{}%20анусів.'.format(j[0],str(c[0]),j[1],str(c[1]),j[2],str(c[2])))
            c = [0,0,0]
            j = [None, None, None]
            for p in range(len(rate)):
                if rate[p] != None and rate2[p][1] != None and rate2[p][2] != None and rate2[p][3] != None:
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
            bot.send_mes(bot.get_chat_id(bot.last_update()),'Три%20самі%20пасивні%20гея:%0A1.%20@{}%20втратив%20анальну%20дєвствєнность%20{}%20раз(a).%0A2.%20@{}%20втратив%20анальну%20дєвствєнность%20{}%20раз(a).%0A3.%20@{}%20втратив%20анальну%20дєвствєнность%20{}%20раз(a).'.format(j[0],str(c[0]),j[1],str(c[1]),j[2],str(c[2])))
            
        if bot.get_message(bot.last_update()) == "Старт" or bot.get_message(bot.last_update()) == "Start":
           if len(players) >= 2:
               game()
               break
           else:
               bot.send_mess(bot.get_chat_id(bot.last_update()), "Мало гравців(Мінімум 2)")


        if bot.get_message(bot.last_update()) == "Стоп" or bot.get_message(bot.last_update()) == "Stop":
            bot.send_mess(bot.get_chat_id(bot.last_update()), "Гру відмінено")
            players.clear()
            break
        offset = last_update_id + 1
        
def game():
    rand = random.randint(1,3)
    players3 = np.empty((20,3), dtype="object")
    for p in range(len(players)):
        players3[p][0] = players[p]
    def storonu():
        rand = random.randint(1,3)
        countM = 0
        for p in range(len(players)):
            rand = random.randint(1,3)
            if rand == 1:
                if countElement(players3,"Мєнт", 20, 3) <= countElement(players3,"Разбойнік", 20, 3):
                    players3[p][1] = "Мєнт"
                else:
                    players3[p][1] = "Разбойнік"
            if rand == 2:
                if countElement(players3,"Мєнт", 20, 3) >= countElement(players3,"Разбойнік", 20, 3):
                    players3[p][1] = "Разбойнік"
                else:
                    players3[p][1] = "Мєнт"
            if rand == 3:
                if countM == 0:
                    players3[p][1] = "Мер"
                    countM = countM + 1
                else:
                    rand2= random.randint(1,2)
                    if rand2 == 1:
                        if countElement(players3,"Мєнт", 20, 3) <= countElement(players3,"Разбойнік", 20, 3):
                            players3[p][1] = "Мєнт"
                        else:
                            players3[p][1] = "Разбойнік"
                    if rand2 == 2:
                        if countElement(players3,"Мєнт", 20, 3) >= countElement(players3,"Разбойнік", 20, 3):
                            players3[p][1] = "Разбойнік"
                        else:
                            players3[p][1] = "Мєнт"
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
            bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + players3[k][0] + " - " + players3[k][1])
    def raund():
        for p in range(len(players)):
            if players3[p][2] != "Died":
                for i in range(len(players)):
                    if i != p and players3[i][2] != "Died":
                        if players3[p][1] == "Мер":
                            if players3[i][1] == "Мєнт":
                                bot.send_mess(bot.get_chat_id(bot.last_update()), "Мер @" + players[p] + " помітив мєнта @" + players[i])
                                die = random.randint(1,2)
                                if die == 1:
                                    rep = random.randint(1,4)
                                    if rep == 1:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мер @" + players[p] + " знищив очко мєнта @" + players[i])
                                    if rep == 2:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мер @" + players[p] + " розтарабанив очко мєнта @" + players[i])
                                    if rep == 3:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнт @" + players[i] + " кінчив в штани коли його їбав мер @" + players[p])
                                    if rep == 4:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнта @" + players[i] + " спіткала анальна кара мера @" + players[p])
                                    players3[i][2] = "Died"
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
                                    life = random.randint(1,4)
                                    if life == 1:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мер @" + players[p] + " промазав своїм пенісом і мєнт @" + players[i] + " зірвався та втік")
                                    if life == 2:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнту @" + players[i] + " вдалося уникнути пеніса мера @" + players[p])
                                    if life == 3:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Меру @" + players[p] + " не вдалося піймати мєнта @" + players[i])
                                    if life == 4:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнт @" + players[i] + " в останній момент використав 'стан' і втік від мера @" + players[p])
                        if players3[p][1] == "Мєнт":
                            if players3[i][1] == "Разбойнік":
                                bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнт @" + players[p] + " помітив разбойніка @" + players[i])
                                die = random.randint(1,2)
                                if die == 1:
                                    rep = random.randint(1,4)
                                    if rep == 1:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнт @" + players[p] + " знищив очко разбойніка @" + players[i])
                                    if rep == 2:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнт @" + players[p] + " розтарабанив очко разбойніка @" + players[i])
                                    if rep == 3:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойнік @" + players[i] + " кінчив в штани коли його їбав мєнт @" + players[p])
                                    if rep == 4:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойніка @" + players[i] + " спіткала анальна кара мєнта @" + players[p])
                                    players3[i][2] = "Died"
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
                                    life = random.randint(1,4)
                                    if life == 1:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнт @" + players[p] + " промазав своїм пенісом і разбойнік @" + players[i] + " зірвався та втік")
                                    if life == 2:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойніку @" + players[i] + " вдалося уникнути пеніса мєнта @" + players[p])
                                    if life == 3:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнту @" + players[p] + " не вдалося піймати разбойніка @" + players[i])
                                    if life == 4:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойнік @" + players[i] + " в останній момент використав 'стан' і втік від мєнта @" + players[p])
                        if players3[p][1] == "Разбойнік":
                            if players3[i][1] == "Мер":
                                bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойнік @" + players[p] + " помітив мера @" + players[i])
                                die = random.randint(1,2)
                                if die == 1:
                                    rep = random.randint(1,4)
                                    if rep == 1:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойнік @" + players[p] + " знищив очко мера @" + players[i])
                                    if rep == 2:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойнік @" + players[p] + " розтарабанив очко мера @" + players[i])
                                    if rep == 3:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мер @" + players[i] + " кінчив в штани коли його їбав разбойнік @" + players[p])
                                    if rep == 4:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мера @" + players[i] + " спіткала анальна кара разбойніка @" + players[p])
                                    players3[i][2] = "Died"
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
                                    life = random.randint(1,4)
                                    if life == 1:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойнік @" + players[p] + " промазав своїм пенісом і мер @" + players[i] + " зірвався та втік")
                                    if life == 2:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Меру @" + players[i] + " вдалося уникнути пеніса разбойніка @" + players[p])
                                    if life == 3:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойніку @" + players[p] + " не вдалося піймати мера @" + players[i])
                                    if life == 4:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мер @" + players[i] + " в останній момент використав 'стан' і втік від разбойніка @" + players[p])
    raund()
    life = 1
    while 1:
        if len(players) > 5:
            for r in range(len(players)):
                for c in range(3):
                    if players3[r][c] == "Мер":
                        if players3[r][c+1] == "Died":
                            r = random.randint(1,2)
                            if life == 1:
                                if r == 1:
                                    players3[r][c+1] = None
                                    bot.send_mess(bot.get_chat_id(bot.last_update()), "Мер @" + players[r] + " платить за восcтановлєніє свого очка і повертається до гри")
                                    life = 0
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
                    bot.send_mess(bot.get_chat_id(bot.last_update()), players3[p][1] + " @" + players[p] + " зберіг своє очко та виграв" )
            players.clear()
            break
            return
        else:
            raund()
      
def start():
    offset = None
    while 1:
        bot.get_updates(offset)
        last_update = bot.last_update()
        if last_update is None:
            continue
        last_update_id = last_update['update_id']
        r = random.randint(1,23)
        rb = random.randint(1,3)
        igra = "Гра Ігра Игра Game Грать Плей Играть Іграть play гра ігра игра game грать плей играть іграть play"
        if bot.get_message(bot.last_update()) in igra:
            game_start()
        if rb == 1 and bot.get_username(bot.last_update()) == "zagin177":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"+", bot.get_message_id(bot.last_update()))
        if rb == 2 and bot.get_username(bot.last_update()) == "zagin177":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Согласен", bot.get_message_id(bot.last_update()))
        if rb == 3 and bot.get_username(bot.last_update()) == "zagin177":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Поддержую", bot.get_message_id(bot.last_update()))
        if r == 1 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпецюк поїш гамна", bot.get_message_id(bot.last_update()))
        if r == 2 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Я єбав тебе в рот, Шпетюк", bot.get_message_id(bot.last_update()))
        if r == 3 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпетюк блять", bot.get_message_id(bot.last_update()))
        if r == 4 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"продам тебе циганам", bot.get_message_id(bot.last_update()))
        if r == 5 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпетюк гавно своє їсть", bot.get_message_id(bot.last_update()))
        if r == 6 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"в рот собі насри", bot.get_message_id(bot.last_update()))
        if r == 7 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"ти обісраний", bot.get_message_id(bot.last_update()))
        if r == 8 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Хай шпетюк отсосе", bot.get_message_id(bot.last_update()))
        if r == 9 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпецюк", bot.get_message_id(bot.last_update()))
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Ти блатний як двері")
        if r == 10 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"а уїбать", bot.get_message_id(bot.last_update()))
        if r == 11 and bot.get_username(bot.last_update()) == "shputya":
            bot.forward_mess(bot.get_chat_id(bot.last_update()), bot.get_chat_id(bot.last_update()), bot.get_message_id(bot.last_update()))
            bot.send_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/4/42/Voice1.ogg")
        if r == 12 and bot.get_username(bot.last_update()) == "shputya":
            bot.forward_mess(bot.get_chat_id(bot.last_update()), bot.get_chat_id(bot.last_update()), bot.get_message_id(bot.last_update()))
            bot.send_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/c/cb/Voice2.ogg")
        if r == 13 and bot.get_username(bot.last_update()) == "shputya":
            bot.forward_mess(bot.get_chat_id(bot.last_update()), bot.get_chat_id(bot.last_update()), bot.get_message_id(bot.last_update()))
            bot.send_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/2/2e/Voice3.ogg")
        if r == 14 and bot.get_username(bot.last_update()) == "shputya":
            bot.forward_mess(bot.get_chat_id(bot.last_update()), bot.get_chat_id(bot.last_update()), bot.get_message_id(bot.last_update()))
            bot.send_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/b/b0/Voice4.ogg")
        if r == 15 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"ти овощ", bot.get_message_id(bot.last_update()))
        if r == 16 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Шпитя ти тупий", bot.get_message_id(bot.last_update()))
        if r == 17 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Ти дебіл шпитя", bot.get_message_id(bot.last_update()))
        if r == 18 and bot.get_username(bot.last_update()) == "shputya":
            bot.forward_mess(bot.get_chat_id(bot.last_update()), bot.get_chat_id(bot.last_update()), bot.get_message_id(bot.last_update()))
            bot.resend_voice(bot.get_chat_id(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/b/bf/Voice5.ogg")
        if r == 19 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Завали їбало", bot.get_message_id(bot.last_update()))
        if r == 20 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Пашол нахуй Шпитюк", bot.get_message_id(bot.last_update()))
        if r == 21 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Ти підарастіческа хуйня їбана", bot.get_message_id(bot.last_update()))
        if r == 22 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"Ти кріпак засраний", bot.get_message_id(bot.last_update()))
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Іди сіно кидай")
        if r == 23 and bot.get_username(bot.last_update()) == "shputya":
            
            bot.resend_mess(bot.get_chat_id(bot.last_update()),"ти загноение  підзалупного міра", bot.get_message_id(bot.last_update()))


        off = "Богдан, завали єбало Соси cоси Закрий єбало Завали єбало Богдан, закрий єбало Богдан, єбало офф Єбало офф off Пішов Богдан, нахуй ашол Богдан, нахуй пішов нахуй Пашол нахуй Іди нах Богдан, іди нах Іди нахуй Богдан, іди нахуй Богдан, сосни Сосни Богдан, пососи Пососи" 
        if bot.get_message(bot.last_update()) in off:
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Ок")
            offset = None
            break
        offset = last_update_id + 1
start()
offset = None
while 1:
    bot.get_updates(offset)
    last_update = bot.last_update()
    if last_update is None:
            continue
    last_update_id = last_update['update_id']
    on = "Бодька Богдан Бодя Бодька ти тут? Богдан ти тут? Бодя ти тут? Бодька проснись Богдан проснись Бодя проснись Бодька, ти тут? Богдан, ти тут? Бодя, ти тут? Бодька, проснись Богдан, проснись Бодя, проснись "
    if bot.get_message(bot.last_update()) in on:
        bot.send_mess(bot.get_chat_id(bot.last_update()),"Де Шпецюк блять")
        start()
    offset = last_update_id + 1
