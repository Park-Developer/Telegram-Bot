import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=034220"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content,"html.parser")

no_today = bs_obj.find("p", {"class": "no_today"})  # 태그 p, 속성값 no_today 찾기
blind = no_today.find("span")  # 태그 span, 속성값 blind 찾기
now_price = blind.text

print(now_price)