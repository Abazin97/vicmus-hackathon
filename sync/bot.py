import telebot as tg
from telebot import types
from config import bot
from info import phr
from time import sleep


@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, phr['greet'])
    
    
@bot.message_handler(commands=['stop_polling'])
def stop(msg):
    kbd = types.InlineKeyboardMarkup()
    kbd.add(types.InlineKeyboardButton(text='Да', callback_data='y'))
    kbd.add(types.InlineKeyboardButton(text='Отмена', callback_data='n'))
    bot.reply_to(msg, 'Остановить бота?', reply_markup = kbd)

    

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "y":
        bot.stop_bot()
    elif call.data == "n":
        bot.send_message(call.message.chat.id, 'Ok')




if __name__ == '__main__':
    while True:
        try:
            print('Новый запуск бота.')
            bot.polling(none_stop=True)
        except Exception as err:
            print('Произошла ошибка: {}'.format(err))
            sleep(5)
            
