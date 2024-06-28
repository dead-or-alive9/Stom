from django.db import models


class Specialist(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    fullname = models.CharField(max_length=100)
    history = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=15)
    img = models.ImageField()
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    def __str__(self):
        return self.fullname


class DoctorSpecialist(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f"{self.doctor.fullname} - {self.specialist.name}"


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    img = models.ImageField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


class SpecialistService(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f"{self.specialist.name} - {self.service.name}"


class Patients(models.Model):
    STATUS_CHOICES = (
        ('draft', ' '),
        ('published', 'Осмотр  окончен '),
    )
    PAYMENT_CHOICES = (
        ('draft', 'Не оплачено'),
        ('published', 'Оплачено'),
    )
    name = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    number = models.CharField(max_length=15, blank=False)
    data = models.DateField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='Patients')
    start_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    time_over = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='draft')
    status_payment = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='draft')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


class Hospital(models.Model):
    tite = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=60)
    description = models.TextField()
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
