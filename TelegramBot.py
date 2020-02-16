import requests
import json
import random

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
##        total_updates = len(results) - 1
##        return results[total_updates]
    
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

bot = BogdanBot()
def start():
    offset = None
    while 1:
        bot.get_updates(offset)
        last_update = bot.last_update()
        if last_update is None:
            continue
        last_update_id = last_update['update_id']
        r = random.randint(1,18)
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

        rand = random.randint(1,2000)
        if rand == 100:
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Ми не підтримуємо булінг")
        if bot.get_message(bot.last_update()) == "Богдан, завали єбало" or bot.get_message(bot.last_update()) == "Соси" or bot.get_message(bot.last_update()) == "Закрий єбало" or bot.get_message(bot.last_update()) == "Завали єбало" or bot.get_message(bot.last_update()) == "Богдан,закрий єбало" or bot.get_message(bot.last_update()) == "єбало офф" or bot.get_message(bot.last_update()) == "єбало off " or bot.get_message(bot.last_update()) == "Пішов нахуй Богдан" or bot.get_message(bot.last_update()) == "Пішов нахуй" or  bot.get_message(bot.last_update()) == "Пашол нахуй Богдан" or bot.get_message(bot.last_update()) == "Пашол нахуй" or bot.get_message(bot.last_update()) == "Бодя іди нах" or bot.get_message(bot.last_update()) == "іди нах" or bot.get_message(bot.last_update()) == "Бодя іди нахуй" or bot.get_message(bot.last_update()) == "Іди нахуй" or bot.get_message(bot.last_update()) == "Богдан іди нахуй" or bot.get_message(bot.last_update()) == "Богдан пішов нахуй" or bot.get_message(bot.last_update()) == "Богдан пашол нахуй" or bot.get_message(bot.last_update()) == "Shut up" or bot.get_message(bot.last_update()) == "Сосни" or bot.get_message(bot.last_update()) == "Пососи" or bot.get_message(bot.last_update()) == "Пососи ок?" or bot.get_message(bot.last_update()) == "Пососеш ок?" :
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
    if bot.get_message(bot.last_update()) == "Бодька" or bot.get_message(bot.last_update()) == "Богдан" or bot.get_message(bot.last_update()) == "Бодя" or bot.get_message(bot.last_update()) == "Бодька ти тут?" or bot.get_message(bot.last_update()) == "Богдан ти тут?" or bot.get_message(bot.last_update()) == "Бодя ти тут?" or (bot.last_update()) == "Бодька проснись" or bot.get_message(bot.last_update()) == "Богдан проснись" or bot.get_message(bot.last_update()) == "Бодя проснись":
        bot.send_mess(bot.get_chat_id(bot.last_update()),"Де Шпецюк блять")
        start()
    offset = last_update_id + 1
