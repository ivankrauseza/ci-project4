from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Appointments(models.Model):
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
    app_date = models.DateField()
    app_time = models.CharField(max_length=4, choices=SLOTS, default="11AM")
    app_type = models.CharField(max_length=100, choices=TYPE, default="11AM")
    confirmed = models.BooleanField(default=False, blank=True)
    doctor = models.IntegerField(default=0)
    completed = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(default=datetime.now)
