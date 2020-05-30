import requests
import json

class ESportBot():
    def __init__(self):
        self.u = "https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/getUpdates"      ##Ccылочка из которой получаем инфу

    def get_updates(self,offset=None, timeout=30):                ##Получаем все сообщения которые видит бот
        params = {'timeout': timeout, 'offset': offset}
        self.url = requests.get(self.u, params)
        jsonresponse = json.loads(self.url.text)
        return jsonresponse

    def last_update(self):                                          ##Получаем последнее сообщение
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
    
    def get_chat_id(self,update):                         ##Получить ид чата из последнего сообщения
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            return chat_id
        else:
            return None
        if 'edited_message' in update:
            chat_id = update['edited_message']['chat']['id']
            return chat_id
        else:
            return None
    def send_mess(self, chat, text):                 ##Отправить сообщение
        params = {'chat_id': chat, 'text': text}
        response = requests.post("https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/" + 'sendMessage', params)
        return response
    
    def resend_mess(self, chat, text, reply):  
        params = {'chat_id': chat, 'text': text, 'reply_to_message_id': reply}        ##Ответить на сообщение
        response = requests.post("https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/" + 'sendMessage', params)
        return response
    def send_mes(self, chat, text):                                   ##Также отправить сообщение, но если в сообщении много текста, пробелов и абзацов
        response = requests.post("https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/sendMessage?chat_id={}&text={}".format(chat, text))
        return response
    def send_voice(self, chat, voice, reply):                              ##Отправить голосовое сообщение
        params = {'chat_id': chat, 'voice': voice , 'reply_to_message_id': reply}
        response = requests.post("https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/" + 'sendVoice', params)
        return response
    def send_sticker(self, chat, sticker, reply):                                ##Отпрвить ответом стикер
        params = {'chat_id': chat, 'sticker': sticker , 'reply_to_message_id': reply}   
        response = requests.post("https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/" + 'sendSticker', params)
        return response
    def send_stick(self, chat, sticker):                            ##Просто отправить стикер
        params = {'chat_id': chat, 'sticker': sticker}
        response = requests.post("https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/" + 'sendSticker', params)
        return response
    def get_message(self,update):              ##Получить текст из последнего сообщения
        if 'message' in update:
            if 'text' in update['message']:
                chat_id = update['message']['text']
                return chat_id
            else:
                
                no = "non"
                return no
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
        else:
            no = "non"
            return no
    def get_message_id(self,update):                    ##Получить ид сообщения
        if 'message' in update:
            chat_id = update['message']['message_id']
            return chat_id
        if 'edited_message' in update:
            chat_id = update['edited_message']['message_id']
            return chat_id
    def get_username(self, update):                       ##Получить имя того кто отправил сообщение
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
    def get_id(self, update):               ##Получить ид того кто отправил сообщение
         if 'message' in update:
             if 'id' in update['message']['from']:
                chat_id = update['message']['from']['id']
                return chat_id
         if 'edited_message' in update:
             if 'id' in update['edited_message']['from']:
                chat_id = update['edited_message']['from']['id']
                return chat_id
def getMatch(matchid):
    match = requests.get("https://api.opendota.com/api/matches/{}?api_key=19674c39-adc9-4622-8af5-7050103d6964".format(matchid))
    jsonresp = json.loads(match.text)
    return jsonresp
def getProMatch():
    match = requests.get("https://api.opendota.com/api/proMatches?api_key=19674c39-adc9-4622-8af5-7050103d6964")
    jsonresp = json.loads(match.text)
    return jsonresp
