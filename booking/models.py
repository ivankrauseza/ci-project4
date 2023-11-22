from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Calendar(models.Model):

    class Meta:
        ordering = ['date']

    name = models.CharField(default="", max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(default="", max_length=255)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CalendarInstance(models.Model):

    class Meta:
        verbose_name_plural = 'Calendar Entries'

    title = models.CharField(default="Meeting Room", max_length=255)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.ForeignKey(Calendar, null=True, on_delete=models.CASCADE)
    request = models.TextField(blank=True, null=True)
    booked = models.BooleanField(default=False)
    START_TIME = (
        ('09:00', '09:00'),
        ('12:00', '12:00'),
        ('15:00', '15:00'),
    )
    start_time = models.CharField(
        max_length=10,
        choices=START_TIME,
        blank=True,
        default='9am',
    )

    def __str__(self):
        return self.title

    @property
    def calendar_name(self):
        return self.date


class Booking(models.Model):

    MEAL = (
        ("NONE", "NONE"),
        ("BEEF", "BEEF"),
        ("CHICKEN", "CHICKEN"),
        ("VEGETARIAN", "VEGETARIAN"),
    )

    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now, null=True)
    created = models.DateTimeField(default=datetime.now, null=True)
    cancel = models.BooleanField(default=False, blank=True)
    cancelwhen = models.DateTimeField(default=datetime.now, null=True)
    meal = models.CharField(max_length=99, choices=MEAL, default="NONE")


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
