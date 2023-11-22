# Generated by Django 4.2.6 on 2023-11-22 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0031_remove_calendarinstance_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarinstance',
            name='start_time',
            field=models.CharField(blank=True, choices=[('9am', '9am'), ('12pm', '12pm'), ('3pm', '3pm')], default='9am', max_length=10),
        ),
    ]
