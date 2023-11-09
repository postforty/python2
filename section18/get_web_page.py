from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/section18/html_ex.html'
# param = {'query':'파이썬'}
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# print(soup.find('a').get('href'))

for i in range(len(soup.find_all('li'))):
    print(soup.find_all('li')[i].text)

print(soup.find_all('div', class_='container')[0].text)