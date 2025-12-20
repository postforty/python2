from tkinter import *

def say_hello():
    print("안녕하세요!")

window = Tk()
window.geometry("300x200")

# 위젯 생성 (부모 윈도우, 속성들...)
label = Label(window, text="버튼을 눌러보세요.")
label.pack() # pack()은 위젯을 차례대로 쌓는 배치 방식

button = Button(window, text="클릭", command=say_hello)
button.pack()

window.mainloop()