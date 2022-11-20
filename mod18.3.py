# import telebot
#
TOKEN = "5982358558:AAFULmytTZjUTLADL3pczHVIDQVchmfTOUE"
#
# bot = telebot.TeleBot(TOKEN)
#
# bot.polling(none_stop=True)


# import telebot
#
# TOKEN = "Токен полученный при регистрации"
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(filters)
# def function_name(message):
#     bot.reply_to(message, "This is a message handler")

# import telebot
#
# bot = telebot.TeleBot("TOKEN")
#
#
# # Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     pass

import telebot

bot = telebot.TeleBot("TOKEN")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, f'Все хорошо, {message.chat.username}')


#bot.polling(none_stop=True)
