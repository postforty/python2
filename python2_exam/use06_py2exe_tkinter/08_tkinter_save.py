from tkinter import *
from tkinter.filedialog import asksaveasfile

def save():
    # 저장 창을 띄우고 파일 객체를 반환받음
    f = asksaveasfile(defaultextension=".txt")
    if f:
        f.write("메모장 연습")
        f.close()

window = Tk()
Button(window, text="저장하기", command=save).pack()
window.mainloop()