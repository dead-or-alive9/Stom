from django import forms
from .models import Patients, Doctor, Specialist, Service, Doctor_specialist, Specialist_service


class Doctor_admin(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = 'all'


class Specialist_admin(forms.ModelForm):
    class Meta:
        model = Specialist
        fields = 'all'


class Service_admin(forms.ModelForm):
    class Meta:
        model = Service
        fields = 'all'


class Doctor_specialist_admin(forms.ModelForm):
    class Meta:
        model = Doctor_specialist
        fields = 'all'


class Specialist_service_admin(forms.ModelForm):
    class Meta:
        model = Specialist_service
        fields = 'all'


class Patients_admin(forms.ModelForm):
    class Meta:
        model = Patients
        fields = 'all'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ('name', 'lastname', 'number', 'date', 'doctor')