leagues = ['RED STAR CUP','World E-sports Legendary League','Oceanic Esports Dota League','中国DOTA2职业联赛','ESL One Birmingham 2020 Online powered by Intel']
def getLastMatch(idchat, last_match, matchStats):
    league_name = matchStats['league']['name']
    if league_name in leagues:
        pass
    else:
        return
    radiant_team = "Noname"
    try:
        radiant_team = matchStats['radiant_team']['name']
    except:
        radiant_team = "Noname"
    radiant_score = matchStats['radiant_score']
    dire_team = "Noname"
    try:
        dire_team = matchStats['dire_team']['name']
    except:
        dire_team = "Noname"
    dire_score = matchStats['dire_score']
    duration = last_match[0]['duration']/60
    radiant_players = []
    dire_players = []
    for n in range(5):
        if (matchStats['players'][n]['name']) is None:
            radiant_players.append(matchStats['players'][n]['personaname'])
        else:
            radiant_players.append(matchStats['players'][n]['name'])
        for h in heroes:
            if h['id'] == matchStats['players'][n]['hero_id']:
                radiant_players.append(h['localized_name'])
        radiant_players.append(matchStats['players'][n]['kills'])
        radiant_players.append(matchStats['players'][n]['assists'])
        radiant_players.append(matchStats['players'][n]['deaths'])
        if (matchStats['players'][n+5]['name']) is None:
            dire_players.append(matchStats['players'][n+5]['personaname'])
        else:
            dire_players.append(matchStats['players'][n+5]['name'])
        for h in heroes:
            if h['id'] == matchStats['players'][n+5]['hero_id']:
                dire_players.append(h['localized_name'])
        dire_players.append(matchStats['players'][n+5]['kills'])
        dire_players.append(matchStats['players'][n+5]['assists'])
        dire_players.append(matchStats['players'][n+5]['deaths'])
    winner = 0
    if (matchStats['radiant_win']):
        winner = radiant_team
    else:
        winner = dire_team
    bot.send_mes(idchat, "\u2b50\u2b50\u2b50Лига:%20{}\u2b50\u2b50\u2b50%0A{}%20против%20{}%0AСилы%20Света:%20{}.%20Счёт:%20{}.%0AСилы%20Тьмы:%20{}.%20Счёт:%20{}.%0AПобедили:%20{}%0AПродолжительность:%20{}%20мин.%0A%0A{}:%0AИгрок%20-%20Герой%20-%20Убийства%20-%20Помощь%20-%20Смерти%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A%0A{}:%0AИгрок%20-%20Герой%20-%20Убийства%20-%20Помощь%20-%20Смерти%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}".format(league_name,radiant_team,dire_team,radiant_team,radiant_score,dire_team,dire_score,winner,str(round(duration,2)),radiant_team,radiant_players[0],radiant_players[1],radiant_players[2],radiant_players[3],radiant_players[4],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[5],radiant_players[6],radiant_players[7],radiant_players[8],radiant_players[9],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[10],radiant_players[11],radiant_players[12],radiant_players[13],radiant_players[14],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[15],radiant_players[16],radiant_players[17],radiant_players[18],radiant_players[19],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[20],radiant_players[21],radiant_players[22],radiant_players[23],radiant_players[24],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_team, dire_players[0],dire_players[1],dire_players[2],dire_players[3],dire_players[4],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[5],dire_players[6],dire_players[7],dire_players[8],dire_players[9],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[10],dire_players[11],dire_players[12],dire_players[13],dire_players[14],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[15],dire_players[16],dire_players[17],dire_players[18],dire_players[19],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[20],dire_players[21],dire_players[22],dire_players[23],dire_players[24]))
##    if bot.get_message(idchat) == "/AllLastMatchStats":
##        firstBloodTime = matchStats['first_blood_time']
    print('yes')
def update(token, id, **kwargs):
    data = json.dumps(kwargs)
    p = requests.post('https://write.as/api/posts' + "/%s" % id, data=data,
        headers={"Authorization": "Token %s" % token,
                "Content-Type":"application/json"})
    if p.status_code != 200:
        return "Error in updatePost(): %s" % p.json()["error_msg"]
def updateList(members):
    b = ''
    for k in members:
        b += str(k) + ','
    update('54e5b71b-8113-4381-4819-4b6e942e5b25', '3s53eqfuvys0y85q', body = (b))
heroes = json.loads(requests.get("https://api.opendota.com/api/heroes?api_key=19674c39-adc9-4622-8af5-7050103d6964").text)
r = requests.get("https://write.as/api/posts/3s53eqfuvys0y85q")
objects = json.loads(r.text)['data']['body']
members = []
k = ''
for o in objects:
    if o != ',':
        k +=str(o)
    else:
        members.append(int(k))
        k = ''
bot = ESportBot()          
offset = None
match_now = 0
print(members)
while 1:
    print(1)
    bot.get_updates(offset)     
    last_update = bot.last_update()
    last_match = getProMatch()
    matchStats = getMatch(last_match[0]['match_id'])
    if last_match[0]['match_id'] != match_now:
        for m in members:
            getLastMatch(m, last_match,matchStats)
        match_now = last_match[0]['match_id']
    if last_update is None:         
        continue
    last_update_id = last_update['update_id']
    if bot.get_message(last_update) == "/enablenews" or bot.get_message(last_update) == "/enablenews@dotaCyberGameBot":
        if bot.get_chat_id(last_update) in members:
            pass
        else:
            bot.send_mess(bot.get_chat_id(last_update),'Авто рассылка включена')
            members.append(bot.get_chat_id(last_update))
            updateList(members)
    if bot.get_message(last_update) == "/disablenews" or bot.get_message(last_update) == "/disablenews@dotaCyberGameBot":
        if bot.get_chat_id(last_update) in members:
            bot.send_mess(bot.get_chat_id(last_update),'Авто рассылка выключена')
            del members[members.index(bot.get_chat_id(last_update))]
            print(members)
            updateList(members)
    if bot.get_message(last_update) == "/lastmatchstats" or bot.get_message(last_update) == "/lastmatchstats@dotaCyberGameBot" or bot.get_message(last_update) == "/alllastmatchstats" or bot.get_message(last_update) == "/alllastmatchstats@dotaCyberGameBot":
        getLastMatch(bot.get_chat_id(last_update), last_match,matchStats)
    offset = last_update_id + 1
