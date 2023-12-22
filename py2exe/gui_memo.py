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
    help_view = Toplevel(window)
    help_view.geometry("300x50+800+300")
    help_view.title("만든이")
    lb = Label(help_view, text = "메모장 만들기")
    lb.pack()

window = Tk()

# https://icon-icons.com/ko/%EC%95%84%EC%9D%B4%EC%BD%98/%EB%A9%94%EB%AA%A8-%ED%8E%B8%EC%A7%91-%EC%97%B0%ED%95%84-%EC%93%B0%EA%B8%B0/109205
window.iconbitmap('memo.ico')

window.title("메모장")
window.geometry("400x400+800+300")
window.resizable(False, False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0) # tearoff 하위메뉴의 분리 기능 사용 유/무
menu_1.add_command(label="새로 만들기", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy) # window.destroy 종료
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이", command=maker)
menu.add_cascade(label="만든이", menu=menu_2)

# 텍스트 영역
text_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky = N + E + S + W) # 텍스트 창을 동서남북 방향으로 붙임

window.config(menu=menu)

window.mainloop()
