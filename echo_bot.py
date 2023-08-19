from telegram import Bot
from time import sleep
TOKEN ="6467582835:AAE0AQNGtJgiJs6sWWL9WRZbFM6EdfVpcMM"
bot=Bot(token=TOKEN)
message=bot.get_updates()[-1].message.text
print(message)
while True:
    last_message=bot.get_updates()[-1].message.text
    chat_id=bot.get_updates()[-1].message.chat.id
    if message!=last_message:
        bot.send_message(chat_id,last_message)
        message=last_message
    print(message)
    sleep(1)