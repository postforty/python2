'''
크롤링
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 브라우저 꺼짐 방지 옵션
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# 창 숨기는 옵션 추가
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

URL='https://search.naver.com/search.naver?query=환율'
driver.get(url=URL)

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

time.sleep(0.5)

# dt 태그 찾기
dt_elements = driver.find_elements(By.CSS_SELECTOR,"dt span")

# dd 태그 찾기
dd_elements = driver.find_elements(By.CSS_SELECTOR,"dd span strong")

for dt, dd in zip(dt_elements, dd_elements):
    if dt.text:
        result.append((dt.text, dd.text, float(dd.text.replace(",", ""))))


'''
GUI 코드
'''
from tkinter import *
import tkinter.font
from tkinter import ttk

def convert_currency(currency_list):
    currency_id = radio_var.get()
    input_value = int(input_box.get())

    # print("currency_list : ", currency_list)
    # print("currency_id : ", currency_id)
    # print("input_value : ", input_value)

    # JPY 100
    if currency_list[currency_id][0] == "일본":
        result = f"{currency_list[currency_id][2] * input_value / 100:0,.2f}KRW"
    # 그외 통화
    else:
        result = f"{currency_list[currency_id][2] * input_value:0,.2f}KRW"

    # 변환 결과를 텍스트 레이블에 표시
    result_currency.config(text=result)
    input_box.delete(0, 'end') # 처음부터 끝까지 지우기

# Tkinter 창 생성
window=Tk()

# https://icon-icons.com/ko/
window.iconbitmap('currency.ico')

window.title("환율 변환기")
window.geometry("300x500")
window.resizable(0, 0)

font=tkinter.font.Font(family="맑은 고딕", size=24, slant="italic")

label_title=Label(window, text="환율 변환기", font=font)
label_title.pack()

# 가로선 레이블 생성
sp1=ttk.Separator(window, orient="horizontal")
sp1.pack(fill="both")

# 텍스트 레이블 생성
# label_text = ["미국: 1,333.00 KRW",
#              "일본: 892.92 KRW",
#              "유럽연합: 1,437.84 KRW",
#              "중국: 184.64 KRW",
#              "영국: 1,683.78 KRW",
#              "호주: 869.78 KRW",
#              "캐나다: 989.67 KRW",
#              "뉴질랜드: 811.62 KRW",
#              "태국: 37.11 KRW",
#              "베트남: 5.45 KRW",
#              "홍콩: 170.37 KRW",
#              "대만: 42.44 KRW"]

radio_var=IntVar()

for i, v in enumerate(result):
    # anchor=W : anchor 매개변수는 “n”, “s”, “e”, “w”, “ne”, “nw”, “se”, “sw”, “center” 중 하나의 값을 갖습니다.
    # padx=5 이렇게 하면 좌우 동일하게 적용된다.
    # padx=(1,5) 이렇게 처리하면 왼쪽은 1, 오른쪽은 5가 적용된다.
    text = f'{v[0]} : {v[1]}KRW'
    Radiobutton(window, text=text, value=i, variable=radio_var).pack(anchor="w", padx=20)

# 가로선 레이블 생성
sp2=ttk.Separator(window, orient="horizontal")
sp2.pack(fill="both")

# 입력 레이블
input_label = Label(window, text="금액 : ", justify="left")
input_label.place(x=20, y=400)

# 입력 창
input_box = Entry(window, width=15)
input_box.place(x=80, y=400, height=25)

# 버튼
input_button = Button(window, text="변환", width=7, height=1, command=lambda: convert_currency(result)) # 매개변수를 전달하기 위해 람다 함수 사용
input_button.place(x=200, y=400)

# 변환 결과 레이블 생성
result_label = Label(window, text="변환 결과 : ", justify="left")
result_label.place(x=20, y=450)

# 변환 결과 생성
result_currency = Label(window, text="", justify="left")
result_currency.place(x=100, y=450)

# Tkinter 창 실행
window.mainloop()

# 마지막 미션 : auto-py-to-exe로 exe 파일 생성하기
