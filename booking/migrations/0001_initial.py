# Generated by Django 4.2.6 on 2023-11-22 22:41

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('booked', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Demonstration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demo_guest', models.CharField(default='', max_length=255)),
                ('demo_email', models.EmailField(default='', max_length=255)),
                ('demo_phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('demo_date', models.DateField()),
                ('demo_time', models.CharField(choices=[('11AM', '11AM'), ('2PM', '2PM'), ('7PM', '7PM')], default='11AM', max_length=4)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='CalendarInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Meeting Room', max_length=255)),
                ('request', models.TextField(blank=True, null=True)),
                ('booked', models.BooleanField(default=False)),
                ('start_time', models.CharField(blank=True, choices=[('09:00', '09:00'), ('12:00', '12:00'), ('15:00', '15:00')], default='9am', max_length=10)),
                ('date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.calendar')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Calendar Entries',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('cancel', models.BooleanField(blank=True, default=False)),
                ('cancelwhen', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('meal', models.CharField(choices=[('NONE', 'NONE'), ('BEEF', 'BEEF'), ('CHICKEN', 'CHICKEN'), ('VEGETARIAN', 'VEGETARIAN')], default='NONE', max_length=99)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_type', models.CharField(choices=[('GP Consultation', 'GP Consultation'), ('Mental Health', 'Mental Health')], default='11AM', max_length=100)),
                ('app_date', models.DateField()),
                ('app_time', models.CharField(choices=[('11AM', '11AM'), ('2PM', '2PM'), ('7PM', '7PM')], default='11AM', max_length=4)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('confirmed', models.BooleanField(blank=True, default=False)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('app_member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
