# pip install BeautifulSoup4
# pip install requests
import requests
from bs4 import BeautifulSoup
import re

# 웹 브라우저와 웹 서버 간에 정보를 주고받을 때, URL에는 ASCII 문자만 사용 가능
# URL 인코딩(Percent Encoding)은 이러한 제한을 극복하기 위한 방법
# [동작 순서]
# 1. 문자를 ASCII 코드 포인트로 변환
# 2. ASCII 코드 포인트를 16진수로 표현
# 3. 16진수 앞에 '%'를 붙여 URL에 사용 가능한 형태로 만듦
url = "https://search.naver.com/search.naver"
param = {"query": "영화 기생충 리뷰"}
response = requests.get(url, params=param)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# print(soup)

review_list = soup.find_all("span", class_="this_text")

# print(review_list)

# for review in review_list:
#     result = re.sub('<span class="this_text">|</span>', "", str(review))
#     result = re.sub("&lt;", "<", str(result))
#     result = re.sub("&gt;", ">", str(result))
#     print(result)

for review in review_list:
    # result = review.text
    result = review.get_text()
    print(result)
