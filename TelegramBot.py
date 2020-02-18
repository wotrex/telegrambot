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
        chat_id = update['message']['chat']['id']
        return chat_id
    
    def get_chat_sp(self,update):  
        chat_id = update['message']['chat']['id']
        if update['message']['from']['id'] == 395942614 and (update['message']['chat']['type'] == "group" or update['message']['chat']['type'] == "supergroup") :
            return chat_id
    def get_chat_bog(self,update):  
        chat_id = update['message']['chat']['id']
        if update['message']['from']['username'] == 'zagin177' and (update['message']['chat']['type'] == "group" or update['message']['chat']['type'] == "supergroup") :
            return chat_id
    def send_mess(self, chat, text):  
        params = {'chat_id': chat, 'text': text}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'sendMessage', params)
        return response
    def send_mes(self, chat, text):  
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/sendMessage?chat_id={}&text={}".format(chat, text))
        return response
    def send_voice(self, chat, voice):  
        params = {'chat_id': chat, 'voice': voice}
        response = requests.post("https://api.telegram.org/bot1061329648:AAFzLR4YTveVjLFSZb6cGcy5ze2TZRw8fbU/" + 'sendVoice', params)
        return response
    def get_message(self,update):
        if 'text' in update['message']:
            chat_id = update['message']['text']
            return chat_id
    def get_username(self, update):  
        chat_id = update['message']['from']['username']
        return chat_id

bot = BogdanBot()
players = []
rate = np.empty((20,1), dtype="object")
rate2 = np.empty((20,4), dtype="object")
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
        countP = 0
        countR = 0
        countM = 0
        for p in range(len(players)):
            if rand == 1:
    ##            bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + p + " обрав Мєнта")
                if countP < (countR + 1) or countR == countP:
                    players3[p][1] = "Мєнт"
                    countP = countP + 1
                    rand = random.randint(1,3)
                else:
                    players3[p][1] = "Разбойнік"
                    countR = countR + 1
                    rand = random.randint(1,3)
            if rand == 2:
    ##            bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + p + " обрав Розбійника")
                if countR < (countP + 1) or countR == countP:
                    players3[p][1] = "Разбойнік"
                    countR = countR + 1
                    rand = random.randint(1,3)
                else:
                    players3[p][1] = "Мєнт"
                    countP = countP + 1
                    rand = random.randint(1,3)
            if rand == 3:
    ##            bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + p + " обрав Мера")
                if countM == 0:
                    players3[p][1] = "Мер"
                    countM = countM + 1
                    rand = random.randint(1,3)
                else:
                    rand2= random.randint(1,2)
                    if rand == 1:
                        players3[p][1] = "Мєнт"
                        countP = countP + 1
                        rand = random.randint(1,3)
                    if rand == 2:
                        players3[p][1] = "Разбойнік"
                        countR = countR + 1
                        rand = random.randint(1,3)
    storonu()
    if len(players) == 2:
        if players3[0][1] == players3[1][1]:
            storonu()

    if len(players) == 3:
        if players3[0][1] == players3[1][1] or players3[0][1] == players3[2][1] or players3[1][1] == players3[2][1]:
            storonu()

    for k in range(len(players)):
        if players3[k][0] != None and players3[k][1] != None:
            bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + players3[k][0] + " - " + players3[k][1])
    def raund():
        for p in range(len(players)):
            if players3[p][2] != "Died":
                for i in range(len(players)):
                    if i != p and players3[i][2] != "Died":
                        if players3[p][1] == "Мер":
                            if players3[i][1] == "Мер":
                                a = True
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
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мер @" + players[p] + " промазав своїм пенісом і мєнт @" + players[i] + "зірвався та втік")
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
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мєнт @" + players[p] + " промазав своїм пенісом і разбойнік @" + players[i] + "зірвався та втік")
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
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойнік @" + players[p] + " промазав своїм пенісом і мер @" + players[i] + "зірвався та втік")
                                    if life == 2:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Меру @" + players[i] + " вдалося уникнути пеніса разбойніка @" + players[p])
                                    if life == 3:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Разбойніку @" + players[p] + " не вдалося піймати мера @" + players[i])
                                    if life == 4:
                                        bot.send_mess(bot.get_chat_id(bot.last_update()), "Мер @" + players[i] + " в останній момент використав 'стан' і втік від разбойніка @" + players[p])
    raund()
    while 1:
        if "Died" in players3:
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
        if rb == 1:
            bot.send_mess(bot.get_chat_bog(bot.last_update()),"+")
        if rb == 2:
            bot.send_mess(bot.get_chat_bog(bot.last_update()),"Согласен")
        if rb == 3:
            bot.send_mess(bot.get_chat_bog(bot.last_update()),"Поддержую")
        if r == 1:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Шпецюк поїш гамна")
        if r == 2:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Я єбав тебе в рот, Шпетюк")
        if r == 3:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Шпетюк блять")
        if r == 4:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"@shputya, продам тебе циганам")
        if r == 5:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Шпетюк гавно своє їсть")
        if r == 6:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"@shputya, в рот собі насри")
        if r == 7:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"@shputya, ти обісраний")
        if r == 8:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Хай шпетюк отсосе")
        if r == 9:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Шпецюк")
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Ти блатний як двері")
        if r == 10:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"@shputya, а уїбать")
        if r == 11:
            bot.send_voice(bot.get_chat_sp(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/4/42/Voice1.ogg")
        if r == 12:
            bot.send_voice(bot.get_chat_sp(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/c/cb/Voice2.ogg")
        if r == 13:
            bot.send_voice(bot.get_chat_sp(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/2/2e/Voice3.ogg")
        if r == 14:
            bot.send_voice(bot.get_chat_sp(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/b/b0/Voice4.ogg")
        if r == 15:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"@shputya, ти овощ")
        if r == 16:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Шпитя ти тупий")
        if r == 17:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Ти дебіл шпитя")
        if r == 18:
            bot.send_voice(bot.get_chat_sp(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/b/bf/Voice5.ogg")
        if r == 19:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Завали їбало")
        if r == 20:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Пашол нахуй Шпитюк")
        if r == 21:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Ти підарастіческа хуйня їбана")
        if r == 22:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Ти кріпак засраний")
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"Іди сіно кидай")
        if r == 23:
            bot.send_mess(bot.get_chat_sp(bot.last_update()),"@shputya ти загноение  підзалупного міра")

        rand = random.randint(1,500)
        if rand == 100:
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Ми не підтримуємо булінг")
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
