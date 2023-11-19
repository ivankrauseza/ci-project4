# Generated by Django 4.2.6 on 2023-11-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_demonstration_demo_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demonstration',
            name='demo_time',
            field=models.DecimalField(choices=[('11:00', '11AM'), ('14:00', '2PM'), ('19:00', '7PM')], decimal_places=2, max_digits=10),
        ),
    ]