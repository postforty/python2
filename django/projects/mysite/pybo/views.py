from django.shortcuts import render
from django.views import View
import requests
from bs4 import BeautifulSoup


def index(request):
    return render(request, "pybo/base.html")


def qr(request):
    return render(request, "pybo/qr.html")


def home(request):
    return render(request, "pybo/home.html")


def chart(request):
    # https://www.weather.go.kr/ > 관측기후 > 육상 > 도시별관측
    response = requests.get("https://www.weather.go.kr/w/obs-climate/land/city-obs.do")
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", id="weather_table")

    data = []
    for tr in table.find_all("tr"):
        tds = list(tr.find_all("td"))

        for td in tds:
            if td.find("a"):
                point = td.find("a").text
                temperature = tds[5].text
                humidity = tds[10].text

                data.append([point, temperature, humidity])

    selected_cities = []
    for i in data:
        if i[0] in ["서울", "인천", "대전", "대구", "광주", "부산", "울산"]:
            selected_cities.append(i)

    city_name_list = []
    temperature_list = []
    humidity_list = []
    print(selected_cities)
    for i in selected_cities:
        city_name_list.append(i[0])
        # 온도, 습도 값의 타입 실수형으로 변경
        temperature_list.append(float(i[1]))
        humidity_list.append(float(i[2]))

    context = {"chart_data": [city_name_list, temperature_list, humidity_list]}
    print(context)
    return render(request, "pybo/chart.html", context)
