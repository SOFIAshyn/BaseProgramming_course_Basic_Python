from telegram import ReplyKeyboardMarkup
import questions
from telegram.ext import ConversationHandler
import sys
import constants
sys.path.append("../app/")
import anti_talon_bot


chosen_sub = ""
count_run = 0

def start(bot, update):
    reply_keyboard = [[i for i in constants.storage_subject[1]]]

    update.message.reply_text(
        """Хей, {}!
        Я - Antitalon Bot🤖
        Я допоможу тобі у підготовці до іспитів!📝
        У тебе є можливість обрати один з напрямів - \
Історія або Дискретна математика⚡️.
        Покращуй свої скіли в будь-який момент завдяки тестам! \
А за кожну правильну відповідь отримуй бали - джеджорики або щербинчики💰
         Крім цього, кожного дня спостерігай за своїм місцем та місцем \
учасника у Leaderboard!

        У тебе є кілька можливостей:
        ✨пропускати питання,якщо не знаєш відповіді  (проте пам'ятай, \
що за кожне пропущене питання
        у тебе зменшиться кількість балів на 10,а за кожні 3 \
пропущені питання - на 50)
        ✨спостерігати за рейтингом

        Якщо ти хочеш дізнатись більше про команди, то пиши
        /help""".format(update.message.from_user.first_name),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                         one_time_keyboard=True))

    return anti_talon_bot.SUBJECT


def subject(bot, update):
    global chosen_sub
    global count_run
    update.message.reply_text("Ти вибрав: ")
    constants.OPINION = update.message.text
    if count_run > 0:
        check_right = questions.correct_answer(constants.storage_subject[2],
                                               constants.OPINION)
    else:
        check_right = ""
    update.message.reply_text(update.message.text + check_right)
    if update.message.text.strip() == "History":
        chosen_sub = "../src/datastorage/history.json"
    elif update.message.text == "Math":
        chosen_sub = "../src/datastorage/discret.json"
    constants.gl_chosen_sub = chosen_sub

    constants.storage_subject = questions.run_question(chosen_sub)
    reply_keyboard = [[i for i in constants.storage_subject[1]]]
    update.message.reply_text(
        constants.storage_subject[0],
        reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                         one_time_keyboard=True))
    count_run += 1
    return anti_talon_bot.NEXT_QUESTION


def cancel(bot, update):
    user = update.message.from_user
    anti_talon_bot.logger.info(
        "User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.')
    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    anti_talon_bot.logger.warning(
        'Update "%s" caused error "%s"', update, error)


def help_me(bot, update):
    update.message.reply_text(
        """Я можу допомогти тобі не отримати талон.😎
        Ось тобі перелік команд, які ти можеш використовувати:

        /start - розпочати гру
        /help - отримати ще раз правила і команди
        /invite - можливість запросити друзів😉
        /leaderboard - можливість побачити рейтинг гравців""")


def invite_friend(bot, update):
    update.message.reply_text(
        """Хочеш запросити друга, {}😏?

        Поділись цим лінком зі своїми друзями😋:
        https://t.me/AntiTalonBot
        """.format(update.message.from_user.first_name))


def stop(bot, update):
    update.message.reply_text(
        """Ти зупинив гру((
        Ось тобі перелік команд, які ти можеш використовувати:

        /start - розпочати гру
        /help - отримати ще раз правила і команди
        /stop - зупинити подачу питань
        /invite - можливість запросити друзів😉
        /leaderboard - можливість побачити рейтинг гравців""")

#
# def leaderboard(bot, update):
#     update.message.reply_text(
#         "{}".format((update.message.from_user.first_name)+ " " + constants.DJEJORYKY+ " " + constants.SHCHERBYNSHI))
