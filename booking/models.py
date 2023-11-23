from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Appointments(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    TYPE = (
        ("GP Consultation", "GP Consultation"),
        ("Mental Health", "Mental Health"),
    )
    SLOTS = (
        ("11AM", "11AM"),
        ("2PM", "2PM"),
        ("7PM", "7PM"),
    )
    app_member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    app_type = models.CharField(max_length=100, choices=TYPE, default="11AM")
    app_date = models.DateField()
    app_time = models.CharField(max_length=4, choices=SLOTS, default="11AM")
    created = models.DateTimeField(default=datetime.now)
    confirmed = models.BooleanField(default=False, blank=True)
    doctor = models.IntegerField(default=0)
    completed = models.BooleanField(default=False, blank=True)
