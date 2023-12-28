# pip install Flask
import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO
import matplotlib
from views.chart import weather_chart
import base64

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

    """ 차트를 이미지로 저장 """
    # case1
    img = BytesIO()
    plt.savefig(img, format="png")
    # `plt.savefig()` 함수를 사용하여 이미지를 `BytesIO` 객체에 저장하면, 파일 포인터는 파일의 끝을 가리키게 됩니다.
    # 이 상태에서 `img.read()` 를 호출하면 아무 데이터도 읽지 못합니다.
    # `img.seek(0)`을 호출하면 파일 포인터가 다시 파일의 시작 지점으로 이동하게 되므로,
    # 이후 `img.read()`를 호출하면 파일의 내용을 처음부터 다시 읽을 수 있게 됩니다.
    img.seek(0)

    # 이미지를 파일로 저장
    with open("static/chart.png", "wb") as f:
        f.write(img.read())

    # case2
    # plt.savefig()를 사용하여 이미지를 파일로 저장하는 방법이 훨씬 간단하며,
    # BytesIO 객체를 사용하는 경우에는 이미지 데이터를 메모리에 임시로 저장하거나 다른 용도로 활용할 때 유용합니다.***
    # plt.savefig("static/chart.png", format="png")

    plt.close()

    # 이미지를 HTML 템플릿에 전달
    return render_template("chart.html")


@app.route("/weather")
def weather():
    img_result = weather_chart()

    # 이진 데이터를 Base64로 인코딩합니다.
    img_base64 = base64.b64encode(img_result).decode()

    # 이미지를 HTML 템플릿에 전달
    return render_template("weather.html", chart=img_base64)


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=3000)
