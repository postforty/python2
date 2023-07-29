from tkinter import *
from tkinter.filedialog import *


def new_file():
    pass


def save_file():
    pass


def maker():
    pass


window = Tk()
window.title("메모장")
window.geometry("400x400+800+300")
window.resizable(False, False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)  # tearoff 하위메뉴의 분리 기능 사용 유/무
menu_1.add_command(label="새로 만들기", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy)  # window.destroy 종료
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이", command=maker)
menu.add_cascade(label="만든이", menu=menu_2)

# 텍스트 영역
text_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)  # 텍스트 창을 동서남북 방향으로 붙임

window.config(menu=menu)

window.mainloop()
