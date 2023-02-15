# https://oceancoding.blogspot.com/2019/05/blog-post_21.html
# https://foxtrotin.tistory.com/272
from socket import *
import threading
import time

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_path = 'chat_server.ui'
from_class = uic.loadUiType(ui_path)[0]

# 채팅 서버
def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))

port = 8081

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

sender = threading.Thread(target=send, args=(connectionSock,)) #send함수를 인자를 넣어 쓰레드 생성
receiver = threading.Thread(target=receive, args=(connectionSock,)) #receive함수를 인자를 넣어 쓰레드 생성

sender.start()
receiver.start()

# while True: #프로그램을 계속 실행한다
#     time.sleep(1) #1초 쉰다
#     pass

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('채팅 서버')
        self.btn_send.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        btn_value = self.input_msg.text()
        self.msg_box.append(btn_value)
        self.input_msg.clear()
        print(btn_value)

if __name__=="__main__":
    app = QApplication(sys.argv) # sys.argv는 python으로 실행한 시스템 argument(Command Line Argument)를 확인
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

