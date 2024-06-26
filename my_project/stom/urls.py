from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('info/', info, name='info'),
]
