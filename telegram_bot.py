import telegram
import logging
from telegram.ext import CommandHandler
import logging
from telegram.ext import Updater
import json

import general_cmd
#import stock_cmd
import message_handle
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

class Telegram_bot():
    def __init__(self,address):
        self.initial_setting(address) # 봇 생성
        self.make_function() # 봇 기능 생성

    def initial_setting(self,address='C:\\Users\\gnvid\\PycharmProjects\\telegramBot'):
        # Telegram bot 정보 가져오기
        bot_json_addr = address+'\\mybot.json'
        with open(bot_json_addr, 'r', encoding='UTF8') as f1:
            self.bot_json = json.load(f1)

        self.my_token=self.bot_json["token"]
        self.updater = Updater(token=self.my_token, use_context=True)
        self.bot = telegram.Bot(token=self.my_token)
        self.dispatcher = self.updater.dispatcher

        # 내 주식 정보 가져오기
        stock_list_addr = address+'\\stock_list.json'
        with open(stock_list_addr, 'r', encoding='UTF8') as f2:
            self.stock_json = json.load(f2)

        self.currnet_stock_url = self.stock_json["Current Stock Price"]

    def make_function(self):
        # [메세지 핸들러]

        # 저장된 주식 List 만들기
        self.saved_stock_list={}
        for saved_stock in self.stock_json['Stock List']:
            self.saved_stock_list[list(saved_stock.keys())[0]]=list(saved_stock.values())[0]

        message_handle.make_msg_response(self.dispatcher,self.saved_stock_list,self.currnet_stock_url )

        # 일반 명령어 작성
        general_cmd.make_gen_cmd(self.dispatcher)
        
        # 주식 관련 명령어 작성(자동 모니터링 기능)
        #stock_cmd.make_stock_cmd(self.dispatcher)


