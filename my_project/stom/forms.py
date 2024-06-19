from django import forms
from .models import Patients, Doctor, Specialist, Service, Doctor_specialist, Specialist_service


class Doctor_admin(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class Specialist_admin(forms.ModelForm):
    class Meta:
        model = Specialist
        fields = '__all__'


class Service_admin(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class Doctor_specialist_admin(forms.ModelForm):
    class Meta:
        model = Doctor_specialist
        fields = '__all__'


class Specialist_service_admin(forms.ModelForm):
    class Meta:
        model = Specialist_service
        fields = '__all__'


class Patients_admin(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ('name', 'lastname', 'number', 'date', 'doctor')
