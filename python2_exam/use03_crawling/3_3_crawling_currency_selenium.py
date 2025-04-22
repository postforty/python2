# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# ! 창 숨기는 옵션 추가
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("headless")

# * case1 : chromedriver_autoinstaller
# * pip install chromedriver-autoinstaller
# import chromedriver_autoinstaller
# driver = webdriver.Chrome(service=ChromeService(chromedriver_autoinstaller.install()), options=chrome_options) # !창 숨기는 옵션 추가
# driver = webdriver.Chrome(service=ChromeService(chromedriver_autoinstaller.install()))

# * case2 : 웹드라이버 무설치
# driver = webdriver.Chrome(options=chrome_options) # ! 창 숨기는 옵션 추가
driver = webdriver.Chrome()

URL='https://search.naver.com/search.naver?query=환율'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10) # 10초안에 웹페이지를 load 하면 바로 넘어가거나, 10초를 기다림

# dt 태그 찾기
dt_elements = driver.find_elements(By.CSS_SELECTOR,"dt span")

# dd 태그 찾기
dd_elements = driver.find_elements(By.CSS_SELECTOR,"dd span strong")

# 결과를 저장할 리스트 초기화
result = []

# dt 태그와 dd 태그의 텍스트 추출하여 리스트에 저장
for dt, dd in zip(dt_elements, dd_elements):
    if dt.text:
        result.append((dt.text, dd.text, float(dd.text.replace(",", ""))))

# 다음 탭 렌더링
elem = driver.find_element(By.CSS_SELECTOR, "a.cmm_pg_next.on")
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(time_to_wait=10)

# dt 태그 찾기
dt_elements = driver.find_elements(By.CSS_SELECTOR,"dt span")

# dd 태그 찾기
dd_elements = driver.find_elements(By.CSS_SELECTOR,"dd span strong")

for dt, dd in zip(dt_elements, dd_elements):
    if dt.text:
        result.append((dt.text, dd.text, float(dd.text.replace(",", ""))))

# 결과 출력
print(result)

# 환율 변환기 코드
print("=" * 30)
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

