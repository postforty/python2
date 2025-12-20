# py를 exe로 빌드
# https://pypi.org/project/auto-py-to-exe/
# pip install auto-py-to-exe
from tkinter import *
from tkinter.filedialog import *

def new_file():
    text_area.delete(1.0, END)

def save_file():
    # 탐색창에서 입력한 파일 경로 생성
    f = asksaveasfile(mode = 'w', defaultextension=".txt", filetypes=[('Text files', '.txt')])

    print(f) # <_io.TextIOWrapper name='C:/Users/J/Documents/GitHub/python2/memo.txt' mode='w' encoding='cp949'>
    print(f.name) # asksaveasfile로 생성된 파일 경로

    # 텍스트 영역 처음부터 끝까지
    text_save = str(text_area.get(1.0, END))

    # with를 사용하면 close()할 필요가 없다.
    # with open(f.name, 'wt', encoding='utf8') as f2:
    #     ft.write(text_save)

    # 인코딩하여 한글 깨짐 문제를 해결
    f2 = open(f.name, 'wt', encoding='utf8')
    f2.write(text_save)
    f2.close()

def maker():
    help_view = Toplevel(window) # 외부 윈도우 창 생성
    help_view.geometry("300x50+800+300")
    help_view.title("만든이")
    lb = Label(help_view, text = "김일남의 메모장 만들기")
    lb.pack()

window = Tk()

# https://icon-icons.com/ko/
window.iconbitmap('memo.ico')

window.title("메모장")
window.geometry("400x400+800+300")
# window.resizable(False, False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0) # tearoff 하위메뉴의 분리 기능 사용 유/무
menu_1.add_command(label="새로 만들기", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy) # window.destroy 종료
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="도움말", command=maker)
menu.add_cascade(label="정보", menu=menu_2)

# 그리드 가중치 설정 (Text 위젯이 위치할 0번 행/열 확장)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# 세로 스크롤바 생성
v_scroll = Scrollbar(window, orient="vertical")
v_scroll.grid(row=0, column=1, sticky="ns") # 텍스트 우측에 세로로 길게 배치

# 가로 스크롤바 생성
h_scroll = Scrollbar(window, orient="horizontal")
h_scroll.grid(row=1, column=0, sticky="ew") # 텍스트 하단에 가로로 길게 배치

# 텍스트 영역
text_area = Text(window,
                wrap="none", # 자동 줄바꿈 끔
                # 스크롤바와 연결
                yscrollcommand=v_scroll.set, 
                xscrollcommand=h_scroll.set)

text_area.grid(row=0, column=0, sticky="nsew") # 텍스트 창을 동서남북 방향으로 붙임

# 스크롤바가 Text 위젯을 제어하도록 명령 설정
v_scroll.config(command=text_area.yview)
h_scroll.config(command=text_area.xview)

window.config(menu=menu) # 이 코드가 있어야 창이 표시됨

window.mainloop()
