# Generated by Django 4.2.6 on 2023-11-23 20:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_type', models.CharField(choices=[('GP Consultation', 'GP Consultation'), ('Mental Health', 'Mental Health')], default='11AM', max_length=100)),
                ('app_date', models.DateField()),
                ('app_time', models.CharField(choices=[('11AM', '11AM'), ('2PM', '2PM'), ('7PM', '7PM')], default='11AM', max_length=4)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('confirmed', models.BooleanField(blank=True, default=False)),
                ('doctor', models.IntegerField(default=0)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('app_member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
