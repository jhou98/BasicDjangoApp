from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    from graphs.query import baseData
    return render(request, "graphs.html", {"test_fn": baseData('newtable1')})
