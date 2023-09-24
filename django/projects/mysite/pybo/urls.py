from django.urls import path

from . import views

app_name = "pybo"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("chart/", views.chart, name="chart"),
]
