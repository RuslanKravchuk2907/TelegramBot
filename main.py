import telebot
import webbrowser

bot = telebot.TeleBot("8052382991:AAGHDKY1gwapQzBje0pVM4PFkXZrGq6-wnM")


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://github.com/RuslanKravchuk2907')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello!, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id)


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello!, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
