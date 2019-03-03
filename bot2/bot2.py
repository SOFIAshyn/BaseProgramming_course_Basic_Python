from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    print(update.from_user.message_id)
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('762218447:AAFNKR2dCJDPOpFdvyuD0132bX8n9-FBuvE')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
