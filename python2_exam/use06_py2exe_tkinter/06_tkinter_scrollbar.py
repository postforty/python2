from tkinter import *

window = Tk()
window.title("스크롤바 실습")
window.geometry("400x300")

# 1. 그리드 가중치 설정 (Text 위젯이 위치할 0번 행/열 확장)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# 2. 세로 스크롤바 생성
v_scroll = Scrollbar(window, orient="vertical")
v_scroll.grid(row=0, column=1, sticky="ns") # 텍스트 우측에 세로로 길게 배치

# 3. 가로 스크롤바 생성
h_scroll = Scrollbar(window, orient="horizontal")
h_scroll.grid(row=1, column=0, sticky="ew") # 텍스트 하단에 가로로 길게 배치

# 4. Text 위젯 생성 (스크롤바와 연결)
# wrap="none" 설정을 해야 가로 스크롤바가 활성화됩니다 (자동 줄바꿈 끔)
text_area = Text(window, wrap="none", 
                 yscrollcommand=v_scroll.set, 
                 xscrollcommand=h_scroll.set)
text_area.grid(row=0, column=0, sticky="nsew")

# 5. 스크롤바가 Text 위젯을 제어하도록 명령 설정
v_scroll.config(command=text_area.yview)
h_scroll.config(command=text_area.xview)

window.mainloop()