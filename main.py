import telebot
from telebot import types

bot = telebot.TeleBot("8052382991:AAGHDKY1gwapQzBje0pVM4PFkXZrGq6-wnM")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Go to the site')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Delete text')
    btn3 = types.KeyboardButton('Add text')
    markup.row(btn2, btn3)
    file = open('./pic.jpg', 'rb')
    # bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Hello!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Go to the site':
        bot.send_message(message.chat.id, "Site is open")
    elif messsage.text == 'Delete photo':
        bot.send_message(message.chat.id, "Photo is deleted")

@bot.message_handler(commands=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go to the site', url='https://github.com/RuslanKravchuk2907')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete text', calllback_data='delete')
    btn3 = types.InlineKeyboardButton('Add text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Nice', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'add':
        bot.edit_message_text('Add text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)
