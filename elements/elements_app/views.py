from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    return render(request, "elements_app/home.html")

def performances(request):
    return render(request, "elements_app/performances.html")

def festival_info(request):
    return render(request, "elements_app/festival_info.html")

def tickets(request):
    return render(request, "elements_app/tickets.html")
