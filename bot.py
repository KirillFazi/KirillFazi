import telebot
import random

TOKEN = "587169154:AAHrF-djNcOGOI2NE1Evjq8jtL80dipvUpE"
bot = telebot.TeleBot(TOKEN)

joke = ['''
Царь позвал к себе Иванушку-дурака и говорит:
– Если завтра не принесешь двух говорящих птиц – голову срублю.
Иван принес филина и воробья. Царь говорит:
– Ну, пусть что-нибудь скажут.
Иван спрашивает:
– Воробей, почем раньше водка в магазине была?
Воробей:
– Чирик.
Иван филину:
– А ты, филин, подтверди.
Филин:
– Подтверждаю.
''']

accept_list = ['Не подтверждаю', 'Подтверждаю']
fil = list(set(range(15)))


@bot.message_handler(func=lambda message: message, content_types=['text'])
def accept(message):
    if 'подтверди' in message.text:
        bot.send_message(message.chat.id, random.choice(accept_list))
    if random.choice(fil) == 5:
        bot.send_message(message.chat.id, 'Угу')


bot.polling()








