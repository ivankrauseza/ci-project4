from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Booking(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    booked = models.BooleanField(default=False, blank=True)
    date = models.DateField()
    created = models.DateTimeField(default=datetime.now, null=True)
    cancelwhen = models.DateTimeField(default=datetime.now, null=True)
    request = models.TextField(default="", null=True)


class Demonstration(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    SLOTS = (
        ("11AM", "11AM"),
        ("2PM", "2PM"),
        ("7PM", "7PM"),
    )

    demo_guest = models.CharField(max_length=255, default="")
    demo_email = models.EmailField(max_length=255, default="")
    demo_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    demo_date = models.DateField()
    demo_time = models.CharField(max_length=4, choices=SLOTS, default="11AM")
    created = models.DateTimeField(default=datetime.now)
