from telegram.ext import CommandHandler


def make_gen_cmd(dispatcher):
    # Start 명령어
    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm Ready")

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

