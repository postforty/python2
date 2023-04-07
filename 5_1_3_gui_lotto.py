import tkinter # "Tk 인터페이스"
import tkinter.font
import random

lotto_num = range(1, 46)

def buttonClick():
    # 버튼 클릭시 로또 번호와 생성되는 리스트박스
    for i in range(5):
        lottoPick = map(str, random.sample(lotto_num, 6))
        lottoPick = ','.join(lottoPick)
        lottoPick = f'{i+1}회: {lottoPick}'
        print(lottoPick)
        listbox.insert(i, lottoPick)
    listbox.pack()

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

# 리스트박스 틀
font = tkinter.font.Font(size = 20)
listbox = tkinter.Listbox(window, selectmode='extended', height=5, font=font)
listbox.insert(0, "1회:")
listbox.insert(1, "2회:")
listbox.insert(2, "3회:")
listbox.insert(3, "4회:")
listbox.insert(4, "5회:")
listbox.delete(1, 2)
listbox.pack()

window.mainloop()