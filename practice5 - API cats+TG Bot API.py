import requests
import time
import config


API_URL: str = 'https://api.telegram.org/bot'
API_URL_CONTENT = 'https://randomfox.ca/floof/'
BOT_TOKEN: str = config.TOKEN
TEXT: str = 'Ура! Классный апдейт!'
MAX_COUNTER: int = 100
ERROR_TEXT: str = 'Здесь должна была быть картинка :(\nПопробуйте написать еще раз!'

offset: int = -2
counter: int = 0
chat_id: int

while True:
    
    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет
    
    update = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    print(update)
    
    if update['result']:
        for result in update['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            
            content_response = requests.get(f'https://randomfox.ca/floof/')
            print(content_response)            
            if content_response.status_code == 200:
#                 content_response = requests.get(f'https://randomfox.ca/floof/').json()
                content_url = content_response.json()['image']
                query = f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={content_url}'
                print(query)            
            else:
                query = f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}'
                print(query)            

            requests.get(query)
            
    time.sleep(1)
    counter += 1
    if counter == MAX_COUNTER:
        break