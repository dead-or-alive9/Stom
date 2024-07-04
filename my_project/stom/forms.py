from django import forms
from .models import *


class DoctorAdmin(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class SpecialistAdmin(forms.ModelForm):
    class Meta:
        model = Specialist
        fields = '__all__'


class ServiceAdmin(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class DoctorSpecialistAdmin(forms.ModelForm):
    class Meta:
        model = DoctorSpecialist
        fields = '__all__'


class SpecialistServiceAdmin(forms.ModelForm):
    class Meta:
        model = SpecialistService
        fields = '__all__'


class PatientsAdmin(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ('name', 'number', 'data', 'doctor')
