import requests

# pip install beautifulsoup4
from bs4 import BeautifulSoup
import pandas as pd  # 데이터 처리
import matplotlib.pyplot as plt  # IDLE, 파이썬 인터프리터에서 그래프 표시
from io import BytesIO


def weather_chartjs():
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
                # 차트에서 사용할 수 있도록 문자열을 실수, 정수로 각각 변경해야 함
                temperature = float(tds[5].text)
                humidity = int(tds[10].text)

                data.append([point, temperature, humidity])

    # print(data)

    df = pd.DataFrame(data, columns=["point", "temperature", "humidity"])
    df.set_index("point", inplace=True)
    city_df = df.loc[["서울", "인천", "대전", "대구", "광주", "부산", "울산"]]
    # print(city_df)
    
    result = [city_df.index.tolist()] + city_df.values.T.tolist()
    # print(result)

    return result

if __name__ == "__main__":
    weather_chartjs()
