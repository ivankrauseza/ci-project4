# Generated by Django 4.2.6 on 2023-11-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_rename_meetingroom_calendar'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(default='Meeting Room', max_length=255)),
                ('request', models.TextField(blank=True, null=True)),
                ('start_time', models.CharField(blank=True, choices=[('9am', '9am'), ('10am', '10am'), ('11am', '11am'), ('12am', '12am'), ('1pm', '1pm'), ('2pm', '2pm'), ('3pm', '3pm'), ('4pm', '4pm'), ('5pm', '5pm')], default='9am', max_length=10)),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='calendar',
            options={'ordering': ['date']},
        ),
    ]