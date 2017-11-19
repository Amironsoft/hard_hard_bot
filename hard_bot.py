import telebot
from config import token
from yandex_market_explorer import find

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    otext = "Hello! I'm bot for hardware search!\nSend me what you want and I'll find it 😎"
    bot.send_message(message.chat.id, otext)


@bot.message_handler(content_types=["text"])
def run_action(message):
    itext = message.text
    otext = 'empty'

    print(message.chat.username, message.text)
    if itext == 'Hello hard_hard_bot!':
        otext = rf'Congratulations {message.chat.username}!'
        print(otext)
    elif itext == 'Hi!':
        otext = 'Hello, ' + message.chat.username + '!'
    elif itext == 'stop_bot':
        # bot.stop_polling()
        pass
    else:
        otext = find(itext.replace(" ", "%20"))

    print("\t\t\t" + otext)
    bot.send_message(message.chat.id, otext)


if __name__ == '__main__':
    bot.polling(none_stop=True)
