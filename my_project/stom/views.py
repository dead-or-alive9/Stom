from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'stom/AQN.html')


def info(request):
    return render(request, 'stom/info.html')
