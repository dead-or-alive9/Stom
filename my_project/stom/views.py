from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import *
from .forms import PatientForm


# Главная страница
def aqn(request):
    hospital = Hospital.objects.first()
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or home page
    else:
        form = PatientForm()

    context = {
        'hospital': hospital,
        'doctors': doctors,
        'form': form
    }
    return render(request, 'stom/AQN.html', context)


def doctor_detail(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    specialists = DoctorSpecialist.objects.filter(doctor=doctor)
    return render(request, 'stom/doctor.html', {'doctor': doctor, 'specialists': specialists})


@login_required
def administration(request):
    return render(request, 'stom/administration.html')


@csrf_protect
def login_view(request):
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
