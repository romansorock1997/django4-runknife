from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from pip import main


# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def cruze(request):
    return render(request, 'main/my.html')