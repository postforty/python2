import tkinter
import tkinter.font
import random

lotto_num = range(1, 46)

def buttonClick():
    print(random.sample(lotto_num, 6))

window = tkinter.Tk()
window.title("lotto")
window.resizable(False, False)
window.geometry("400x200+800+300") # 가로세로의 크기, +800+300은 초기 위치

# 창 중앙 위치
# w = 400
# h = 150
# sw = window.winfo_screenwidth()
# sh = window.winfo_screenheight()
# x = (sw - w)/2
# y = (sh - h)/2
# window.geometry('%dx%d+%d+%d' % (w, h, x, y))

button = tkinter.Button(window, overrelief="solid", text='번호확인', width=15, command=buttonClick, repeatdelay=1000, repeatinterval=500) # 마우스를 누르고 있을때 delay, delay 후 interval
button.pack()

window.mainloop()