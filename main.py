import logging

import telegram

import search
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = '5256719525:AAFR0Zouz-j5R-OWLAqES7M2ZVc3QHYYn0o'



def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True)
    )



def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text='Use <b>/news</b> command', parse_mode=telegram.ParseMode.HTML)


def news(update:Update, context: CallbackContext)-> None:
    text = search.getNews()
    title = search.getTitle()
    link = search.getLink()
    link_t = 'href="{0}"'.format(link)
    update.message.reply_text(text='<b>{0}</b>'.format(title), parse_mode=telegram.ParseMode.HTML)
    update.message.reply_text(text)
    update.message.reply_text(link)



#def echo(update: Update, context: CallbackContext):
 #   update.message.reply_text(update.message.text)


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # on different commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("news", news))

    #on non command
  #  dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    #start
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()