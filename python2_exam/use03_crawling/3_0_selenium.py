# 웹드라이버 설치 불필요함
from selenium import webdriver

driver = webdriver.Chrome()

URL='https://search.naver.com/search.naver?query=환율'
driver.get(url=URL)

input()
