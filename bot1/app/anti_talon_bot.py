import logging
from telegram.ext import Updater, \
    CommandHandler, \
    ConversationHandler, \
    RegexHandler, MessageHandler, Filters
import sys
sys.path.append("../src")
import constants
import main_comands

logging.basicConfig(format='%(asctime)s - \
                    %(name)s - \
                    %(levelname)s - \
                    %(message)s',
                    level=logging.INFO)

SUBJECT, NEXT_QUESTION = range(2)


def main():
    updater = Updater(token=constants.TOKEN)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', main_comands.start)],

        states={

            SUBJECT: [RegexHandler('^(History|Math)$', main_comands.subject)],

            NEXT_QUESTION: [MessageHandler(Filters.text, main_comands.subject)]

        },

        fallbacks=[CommandHandler('cancel', main_comands.cancel)]
    )
    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(
        CommandHandler("help", main_comands.help_me))
    updater.dispatcher.add_handler(
        CommandHandler("start", main_comands.start))
    updater.dispatcher.add_handler(
        CommandHandler("stop", main_comands.stop))

    updater.dispatcher.add_handler(CommandHandler(
        "invite", main_comands.invite_friend))
    updater.start_polling()

    updater.idle()


logger = logging.getLogger(__name__)
if __name__ == "__main__":
    main()
