# pip install Flask
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_file
from io import BytesIO
import matplotlib
from views.chart import weather_chart

matplotlib.use("agg")

app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "hello"


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/chart")
def home():
    # return render_template("index.html")
    # Matplotlib 차트 생성
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 7, 8]
    plt.plot(x, y)

    # 차트를 이미지로 저장
    img = BytesIO()
    # plt.savefig(img, format="png")
    plt.savefig("static/chart.png", format="png")
    img.seek(0)

    # Matplotlib 차트를 표시하고 메모리 누수 방지
    plt.show()
    plt.close()

    # 이미지를 HTML 템플릿에 전달
    return render_template("chart.html", chart=img.getvalue())


@app.route("/weather")
def weather():
    img_result = weather_chart()

    # 이미지를 HTML 템플릿에 전달
    return render_template("weather.html", chart=img_result)


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=3000)
