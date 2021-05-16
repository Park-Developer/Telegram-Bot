import telegram_bot
from telegram.ext import CommandHandler

info_file_address='C:\\Users\\gnvid\\PycharmProjects\\telegramBot'

wonho_bot=telegram_bot.Telegram_bot(info_file_address)


wonho_bot.updater.start_polling()