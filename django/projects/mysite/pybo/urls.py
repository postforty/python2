from django.urls import path

from . import views

urlpatterns = [
    path("", views.BarChartView.as_view(), name="bar_chart"),
]
