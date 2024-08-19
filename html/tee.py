import telegram
from telegram.ext import Updater, CommandHandler

Token = "7370739341:AAHWXeHf8kGCsTGxSU9_ulAt42fRXogc3II"

updater = Updater(token=Token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("hello, welcome to hareg bot")

def help(update, context):
    update.message.reply_text(
        """
        /start -> welcome to the channel
        /help -> this particular message
        /content -> about various playlists of hareg bot
        /python -> the first video from python playlist
        /SQL -> the first video from SQL playlist
        /java -> the first video from java playlist
        /contact -> contact information
        """
    )

def content(update, context):
    update.message.reply_text("")

def python(update, context):
    update.message.reply_text("link below that is useful for you: https://bit.ly/4dYXJ2p")

def SQL(update, context):
    update.message.reply_text("link below that is useful for you: https://github.com/AlexTheAnalyst")

def java(update, context):
    update.message.reply_text("link below that is useful for you: https://courses.supersimple.dev/courses/html-css")

def contact(update, context):
    update.message.reply_text("you can contact me on cell phone 0966798482")

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('content', content))
dispatcher.add_handler(CommandHandler('python', python))
dispatcher.add_handler(CommandHandler('SQL', SQL))
dispatcher.add_handler(CommandHandler('java', java))
dispatcher.add_handler(CommandHandler('contact', contact))

updater.start_polling()
updater.idle()