from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler
from random import randint as rd
import wikipedia

wikipedia.set_lang('ru')


bot = Bot(token='5526894010:AAFBcgw5hMjr43-SOtltgA-hoozs1obo3as')
updater = Updater(token='5526894010:AAFBcgw5hMjr43-SOtltgA-hoozs1obo3as')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Hello')

def rand(update, context):
    context.bot.send_message(update.effective_chat.id, f'{rd(1, 100)}')


def wiki(update, context):
    text = ' '.join(context.args)
    result = wikipedia.summary(text, sentences=2)
    context.bot.send_message(update.effective_chat.id, result)


start_handler = CommandHandler('start', start)
random_handler = CommandHandler('random', rand)
wiki_handler = CommandHandler('wiki', wiki)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(wiki_handler)


updater.start_polling()
updater.idle() #ctrl + z