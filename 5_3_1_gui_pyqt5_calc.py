# pip install PyQt5
# pip install pyqt5-tools

# UI 편집기 설치
# https://build-system.fman.io/qt-designer-download

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_path = "calc.ui"
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

if __name__ == "__main__":
    print(sys.argv)
    app = QApplication(
        sys.argv
    )  # sys.argv는 python으로 실행한 시스템 argument(Command Line Argument)를 확인

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()  # 프로그램이 꺼지지 않게 무한 루프 처리
