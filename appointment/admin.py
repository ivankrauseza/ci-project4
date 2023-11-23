from django.contrib import admin
from .models import Appointments


class AppointmentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'app_member',
        'app_date',
        'app_time',
    )

    ordering = ('id', 'app_date', 'app_time',)


admin.site.register(Appointments, AppointmentsAdmin)
