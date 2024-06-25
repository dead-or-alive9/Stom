from django.http import HttpResponse
from django.shortcuts import render


def aqn(request):
    return render(request, 'stom/AQN.html')


def login(request):
    return render(request, 'stom/login.html')


def administration(request):
    return render(request, 'stom/administration.html')
