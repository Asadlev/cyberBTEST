from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcomme to Bot!')

def main():
    updater = Updater("7310054959:AAFCsMzHo9VSpeEbkmwLqqIpkKJ1lmHf_I8")
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

