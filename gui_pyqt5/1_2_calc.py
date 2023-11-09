# pip install PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon

ui_path = r"C:\Users\ITPS\Desktop\python2\gui_pyqt5\calc.ui"
from_class = uic.loadUiType(ui_path)[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(r'C:\Users\ITPS\Desktop\python2\gui_pyqt5\calc.ico'))

        self.btn_c.clicked.connect(self.btn_clicked)
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
        self.btn_rst.clicked.connect(self.btn_clicked)
        self.btn_min.clicked.connect(self.btn_clicked)
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_mul.clicked.connect(self.btn_clicked)
        self.btn_div.clicked.connect(self.btn_clicked)
    
        self.le_view.setEnabled(False)

        self.text_value = ''
    
    def btn_clicked(self):
        btn_value = self.sender().text()

        if btn_value == 'C':
            self.le_view.setText('0')
            self.text_value = ''
        elif btn_value == '=':
            try:
                result = eval(self.text_value.lstrip('0'))
                self.le_view.setText(str(result))
            except:
                self.le_view.setText("error")
        else:
            if btn_value == '×':
                btn_value = '*'
            self.text_value = self.text_value + btn_value
            self.le_view.setText(self.text_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
