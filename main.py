from telegram import Bot
TOKEN ="6467582835:AAE0AQNGtJgiJs6sWWL9WRZbFM6EdfVpcMM"
bot=Bot(token=TOKEN)
user=bot.get_me()
print(user.first_name)