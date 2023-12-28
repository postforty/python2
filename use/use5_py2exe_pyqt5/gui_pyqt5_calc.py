# pip install PyQt5

# UI 편집기 설치
# https://build-system.fman.io/qt-designer-download
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon

ui_path = 'calc.ui'
from_class = uic.loadUiType(ui_path)[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("계산기")

        icon = QIcon("calc.ico")      # QIcon 객체 생성
        self.setWindowIcon(icon)     # 아이콘 설정

        # https://icon-icons.com/ko/

        self.btn_C.clicked.connect(self.btn_clicked)
        self.btn_0.clicked.connect(self.btn_clicked)
        self.btn_1.clicked.connect(self.btn_clicked)
        self.btn_2.clicked.connect(self.btn_clicked)
        self.btn_3.clicked.connect(self.btn_clicked)
        self.btn_4.clicked.connect(self.btn_clicked)
        self.btn_5.clicked.connect(self.btn_clicked)
        self.btn_6.clicked.connect(self.btn_clicked)
        self.btn_7.clicked.connect(self.btn_clicked)
        self.btn_8.clicked.connect(self.btn_clicked)
        self.btn_9.clicked.connect(self.btn_clicked)
        self.btn_result.clicked.connect(self.btn_clicked)
        self.btn_min.clicked.connect(self.btn_clicked)
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_mul.clicked.connect(self.btn_clicked)
        self.btn_div.clicked.connect(self.btn_clicked)

        self.le_view.setEnabled(False)

        self.text_value = ""

    def btn_clicked(self):
        btn_value = self.sender().text()
        # print(btn_value)
        if btn_value == 'C':
            # print("clear")
            self.le_view.setText("0")
            self.text_value = ""
        elif btn_value == "=":
            # print("=")
            try:
                resultValue = eval(self.text_value.lstrip("0")) # 왼쪽이 0이 있는 숫자 001 같은 경우 발생하는 에러 대응 코드
                # resultValue = eval(self.text_value) # eval은 문자열 수식을 계산한 값 출력, python interpreter에서 사용법 보여 줄것!
                self.le_view.setText(str(resultValue))
            except:
                self.le_view.setText("error")
        else:
            if btn_value == '×':
                btn_value = "*"
            self.text_value = self.text_value + btn_value
            # print(self.text_value)
            self.le_view.setText(self.text_value)

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
