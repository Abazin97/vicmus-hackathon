import telebot as tg
from telebot import types
from config import bot
from info import phr
from time import sleep

bot.send_voice
n = ''
#bot.send_photo

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, phr['greet'])
    
    
@bot.message_handler(commands=['stop_polling'])
def stop(msg):
    global n
    kbd = types.InlineKeyboardMarkup()
    kbd.add(types.InlineKeyboardButton(text='Да', callback_data='y'))
    kbd.add(types.InlineKeyboardButton(text='Отмена', callback_data='n'))
    t = bot.reply_to(msg, 'Остановить бота?', reply_markup = kbd)
    print(t)
    n = t
    

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "y":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
    elif call.data == "n":
        bot.send_message(call.message.chat.id, 'Kk')




if __name__ == '__main__':
    while True:
        try:

            bot.polling(none_stop=True)
        except Exception as err:
            print('Произошла ошибка: {}'.format(err))
            sleep(5)
            