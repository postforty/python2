# pip install requests
import requests

# pip install beautifulsoup4
from bs4 import BeautifulSoup
import re


def get_exchange_rate():
    headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "text/html; charset=utf-8"}

    url = "https://search.naver.com/search.naver"
    # print(response.content)
    param = {"acq": "환율", "query": "환율"}
    response = requests.get(url, params=param)
    content = BeautifulSoup(response.content, "html.parser")
    # print(content)
    containers = content.select("div > table > tbody > tr > td > span")
    # print(containers)

    country = [
        "미국 USD",
        "일본 JPY 100",
        "유럽연합 EUR",
        "중국 CNY",
        "영국 GBP",
        "호주 AUD",
        "캐나다 CAD",
        "뉴질랜드 NZD",
    ]
    currency_str = []
    currency_float = []

    for idx, val in enumerate(containers):
        if idx % 4 == 0:
            result = re.sub("<span>|</span>", "", str(val))
            currency_str.append(result)
            currency_float.append(float(re.sub(",", "", result)))

    # print(currency_str)

    print("=" * 30)
    print("{0:|^25}".format(" 환율 변환기 "))
    print("=" * 30)

    for idx, val in enumerate(country):
        print(f"{idx + 1})", val, end=": ")
        print(currency_str[idx], "KRW")

    print("=" * 30)

    select_no = int(input("변환을 원하는 통화를 선택해 주세요: ")) - 1
    amount = int(input("변환하고자하는 금액을 입력해 주세요: "))

    # JPY 100
    if country[select_no][-3:] == "100":
        print(
            f'{"{:0,.2f}".format(amount)} {country[select_no]} 변환 결과: ',
            "{:0,.2f}".format(currency_float[select_no] * amount / 100),
            "KRW",
        )
    # 그외 통화
    else:
        print(
            f'{"{:0,.2f}".format(amount)} {country[select_no]} 변환 결과: ',
            "{:0,.2f}".format(currency_float[select_no] * amount),
            "KRW",
        )


get_exchange_rate()
