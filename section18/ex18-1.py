from bs4 import BeautifulSoup
import requests
import re

url = 'https://search.naver.com/search.naver?'
param = {'query':'영화 기생충 리뷰'}
response = requests.get(url, params=param)
html = response.text
soup = BeautifulSoup(html, "html.parser")

result_list = []
for v in soup.find_all("span", class_="this_text"):
    result_list.append(v.text)

# review_list = soup.find_all("span", class_="this_text")[0].text
# print(review_list)

# result_list = []
# for review in review_list:
#     result = re.sub('<span class="this_text">', '', str(review))
#     result = re.sub('</span>', '', str(result))
#     result = re.sub('&lt;', '<', str(result))
#     result = re.sub('&gt;', '>', str(result))
#     result_list.append(result)

for i, v in enumerate(result_list):
    print(f'{i+1}. {v}')

