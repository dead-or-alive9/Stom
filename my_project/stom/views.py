from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


def aqn(request):
    return render(request, 'stom/AQN.html')


@login_required
def administration(request):
    return render(request, 'stom/administration.html')


@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('administration')
        else:
            return render(request, 'stom/login.html', {'error': 'Неправильный логин или пароль'})

    return render(request, 'stom/login.html')