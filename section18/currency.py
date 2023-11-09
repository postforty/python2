from bs4 import BeautifulSoup
import requests
import re

url = 'https://search.naver.com/search.naver?'
param = {'query':'환율'}
response = requests.get(url, params=param)
html = response.text
soup = BeautifulSoup(html, "html.parser")

containers = []
for i in soup.select("table > tbody > tr > td > span"):
    containers.append(i.get_text())

# print(containers)

country = []
for i in soup.select("table > tbody > tr > th > a > span"):
    country.append(i.get_text())

currency_str = []
currency_float = []
for i, v in enumerate(containers):
    if i % 4 == 0:
        currency_str.append(v)
        currency_float.append(float(re.sub(",",'', v)))

print("="*30)
print("{0:|^25}".format(" 환율 변환기 "))
print("="*30)

for i, v in enumerate(country):
    print(f'{i+1}. {v}', end=': ')
    print(f'{currency_str[i]}원')

print("="*30)

select_no = int(input("변환을 원하는 통화를 선택해 주세요 >>> "))-1
amount = int(input("변환하고자하는 금액을 입력해 주세요 >>> "))

if country[select_no][-3:] == '100':
    print(f'변환 결과: {"{:0,.2f}".format((currency_float[select_no] * amount)/100)}원')
else:
    print(f'변환 결과: {"{:0,.2f}".format(currency_float[select_no] * amount)}원')