# Generated by Django 4.2.6 on 2023-11-22 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_appointments_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='doctor',
        ),
    ]