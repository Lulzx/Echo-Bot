# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

print ("Python Bot By Lulzx")
print ("Lulzx Bot has been started.")

import telebot

API_TOKEN = '384742340:AAETgAQr48DrdczySb6gOCI0dmwHQeuKaM8'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Fuck off! 😒\
""")

@bot.message_handler(commands=['credits', 'about'])
def send_welcome(message):
    bot.reply_to(message, """Fuck off! 😒\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
#ArashEmp
