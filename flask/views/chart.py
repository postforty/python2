import requests

# pip install beautifulsoup4
from bs4 import BeautifulSoup
import pandas as pd  # 데이터 처리
import matplotlib.pyplot as plt  # IDLE, 파이썬 인터프리터에서 그래프 표시
from io import BytesIO


def weather_chart():
    # https://www.weather.go.kr/ > 관측기후 > 육상 > 도시별관측
    response = requests.get("https://www.weather.go.kr/w/obs-climate/land/city-obs.do")
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", id="weather_table")

    table

    data = []
    for tr in table.find_all("tr"):
        tds = list(tr.find_all("td"))

        for td in tds:
            if td.find("a"):
                point = td.find("a").text
                temperature = float(tds[5].text)
                humidity = int(tds[10].text)

                data.append([point, temperature, humidity])

    # print(data)

    df = pd.DataFrame(data, columns=["point", "temperature", "humidity"])
    df.set_index("point", inplace=True)
    city_df = df.loc[["서울", "인천", "대전", "대구", "광주", "부산", "울산"]]
    print(city_df)

    # Windows 한글 폰트 설정
    # pip install matplotlib
    from matplotlib import font_manager, rc

    # AttributeError: module 'matplotlib' has no attribute 'font_manager' 에러가 발생하면 해당 코드를 주석 처리한 후 실행한 후, 주석 해제 후 다시 실행하면 됨
    # .get_name() 누락 주의!!!
    font_path = "C:/Windows/Fonts/HYGPRM.TTF"
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc("font", family=font_name)

    # 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
    ax = city_df.plot(kind="bar", title="날씨", figsize=(12, 4), legend=True, fontsize=12)
    ax.set_xlabel("도시", fontsize=12)  # x축 정보 표시
    ax.set_ylabel("기온/습도", fontsize=12)  # y축 정보 표시
    ax.legend(["기온", "습도"], fontsize=12)  # 범례 지정

    # 차트 이미지 생성
    img = BytesIO()
    plt.savefig(img, format="png")

    # img.seek(0)

    plt.close()

    return img.getvalue()


if __name__ == "__main__":
    weather_chart()
