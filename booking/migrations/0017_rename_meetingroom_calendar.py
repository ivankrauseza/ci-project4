# Generated by Django 4.2.6 on 2023-11-21 10:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0016_meetingroom'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MeetingRoom',
            new_name='Calendar',
        ),
    ]
