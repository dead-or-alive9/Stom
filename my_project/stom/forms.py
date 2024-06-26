from django import forms
from .models import *


class DoctorAdmin(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = 'all'


class SpecialistAdmin(forms.ModelForm):
    class Meta:
        model = Specialist
        fields = 'all'


class ServiceAdmin(forms.ModelForm):
    class Meta:
        model = Service
        fields = 'all'


class DoctorSpecialistAdmin(forms.ModelForm):
    class Meta:
        model = DoctorSpecialist
        fields = 'all'


class SpecialistServiceAdmin(forms.ModelForm):
    class Meta:
        model = SpecialistService
        fields = 'all'


class PatientsAdmin(forms.ModelForm):
    class Meta:
        model = Patients
        fields = 'all'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ('name', 'lastname', 'number', 'date', 'doctor')
