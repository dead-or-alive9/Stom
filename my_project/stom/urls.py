from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', aqn, name='home'),
                  path('login/', login_view, name='login'),
                  path('doctors/<slug:slug>/', doctor_detail, name='doctor_detail'),
                  path('administration/', administration, name='administration'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)