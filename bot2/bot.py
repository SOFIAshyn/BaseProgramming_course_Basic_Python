import telebot

bot_token = '702491109:AAFD8erNpexdx0aCVbW-GkOIANNCCDdG_I0a'

bot = telebot.TeleBot(token=bot_token)

def find_at(msg):
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome! \n Write /help for info ')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Write an instagram username with @ and get a link!')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    f = open('input.txt', 'a', encoding='utf-8')
    f.write(str(message.from_user))
    f.write('\n')
    f.write(str(message.text))
    f.write('\n')
    f.write('---------\n')
    f.close()
    texts = message.text.split()
    at_text = find_at(texts)
    bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))
@bot.message_handler(func=lambda msg: msg.text is not None and '@' not in msg.text)
def at_answer(message):
    f = open('input.txt', 'a', encoding='utf-8')
    f.write(str(message.from_user))
    f.write('\n')
    f.write(str(message.text))
    f.write('\n')
    f.write('---------\n')
    f.close()

bot.polling()
