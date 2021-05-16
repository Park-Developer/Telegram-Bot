from telegram.ext import CommandHandler
import requests
from bs4 import BeautifulSoup
import json


def make_stock_cmd(dispatcher,stock_list:json):
    # Start 명령어
    def current_stock(update, context):
        '''
        :param selector: 조사하고자 하는 주식명(회사명 ,My_List ,ALL)
        :param stock_list: 주식리스트
        :return:
        '''

        currnet_stock_url=stock_list["Current Stock Price"]
        saved_stock_list = []
        for saved_stock in stock_list['Stock List']:
            saved_stock_list.append(list(saved_stock.keys())[0])

        print(saved_stock_list)
        # stock_code=stock_list[stock]

        '''
        result = requests.get(stock_url)
        bs_obj = BeautifulSoup(result.content, "html.parser")

        no_today = bs_obj.find("p", {"class": "no_today"})  # 태그 p, 속성값 no_today 찾기
        blind = no_today.find("span")  # 태그 span, 속성값 blind 찾기
        now_price = blind.text
        '''
        # return now_price
        if "LG디스플레이" in update.message.text:
            context.bot.send_message(chat_id=update.effective_chat.id, text="success")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="??")
    current_stock_handler = CommandHandler('current_stock', current_stock)
    dispatcher.add_handler(current_stock_handler)

