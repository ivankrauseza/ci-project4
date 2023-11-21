from django.contrib import admin
from .models import Booking, MeetingRoom, Demonstration


admin.site.register(Booking)
admin.site.register(MeetingRoom)
admin.site.register(Demonstration)
