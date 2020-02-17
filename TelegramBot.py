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
    bot.send_mess(bot.get_chat_id(bot.last_update()),"Почалася гра МЕР МЄНТИ І РАЗБОЙНІКИ. Правила гри: МЕР повинен трахнути МЄНТІВ, МЄНТИ повинні трахнути РОЗБІЙНИКІВ, РОЗБІЙНИКИ повинні трахнути МЕРА. Кожен повинен зберегти своє очко. Хто зберіг своє очко - той виграв. Все відбувається рандомно. Ви можете тіки подивитись результати. Щоб прийняти участь в грі відправте: + . Щоб почати гру(коли наберуться учасники) відправте: Старт або Start. Щоб закінчити гру: Стоп або Stop")
    while 1:
        bot.get_updates(offset)
        last_update = bot.last_update()
        if last_update is None:
            continue
        last_update_id = last_update['update_id']
        if bot.get_message(bot.last_update()) == "+":
            a = 0
            b = 0
            for r in range(len(rate)):
                if rate[r][0] == bot.get_username(bot.last_update()):
                    b = "Є"
            if b != "Є":
                for u in range(len(rate)):
                    if rate[u][0] == None:
                        rate[u][0] = bot.get_username(bot.last_update())
                        rate2[u][0] = u
                        rate2[u][1] = 0
                        rate2[u][2] = 0
                        rate2[u][3] = 0
                        break
            for p in players:
                if p == bot.get_username(bot.last_update()):
                    a = "Є"
            if a != "Є":
                players.append(bot.get_username(bot.last_update()))
                bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + bot.get_username(bot.last_update()) + " бере участь в грі")
            else:
                bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + bot.get_username(bot.last_update()) + ", ти вже приймаєш участь в грі")

        if bot.get_message(bot.last_update()) == "list":
            bot.send_mess(bot.get_chat_id(bot.last_update()), "Список гравців:")
            for p in players:
                bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + p)
        if bot.get_message(bot.last_update()) == "Рейтинг":
            bot.send_mess(bot.get_chat_id(bot.last_update()), "Рейтинг гравців:")
            for p in range(len(rate)):
                if rate[p] != None and rate2[p][1] != None and rate2[p][2] != None and rate2[p][3] != None:
                    bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + rate[p][0] + " : " + "Виграв ігор - " + str(rate2[p][1]) + ". Кількість знищених ворожих анусів - " + str(rate2[p][2]) + ". Кількість разів коли втратив анальну дєвствєнность - " + str(rate2[p][3])  )

        if bot.get_message(bot.last_update()) == "Старт" or bot.get_message(bot.last_update()) == "Start":
           # bot.send_mess(bot.get_chat_id(bot.last_update()), "Гра ще не написана)")
          # if len(players) >= 2:
           game()
           break
          #     game()
           #    break
         #  else:
         #      bot.send_mess(bot.get_chat_id(bot.last_update()), "Мало гравців(Мінімум 2)")


        if bot.get_message(bot.last_update()) == "Стоп" or bot.get_message(bot.last_update()) == "Stop":
            bot.send_mess(bot.get_chat_id(bot.last_update()), "Гру відмінено")
            players.clear()
            break
        offset = last_update_id + 1

def game():
    rand = random.randint(1,3)
    countP = 0
    countR = 0
    countM = 0
    players3 = np.empty((20,3), dtype="object")
    for p in range(len(players)):
        players3[p][0] = players[p]
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

    for k in range(len(players)):      
        bot.send_mess(bot.get_chat_id(bot.last_update()), "@" + players3[k][0] + " - " + players3[k][1])
    for p in range(len(players)):
        if players3[p][2] != "Died":
            for i in range(len(players)):
                if i != p and players3[i][2] != "Died":
                    if players3[p][1] == "Мер":
                        if players3[i][1] == "Мер":
                            a = True
                        if players3[i][1] == "Мєнт":
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
                                a = True
                        if players3[i][1] == "Разбойнік":
                            a = True
                    if players3[p][1] == "Мєнт":
                        if players3[i][1] == "Мер":
                            a = True
                        if players3[i][1] == "Мєнт":
                            a = True
                        if players3[i][1] == "Разбойнік":
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
                                a = True
                    if players3[p][1] == "Разбойнік":
                        if players3[i][1] == "Мер":
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
                                a = True
                        if players3[i][1] == "Мєнт":
                            a = True
                        if players3[i][1] == "Разбойнік":
                            a = True
    for p in range(len(players)):
        if players[p] in rate:
            for h in range(len(rate)):
                if rate[h][0] == players[p]:
                    rate2[h][1] = rate2[h][1] + 1
                    break
                
    for p in range(len(players)):
        if players3[p][2] != "Died":
            bot.send_mess(bot.get_chat_id(bot.last_update()), players3[p][1] + " @" + players[p] + " зберіг своє очко та виграв" )
    players.clear()
    return
      
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

        rand = random.randint(1,1000)
        if rand == 100:
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Ми не підтримуємо булінг")
        if bot.get_message(bot.last_update()) == "Богдан, завали єбало" or bot.get_message(bot.last_update()) == "Соси" or bot.get_message(bot.last_update()) == "Закрий єбало" or bot.get_message(bot.last_update()) == "Завали єбало" or bot.get_message(bot.last_update()) == "Богдан,закрий єбало" or bot.get_message(bot.last_update()) == "єбало офф" or bot.get_message(bot.last_update()) == "єбало off " or bot.get_message(bot.last_update()) == "Пішов нахуй Богдан" or bot.get_message(bot.last_update()) == "Пішов нахуй" or  bot.get_message(bot.last_update()) == "Пашол нахуй Богдан" or bot.get_message(bot.last_update()) == "Пашол нахуй" or bot.get_message(bot.last_update()) == "Бодя іди нах" or bot.get_message(bot.last_update()) == "іди нах" or bot.get_message(bot.last_update()) == "Бодя іди нахуй" or bot.get_message(bot.last_update()) == "Іди нахуй" or bot.get_message(bot.last_update()) == "Богдан іди нахуй" or bot.get_message(bot.last_update()) == "Богдан пішов нахуй" or bot.get_message(bot.last_update()) == "Богдан пашол нахуй" or bot.get_message(bot.last_update()) == "Shut up" or bot.get_message(bot.last_update()) == "Сосни" or bot.get_message(bot.last_update()) == "Пососи" or bot.get_message(bot.last_update()) == "Пососи ок?" or bot.get_message(bot.last_update()) == "Пососеш ок?" :
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Ок")
            offset = None
            break
        if bot.get_message(bot.last_update()) == "Игра" or bot.get_message(bot.last_update()) == "Ігра" or bot.get_message(bot.last_update()) == "Game":
            game_start()
        offset = last_update_id + 1
start()
offset = None
while 1:
    bot.get_updates(offset)
    last_update = bot.last_update()
    if last_update is None:
            continue
    last_update_id = last_update['update_id']
    if bot.get_message(bot.last_update()) == "Бодька" or bot.get_message(bot.last_update()) == "Богдан" or bot.get_message(bot.last_update()) == "Бодя" or bot.get_message(bot.last_update()) == "Бодька ти тут?" or bot.get_message(bot.last_update()) == "Богдан ти тут?" or bot.get_message(bot.last_update()) == "Бодя ти тут?" or (bot.last_update()) == "Бодька проснись" or bot.get_message(bot.last_update()) == "Богдан проснись" or bot.get_message(bot.last_update()) == "Бодя проснись":
        bot.send_mess(bot.get_chat_id(bot.last_update()),"Де Шпецюк блять")
        start()
    offset = last_update_id + 1
