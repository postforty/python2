# pip install PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_path = r"C:\Users\ITPS\Desktop\python2\gui_pyqt5\calc.ui"
from_class = uic.loadUiType(ui_path)[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
