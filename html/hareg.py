import telegram.ext
from telegram.ext import Updater, CommandHandler
Token="7370739341:AAHWXeHf8kGCsTGxSU9_ulAt42fRXogc3II"

updater=telegram.ext.Updater("toke=Token",Use_context=True)
dispatcher=updater.dispatcher

def satr(update, context):
    update.message.reply_text("hello wellcome to hareg bot")
    
def help(update,context):
    update.message.reply_text(
        """
        /start-> wellcome to the chanal
        /help->this particular message
        /contet->about various playlist of hareg bot
        /python->the first video from python playlist
        /SQL->the first video from SQL playlist
        /java->the first video from java playlist
        /contact->contact information
        """
    )
    
def centent(update,context):
        update.message.reply_text("")
        
def python(update,context):
        update.message.reply_text("link belew tha useful for you: https://bit.ly/4dYXJ2p")
        
def SQ(update,context):
        update.message.reply_text("link belew tha useful for you:https://github.com/AlexTheAnalyst ")
        
def java(update,context):
        update.message.reply_text("link belew tha useful for you:https://courses.supersimple.dev/courses/html-css") 
        
def centact(update,context):
        update.message.reply_text("you can contact me on cell phone 0966798482")
        
dispatcher.add_handler(telegram.ext.CommandHandler('start,start'))   
dispatcher.add_handler(telegram.ext.CommandHandler('python,python'))  
dispatcher.add_handler(telegram.ext.CommandHandler('SQLSQL'))
dispatcher.add_handler(telegram.ext.CommandHandler('java,java'))
dispatcher.add_handler(telegram.ext.CommandHandler('contact,contact'))
dispatcher.add_handler(telegram.ext.CommandHandler('help,help'))
    
updater.start_polling()
updater.idle()
    