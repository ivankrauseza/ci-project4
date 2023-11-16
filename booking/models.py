from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Booking(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now, null=True)
    created = models.DateTimeField(default=datetime.now, null=True)
    cancel = models.BooleanField(default=False, blank=True)
    cancelwhen = models.DateTimeField(default=datetime.now, null=True)
