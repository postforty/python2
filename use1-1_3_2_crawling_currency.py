# pip install requests
import requests

# pip install beautifulsoup4
from bs4 import BeautifulSoup

def get_exchange_rate():
    # headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "text/html; charset=utf-8"}

    url = "https://search.naver.com/search.naver"
    param = param = {"query": "환율"}
    response = requests.get(url, params=param)

    # text는 수신한 byte단위의 데이터를 자동으로 decode 하여 사용자가 보기 좋게 만들어주며, content는 수신한 byte단위의 데이터를 있는 그대로 보여줍니다.
    # query.content는 겉으로 보기에는 무슨 말인지 알아보기 힘든 문장이 나열되어 있습니다. 하지만 가장 처음에 있는 b에서 알 수 있듯이 이 문자들은 모두 바이트 단위의 문자들입니다.
    # 그렇기에 1바이트인 ASCII(알파벳)은 그대로 출력하지만 2바이트 문자인 한글은 저런 식으로 깨져서 나오게 됩니다.

    # content = BeautifulSoup(response.content, "html.parser")
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)

    ul = soup.find('ul', class_='list_item _panel')
    li_list = ul.find_all('li')

    result = []

    for li in li_list:
        # print(li)
        if li.find('span'):
            # print(li.find('span').text)
            # print(li.find('strong').text)
            # (국가, 문자열 환율, 실수 환율)
            result.append((li.find('span').text, li.find('strong').text, float(li.find('strong').text.replace(",", ""))))

    # [('미국', '1,304.00', 1304.0), ('일본', '919.90', 919.9), ('유럽연합', '1,424.10', 1424.1), ('중국', '182.75', 182.75), ('영국', '1,657.78', 1657.78), ('호주', '872.38', 872.38)]
    # print(result)

    print("=" * 30)
    # print("{0:|^25}".format(" 환율 변환기 "))
    print(f"{'환율 변환기':|^25}")
    print("=" * 30)

    for idx, val in enumerate(result):
        print(f"{idx + 1})", val[0], end=": ")
        print(val[1], "KRW")

    print("=" * 30)

    no = int(input("변환을 원하는 통화를 선택해 주세요: ")) - 1
    amount = int(input(f"변환하고자하는 {result[no][0]} 금액을 입력해 주세요: "))

    # JPY 100
    if result[no][0] == "일본":
        print(
            '일본 JPY 100 변환 결과: ',
            # "{:0,.2f}".format(result[no][2] * amount / 100),
            f"{result[no][2] * amount / 100:0,.2f}",
            "KRW",
        )
    # 그외 통화
    else:
        print(f'{result[no][0]} 변환 결과: ',
            # "{:0,.2f}".format(result[no][2] * amount),
            f"{result[no][2] * amount:0,.2f}",
            "KRW",
        )

get_exchange_rate()
