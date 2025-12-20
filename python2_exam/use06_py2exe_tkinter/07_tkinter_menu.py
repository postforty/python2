from tkinter import *

window = Tk()
menu_bar = Menu(window) # 전체 메뉴바

# 하위 메뉴 '파일' 생성
file_menu = Menu(menu_bar, tearoff=0) # 1은 기본값. 메뉴를 독립된 작은 창으로 분리 가능, 0은 분리 기능 비활성
file_menu.add_command(label="종료", command=window.destroy)

# 메뉴바에 '파일' 메뉴 등록
menu_bar.add_cascade(label="파일", menu=file_menu)

window.config(menu=menu_bar) # 윈도우에 메뉴 설정
window.mainloop()