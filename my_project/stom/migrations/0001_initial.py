# Generated by Django 5.0.6 on 2024-06-27 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('history', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=15)),
                ('img', models.ImageField(upload_to='')),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tite', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('img', models.ImageField(upload_to='')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('number', models.CharField(max_length=15)),
                ('data', models.DateField(auto_now_add=True)),
                ('start_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_over', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', ' '), ('published', 'Осмотр  окончен ')], default='draft', max_length=20)),
                ('status_payment', models.CharField(choices=[('draft', 'Не оплачено'), ('published', 'Оплачено')], default='draft', max_length=50)),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Patients', to='stom.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSpecialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stom.doctor')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stom.specialist')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialistService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stom.service')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stom.specialist')),
            ],
        ),
    ]
