import telegram
import logging
from telegram.ext import CommandHandler
from telegram.ext import Updater

# Stock Related Module
import stock_gen_func
import stock_command

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

my_token = '1395535281:AAF2bNWr5YVhPhMreL-PU58qEQMx-BF-IYE'


updater = Updater(token=my_token, use_context=True)

wono_bot = telegram.Bot(token=my_token)
dispatcher = updater.dispatcher

import requests
from bs4 import BeautifulSoup
import json

def current_stock(update, context):
    '''
    :param selector: 조사하고자 하는 주식명(회사명 ,My_List ,ALL)
    :param stock_list: 주식리스트
    :return:
    '''

    json_addr='C:\\Users\\gnvid\\PycharmProjects\\telegramBot\\stock_list.json'
    with open(json_addr, 'r', encoding='UTF8') as f:
        json_data = json.load(f)

    stock_list=json_data #N 이 부분 따로 처리필요
    data_url = "https://finance.naver.com/item/main.nhn?code=" #N 이 부분 따로 처리필요
    #stock_code=stock_list[stock]
    stock_url="https://finance.naver.com/item/main.nhn?code=034220"

    result = requests.get(stock_url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    no_today = bs_obj.find("p", {"class": "no_today"})  # 태그 p, 속성값 no_today 찾기
    blind = no_today.find("span")  # 태그 span, 속성값 blind 찾기
    now_price = blind.text

    #return now_price
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(now_price))

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

current_stock_handler= CommandHandler('current_stock',current_stock)
dispatcher.add_handler(current_stock_handler)


updater.start_polling()

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    json_addr='C:\\Users\\gnvid\\PycharmProjects\\telegramBot\\stock_list.json'
    with open(json_addr, 'r', encoding='UTF8') as f:
        json_data = json.load(f)
    if "LG디스플레이" in update.message.text:

        context.bot.send_message(chat_id=update.effective_chat.id, text=json_data["LG디스플레이"])

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

