import requests
from pprint import pprint
from time import sleep
# Set telegram bot token
TOKEN ="6467582835:AAE0AQNGtJgiJs6sWWL9WRZbFM6EdfVpcMM"
from time import sleep

base_url = f"https://api.telegram.org/bot{TOKEN}"

# Define a function to get updates from telegram bot

def send_dog_photo(chat_id,caption=''):
    url="https://random.dog/woof.json"
    t=requests.get(url)
    photo=t.json()['url']
    params={
        'chat_id':chat_id,
        'photo':photo,
        'caption':caption
    }
    update = requests.get(f"{base_url}/sendPhoto",params=params)
    return update.status_code
def get_updates():
    url = f"{base_url}/getUpdates"
    response = requests.get(url)
    return response.json()

# Define a function to send message to telegram bot

def send_message(chat_id,text):
    params = {
        'chat_id':chat_id,
        'text':text
    }
    update = requests.get(f"{base_url}/getUpdates",params=params)
    data = update.json()
    return data['result']

def send_message(chat_id, text):

    dog = {
        'text': "Dog🐶"
        #'text': "Dog"
    }
    cat = {
        'text': 'Cat😺'
    }

    keyboard = [
        [dog, cat],

    ]

    keyboard = {
        'keyboard': keyboard,
        'resize_keyboard':True,

    }

    parameters = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        'reply_markup': keyboard
    }
    r = requests.get(f"{base_url}/sendMessage", json=parameters)
    return r.json()

pprint(get_updates())

last_message_id = -1

while True:
    msgs = get_updates()
    last_msg = msgs['result'][-1]

    message_id = last_msg['message']['message_id']

    chat_id = last_msg['message']['chat']['id']
    text = last_msg['message']['text']

    print(last_message_id, message_id)

    if last_message_id != message_id:

        if text == '/start':
            send_message(chat_id, "Welcome to Echo Bot!")
        elif text=="Dog🐶":
            send_dog_photo(chat_id)
        else:
            send_message(chat_id, text)

        last_message_id = message_id
    sleep(2)