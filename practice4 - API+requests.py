import requests
import time
import config


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = config.TOKEN
TEXT: str = 'Ура! Классный апдейт!'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    update = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    print(update)
    
    if update['result']:
        for result in update['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            query = f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}'
            print(query)

            requests.get(query)
            
    time.sleep(1)
    counter += 1