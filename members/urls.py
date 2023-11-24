from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='member'),
    path(
        'appointments/',
        views.appointments,
        name='appointments'
    ),
    path(
        'appointments/<int:post_id>',
        views.appointments_detail,
        name='appointments_detail'
    ),
    path(
        'appointments_update/<int:post_id>/',
        views.appointments_update,
        name='appointments_update'
    ),
    path(
        'appointments_delete/<int:post_id>/',
        views.appointments_delete,
        name='appointments_delete'
    ),
]
