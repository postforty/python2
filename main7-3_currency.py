#pip install requests
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import re

def get_exchange_rate():
# def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    # response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    response = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=7&acq=%ED%99%98%EC%9C%A8&qdt=0&ie=utf8&query=%ED%99%98%EC%9C%A8", headers=headers)
    # print(response.content)
    content = BeautifulSoup(response.content, 'html.parser')
    # print(content)
    # containers = content.find('span', {"data-test":"instrument-price-last"})
    # content1 = content.find('div', 'rate_table_bx _table')
    containers = content.select('div > table > tbody > tr > td > span')

    country = ['미국', '일본', '유럽연합', '중국', '영국', '호주', '캐나다', '뉴질랜드']
    currency = []

    for idx, val in enumerate(containers):
        if idx % 4 == 0:
            result = re.sub('<span>|</span>','', str(val))
            currency.append(result)
    
    for idx, val in enumerate(country):
        print(val, end=' ')
        print(currency[idx])

# get_exchange_rate('usd', 'krw')
get_exchange_rate()
