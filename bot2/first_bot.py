#
#
# # import telebot
# # import time
# #
# # bot_token='717137801:AAGA4AM4E3aQiVgz0-do2CAZSmGw4uCLD1o'
# #
# # bot = telebot.TeleBot(token=bot_token)
# #
# # @bot.message_handler(commands=["start"])
# #
# # def send_welcome(message):
# #     bot.reply_to(message, "Welcome")
# #
# # bot.polling()
#
#
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# TOKENAI = 'd521d76a1c74455e8bd1d2714b44bfa6'
# import logging
# import json
# import apiai
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater
# from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
#
#
# updater = Updater(token='717137801:AAGA4AM4E3aQiVgz0-do2CAZSmGw4uCLD1o')
#
# # send request from user to the bot
# dispatcher = updater.dispatcher
#
# # eliminate errors
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# # function that we call for waking the bot up
# def start(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
#
#     keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
#                  InlineKeyboardButton("Option 2", callback_data='2')],
#
#                 [InlineKeyboardButton("Option 3", callback_data='3')]]
#
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Please choose:', reply_markup=reply_markup)
#
#
# def help_function(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="You have a problem...")
#
#
# # function that prints with caps lock
# def caps(bot, update, args):
#     text_caps = ' '.join(args).upper()
#     bot.send_message(chat_id=update.message.chat_id, text=text_caps)
#
# # function that read the message and return the same
# def echo(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
#
#
# def textMessage(bot, update):
#     request = apiai.ApiAI(TOKENAI).text_request() # Токен API к Dialogflow
#     request.lang = "en" # На каком языке будет послан запрос
#     request.session_id = 'SofiiasBot' # ID Сессии диалога (нужно, чтобы потом учить бота)
#     request.query = update.message.text # Посылаем запрос к ИИ с сообщением от юзера
#     responseJson = json.loads(request.getresponse().read().decode('utf-8'))
#     response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
#     # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
#     if response:
#         bot.send_message(chat_id=update.message.chat_id, text=response)
#     else:
#         bot.send_message(chat_id=update.message.chat_id, text='I missunderstand you!')
#
#
# def button(bot, update):
#     query = update.callback_query
#
#     bot.edit_message_text(text="Selected option: {}".format(query.data),
#                           chat_id=query.message.chat_id,
#                           message_id=query.message.message_id)
#
# def error(bot, update, error):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, error)
#
# # set command to wake the bot "start"/"kkk"
# start_handler = CommandHandler('start', start)
# # dispatcher.add_handler(start_handler)
# updater.dispatcher.add_handler(CallbackQueryHandler(button))
# updater.dispatcher.add_error_handler(error)
# # set command to to write sth after the command "/help"
# help_handler = CommandHandler('help', help_function)
# dispatcher.add_handler(help_handler)
# # caps lock
# caps_handler = CommandHandler('caps', caps, pass_args=True)
# dispatcher.add_handler(caps_handler)
# # # read text from user
# # echo_handler = MessageHandler(Filters.text, echo)
# # dispatcher.add_handler(echo_handler)
# txt_mes = MessageHandler(Filters.text, textMessage)
# dispatcher.add_handler(txt_mes)
# # run the bot (here can be "clean=True")
# updater.start_polling()
# # stop the bot with "cntrl + c"
# updater.idle()
# #
# #
# #
# # if __name__ == '__main__':
# #     main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO = range(4)


def start(bot, update):
    reply_keyboard = [['Boy', 'Girl', 'Other']]

    update.message.reply_text(
        'Hi! My name is Professor Bot. I will hold a conversation with you. '
        'Send /cancel to stop talking to me.\n\n'
        'Are you a boy or a girl?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER


def gender(bot, update):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('I see! Please send me a photo of yourself, '
                              'so I know what you look like, or send /skip if you don\'t want to.',
                              reply_markup=ReplyKeyboardRemove())

    return PHOTO


def photo(bot, update):
    user = update.message.from_user
    photo_file = bot.get_file(update.message.photo[-1].file_id)
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text('Gorgeous! Now, send me your location please, '
                              'or send /skip if you don\'t want to.')

    return LOCATION


def skip_photo(bot, update):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text('I bet you look great! Now, send me your location please, '
                              'or send /skip.')

    return LOCATION


def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
                user_location.longitude)
    update.message.reply_text('Maybe I can visit you sometime! '
                              'At last, tell me something about yourself.')

    return BIO


def skip_location(bot, update):
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text('You seem a bit paranoid! '
                              'At last, tell me something about yourself.')

    return BIO


def bio(bot, update):
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("717137801:AAGA4AM4E3aQiVgz0-do2CAZSmGw4uCLD1oN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER: [RegexHandler('^(Boy|Girl|Other)$', gender)],

            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],

            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('skip', skip_location)],

            BIO: [MessageHandler(Filters.text, bio)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
