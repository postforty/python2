from tkinter import *
import tkinter.font
from tkinter import ttk

def convert_currency():
    print(radio_var.get())
    # 입력 창에서 텍스트 가져오기
    input_value = input_box.get()
    # 입력된 값을 이용하여 환율 변환 수행
    # 변환 결과를 출력하거나 원하는 작업 수행
    result = input_value  # 예시 결과, 실제 변환 로직을 적용해야 함

    # 변환 결과를 텍스트 레이블에 표시
    result_currency.config(text=result)

# Tkinter 창 생성
window=Tk()
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
label_text = ["미국: 1,333.00 KRW",
             "일본: 892.92 KRW",
             "유럽연합: 1,437.84 KRW",
             "중국: 184.64 KRW",
             "영국: 1,683.78 KRW",
             "호주: 869.78 KRW",
             "캐나다: 989.67 KRW",
             "뉴질랜드: 811.62 KRW",
             "태국: 37.11 KRW",
             "베트남: 5.45 KRW",
             "홍콩: 170.37 KRW",
             "대만: 42.44 KRW"]

radio_var=IntVar()

for i, v in enumerate(label_text):
    # anchor=W : anchor 매개변수는 “n”, “s”, “e”, “w”, “ne”, “nw”, “se”, “sw”, “center” 중 하나의 값을 갖습니다.
    # padx=5 이렇게 하면 좌우 동일하게 적용된다.
    # padx=(1,5) 이렇게 처리하면 왼쪽은 1, 오른쪽은 5가 적용된다.
    Radiobutton(window, text=v, value=i, variable=radio_var).pack(anchor="w", padx=20)

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
input_button = Button(window, text="변환", width=7, height=1, command=convert_currency)
input_button.place(x=200, y=400)

# 변환 결과 레이블 생성
result_label = Label(window, text="변환 결과 : ", justify="left")
result_label.place(x=20, y=450)

# 변환 결과 생성
result_currency = Label(window, text="")
result_currency.place(x=200, y=450)

# Tkinter 창 실행
window.mainloop()
