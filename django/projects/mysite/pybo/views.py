from django.shortcuts import render
from django.views import View


class BarChartView(View):
    def get(self, request):
        return render(request, "pybo/bar_chart.html")
