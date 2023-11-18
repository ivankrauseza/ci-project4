# Generated by Django 4.2.6 on 2023-11-18 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_demonstration_demo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demonstration',
            name='demo_time',
            field=models.DecimalField(choices=[('11AM', '11AM'), ('2PM', '2PM'), ('7PM', '7PM')], decimal_places=2, max_digits=10),
        ),
    ]
