# Generated by Django 4.1.7 on 2023-03-02 14:00

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Area')),
            ],
        ),
        migrations.CreateModel(
            name='Chronic_condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=70)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('value', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='History_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='Specialist')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNum', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(code='invalid_password', message='Phone number must start 05 and it 10 digit like 05xxxxxxxx', regex='^05[0-9]{8}$')], verbose_name='Phone number')),
                ('is_doctor', models.BooleanField(default=False)),
                ('image_profile', models.ImageField(blank=True, default='Images_profile/default_profile.jpg', null=True, upload_to='Images_profile', validators=[main.models.validate_image])),
                ('ex_address', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.area')),
                ('chronic_conditions', models.ManyToManyField(blank=True, to='main.chronic_condition')),
                ('off_day', models.ManyToManyField(blank=True, related_name='off_days', to='main.day')),
                ('specialty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.specialty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=50)),
                ('discrption', models.TextField()),
                ('file', models.FileField(upload_to=main.models.random_name('Files'))),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='main.userinfo')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='main.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=100)),
                ('start_price', models.IntegerField()),
                ('end_price', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adate', models.DateField()),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('status', models.IntegerField(blank=True, choices=[(1, 'accepted'), (2, 'pended'), (3, 'rejected'), (4, 'Attended'), (5, 'Not attended')], default=2)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointment_set', to='main.userinfo')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointment_set', to='main.userinfo')),
            ],
        ),
    ]
