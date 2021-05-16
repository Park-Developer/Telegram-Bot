from telegram.ext import MessageHandler, Filters
import stock_function # 주식관련 기능 모음 모듈



def make_msg_response(dispatcher,saved_stock_list,data_url):
    # 현재 주가 return
    def current_stock(update, context):
        is_find=False
        for saved_stock in saved_stock_list.keys():
            if saved_stock in update.message.text:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Find")
                stock_code=saved_stock_list[saved_stock]

                current_price=stock_function.currnet_stock(data_url,stock_code)
                context.bot.send_message(chat_id=update.effective_chat.id, text=current_price)
                is_find = True
                break

        if is_find==False:  # 주식 정보를 못찾았을 경우 
            context.bot.send_message(chat_id=update.effective_chat.id, text="??")
            
    
    # Command가 아닌 말에 대해서만 반응
    current_stock_handler = MessageHandler(Filters.text & (~Filters.command), current_stock)
    dispatcher.add_handler(current_stock_handler)



