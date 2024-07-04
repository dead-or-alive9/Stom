from django.contrib import admin
from .models import *

admin.site.register(Specialist)
admin.site.register(Doctor)
admin.site.register(DoctorSpecialist)
admin.site.register(Service)
admin.site.register(SpecialistService)
admin.site.register(Patients)
admin.site.register(Hospital)

