import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=%EA%B3%A0%EC%96%91%EC%9D%B4&sca_esv=3b4249385fa7053d&hl=ko&source=hp&biw=1920&bih=1073&ei=jflvZ_NdnajT6Q_WxY-BCQ&iflsig=AL9hbdgAAAAAZ3AHnQ5-5eNgeNaDKToLT33PU13pasGY&ved=0ahUKEwiz2N_MxcqKAxUd1DQHHdbiI5AQ4dUDCBA&uact=5&oq=%EA%B3%A0%EC%96%91%EC%9D%B4&gs_lp=EgNpbWciCeqzoOyWkeydtDIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyBRAAGIAEMggQABiABBixAzILEAAYgAQYsQMYgwFIyCBQ2w5Ykh5wBHgAkAEBmAGmAaAB7QqqAQMwLjm4AQPIAQD4AQGKAgtnd3Mtd2l6LWltZ5gCBqACsgWoAgDCAgcQABiABBgKwgIEEAAYA5gDAZIHAzIuNKAHySo&sclient=img&udm=2"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

print(soup)

