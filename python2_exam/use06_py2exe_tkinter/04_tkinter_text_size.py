from tkinter import *

def clear_text():
    # 1.0(첫 줄 첫 글자)부터 END(끝)까지 삭제
    text_area.delete(1.0, END)

window = Tk()
# 가로 40글자, 세로 10줄 크기의 텍스트 영역 생성
text_area = Text(window, width=40, height=10)
text_area.pack()

btn = Button(window, text="모두 지우기", command=clear_text)
btn.pack()

window.mainloop()