# pip install flask
from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
from views.chart import weather_chart
import base64

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "hello flask!"

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/chart')
def chart():
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 1, 7, 8]
    plt.plot(x,y)

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    with open("static/chart.png", "wb") as f:
        f.write(img.read())

    plt.close()

    return render_template("chart.html")

@app.route('/weather')
def weather():
    img_result = weather_chart()
    img_base64 = base64.b64encode(img_result).decode()
    return render_template("weather.html",chart=img_base64)

def main():
    app.run(debug=True, port=3000)

if __name__ == "__main__":
    main()