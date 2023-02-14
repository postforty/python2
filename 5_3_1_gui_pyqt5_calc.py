# pip install PyQt5
# pip install pyqt5-tools
# 설치 에러 발생시
# pip install pyside2
# C:\Users\사용자\AppData\Local\Programs\Python\Python310-32\Lib\site-packages\PySide2
# 설치 에러 발생시 직접 설치
# https://build-system.fman.io/qt-designer-download

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_path = 'calc.ui'
from_class = uic.loadUiType(ui_path)[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# import os
# print(os.path.abspath(__file__))
# app = QApplication([os.path.abspath(__file__)])
# myWindow = WindowClass()
# myWindow.show()
# app.exec_()

if __name__=="__main__":
    app = QApplication(sys.argv) # sys.argv는 python으로 실행한 시스템 argument(Command Line Argument)를 확인
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()