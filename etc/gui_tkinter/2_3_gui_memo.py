from tkinter import *
from tkinter.filedialog import asksaveasfile

def new_file():
    text_area.delete(1.0, END)

def save_file():
    f = asksaveasfile(mode = 'w', defaultextension=".txt", filetypes=[('Text files', '.txt')])

    text_save = str(text_area.get(1.0, END))

    f2 = open(f.name, 'w', encoding='utf-8')
    f2.write(text_save)
    f2.close()

def maker():
    help_view = Toplevel(window)
    help_view.geometry("300x100+-1200+300")
    help_view.title("만든이")
    help_view.iconbitmap(r'C:\Users\ITPS\Desktop\python2\tkinter_gui\memo.ico')

    lb = Label(help_view, text = "코리아")
    lb.pack()

window = Tk()
window.title("메모장")
window.resizable(False, False)
window.geometry("400x400+-1200+300")
window.iconbitmap(r'C:\Users\ITPS\Desktop\python2\tkinter_gui\memo.ico')

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="새로 만들기", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="끝내기", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="메모장 정보", command=maker)
menu.add_cascade(label="도움말", menu=menu_2)

text_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

window.config(menu=menu)

window.mainloop()