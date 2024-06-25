from django.urls import path
from .views import *

urlpatterns = [
    path('', aqn, name='home'),
    path('login/', login, name='login'),
    path('administration/', administration, name='administration'),
]
