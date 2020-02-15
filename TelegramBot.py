import requests
import json
import random

class BogdanBot():

    def __init__(self):
        self.u = "https://api.telegram.org/bot1081045084:AAHpRmSel3SgRpHPtSaWCQCG7vWe6l-RGeE/getUpdates"

    def get_updates(self,offset=None, timeout=30):
        params = {'timeout': timeout, 'offset': offset}
        self.url = requests.get(self.u, params)
        jsonresponse = json.loads(self.url.text)
        return jsonresponse

    def last_update(self):  
        results = self.get_updates()['result']
        total_updates = len(results) - 1
        return results[total_updates]
    
    def get_chat_id(self,update):  
        chat_id = update['message']['chat']['id']
        return chat_id
    
    def get_chat_sp(self,update):  
        chat_id = update['message']['chat']['id']
        if update['message']['from']['username'] == "wotrex" and update['message']['chat']['type'] == "group" :
            return chat_id
    def get_message_id(self,update):  
        chat_id = update['message']['message_id']
        return chat_id

    def send_mess(self, chat, text):  
        params = {'chat_id': chat, 'text': text}
        response = requests.post("https://api.telegram.org/bot1081045084:AAHpRmSel3SgRpHPtSaWCQCG7vWe6l-RGeE/" + 'sendMessage', data=params)
        return response
    def send_voice(self, chat, voice):  
        params = {'chat_id': chat, 'voice': voice}
        response = requests.post("https://api.telegram.org/bot1081045084:AAHpRmSel3SgRpHPtSaWCQCG7vWe6l-RGeE/" + 'sendVoice', data=params)
        return response
    def get_message(self,update):
        if 'text' in update['message']:
            chat_id = update['message']['text']
            return chat_id

bot = BogdanBot()
offset = None
def start():
    lastupdate = bot.get_message_id(bot.last_update())
    while 1:
        bot.get_updates()
        last_update = bot.last_update()
        last_update_id = last_update['update_id']
        if lastupdate != bot.get_message_id(bot.last_update()):
            lastupdate = bot.get_message_id(bot.last_update())
            r = random.randint(1,14)
            if r == 1:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"Шпецюк поїш гамна")
            if r == 2:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"Я єбав тебе в рот, Шпетюк")
            if r == 3:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"Шпетюк блять")
            if r == 4:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"@wotrex, продам тебе циганам")
            if r == 5:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"Шпетюк гавно своє їсть")
            if r == 6:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"@wotrex, в рот собі насри")
            if r == 7:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"@wotrex, ти обісраний")
            if r == 8:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"Хай шпетюк отсосе")
            if r == 9:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"Шпецюк")
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"Ти блатний як двері")
            if r == 10:
                bot.send_mess(bot.get_chat_sp(bot.last_update()),"@wotrex, а уїбать")
            if r == 11:
                bot.send_voice(bot.get_chat_sp(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/4/42/Voice1.ogg")
            if r == 12:
                bot.send_voice(bot.get_chat_sp(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/c/cb/Voice2.ogg")
            if r == 13:
                bot.send_voice(bot.get_chat_sp(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/2/2e/Voice3.ogg")
            if r == 14:
                bot.send_voice(bot.get_chat_sp(bot.last_update()),"https://upload.wikimedia.org/wikipedia/commons/b/b0/Voice4.ogg")
        rand = random.randint(1,2000)
        if rand == 100:
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Ми не підтримуємо булінг")
        if bot.get_message(bot.last_update()) == "Богдан, завали єбало":
            bot.send_mess(bot.get_chat_id(bot.last_update()),"Ок")
            offset = None
            break
        offset = last_update_id + 1
start()
while 1:        
    if bot.get_message(bot.last_update()) == "Бодька":
        bot.send_mess(bot.get_chat_id(bot.last_update()),"Де Шпецюк блять")
        start()
