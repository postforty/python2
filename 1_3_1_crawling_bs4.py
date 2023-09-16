# pip install BeautifulSoup4
# pip install requests
import requests
from bs4 import BeautifulSoup
import re

url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bkEw&pkid=68&os=5664043&qvt=0"
param = {"query": "영화 기생충 리뷰"}
response = requests.get(url, params=param)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# print(soup)

review_list = soup.find_all("span", class_="this_text")

# print(review_list)

for review in review_list:
    result = re.sub('<span class="this_text">|</span>', "", str(review))
    result = re.sub("&lt;", "<", str(result))
    result = re.sub("&gt;", ">", str(result))
    print(result)
