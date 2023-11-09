import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from io import BytesIO

def weather_chart():
    response = requests.get("https://www.weather.go.kr/w/obs-climate/land/city-obs.do")
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', id='weather_table')

    data = []
    for tr in table.find_all('tr'):
        tds = list(tr.find_all('td'))

        for td in tds:
            if td.find('a'):
                point = td.find('a').text
                temperature = float(tds[5].text)
                humidity = int(tds[10].text)

                data.append([point, temperature, humidity])

    df = pd.DataFrame(data, columns=["point", "temperature", "humidity"])

    df.set_index("point", inplace=True)

    city_df = df.loc[['부산', '서울', '인천', '대전', '대구', '울산', '제주']]

    font_path = r'C:\Windows\Fonts\batang.ttc'
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)
    
    ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
    ax.set_xlabel('도시', fontsize=12)
    ax.set_ylabel('기온/습도', fontsize=12)
    ax.legend(['기온', '습도'], fontsize=12)

    img = BytesIO()
    plt.savefig(img, format="png")

    plt.close()

    return img.getvalue()

if __name__ == "__main__":
    weather_chart()
