from django.contrib import admin
from .models import Booking, Calendar, CalendarInstance, Demonstration


class CalendarAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'name',
        'booked'
    )

    ordering = ('date',)


class CalendarInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'start_time',
        'calendar_name',
    )

    ordering = ('date', 'start_time',)


admin.site.register(Calendar, CalendarAdmin)
admin.site.register(CalendarInstance, CalendarInstanceAdmin)
admin.site.register(Booking)
admin.site.register(Demonstration)
