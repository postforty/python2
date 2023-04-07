import os
print(os.path.abspath(__file__))
app = QApplication([os.path.abspath(__file__)])
myWindow = WindowClass()
myWindow.show()
app.exec_()