# Generated by Django 4.2.6 on 2023-11-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_demonstration_demo_email_demonstration_demo_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demonstration',
            name='demo_email',
            field=models.EmailField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='demonstration',
            name='demo_guest',
            field=models.CharField(default='', max_length=255),
        ),
    ]