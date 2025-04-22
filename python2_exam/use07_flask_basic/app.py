# pip install flask
# flask run : 파일명이 app.py인 경우 실행 명령어
# python 파일명.py : 그 밖의 경우
# https://wikidocs.net/81238 : 디버깅 모드 활성화 방법등
from flask import Flask, render_template

print(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello flask!"

@app.route('/1')
def page1():
    return "1 페이지"

@app.route('/2')
def page2():
    return "2 페이지"

@app.route('/3')
def page3():
    return render_template("sample.html")


# flask run 명령시 아래 코드없이 실행됨
# flask run debug 모드 사용하려면 실행 명령어(flask run) 전에 set FLASK_DEBUG=true 명령을 입력한다.
# flask run --port=3000
def main():
    app.run(debug=True, port=3000) # debug 모드는 코드 변경시 서버를 자동 재시작 해준다!

if __name__ == "__main__":
    main()