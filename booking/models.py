from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Booking(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(default=datetime.now, blank=True)
