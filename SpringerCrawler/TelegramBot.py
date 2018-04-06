from telegram.ext import Updater, ConversationHandler

def hello(bot, update):
    mess = update.message.from_user
    print(mess.type)

updater = Updater("526937126:AAHL_XAMbxUlmjmyHsRHHThqiA-21WNRik0")

updater.dispatcher.add_handler(ConversationHandler())

updater.start_polling()
updater.idle()