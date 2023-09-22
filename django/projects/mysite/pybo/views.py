from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, "pybo/base.html")


def chart(request):
    return render(request, "pybo/chart.html")
