from tkinter import *

def clear_text():
    text_area.delete(1.0, END)

window = Tk()
window.geometry("300x300")

# 1. 가중치 설정 (창이 커질 때 0번 행과 열을 확장함)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# 2. Text 위젯 배치 (grid 사용)
text_area = Text(window)
# row=0, column=0 자리에 배치하고 nsew(사방)로 늘림
text_area.grid(row=0, column=0, sticky="nsew")

# 3. Button 위젯 배치 (grid 사용)
# 버튼은 텍스트 창 아래(row=1)에 배치
btn = Button(window, text="모두 지우기", command=clear_text)
btn.grid(row=1, column=0, sticky="we") # 좌우로만 늘어나게 설정

window.mainloop()