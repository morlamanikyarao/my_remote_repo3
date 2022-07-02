from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def display(request):
    s="<h1>Hello Students Welcome to DurgaSoft Django classes!!! by durga sir</h1>"
    return HttpResponse(s)
