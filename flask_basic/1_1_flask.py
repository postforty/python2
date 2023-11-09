# pip install flask
from flask import Flask, render_template

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

def main():
    app.run(debug=True, port=3000)

if __name__ == "__main__":
    main()