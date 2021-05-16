import requests
from bs4 import BeautifulSoup

def currnet_stock(url_data,stock_code):
    data_url=url_data+stock_code
    result = requests.get(data_url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    no_today = bs_obj.find("p", {"class": "no_today"})  # 태그 p, 속성값 no_today 찾기
    blind = no_today.find("span")  # 태그 span, 속성값 blind 찾기
    now_price = blind.text
    return now_price

