
from django.urls import path
from . import views


urlpatterns = [       
    path('', views.dashboard, name='dashboard'),
    path(
        'appointments/', 
        views.appointments, 
        name='dashboard_appointments'
    ),
    path(
        'appointments/<int:post_id>',
        views.appointment_detail,
        name='dashboard_appointment_detail'
    ),
    path(
        'appointments/cancel/<int:post_id>/',
        views.appointment_cancel,
        name='dashboard_appointment_cancel'
    ),
    path(
        'appointments/accept/<int:post_id>/',
        views.appointment_accept,
        name='dashboard_appointment_accept'
    ),
    path('members/', views.members, name='members'),
    path('doctors/', views.doctors, name='doctors'),
    path('disable_user/<int:user_id>/', views.disable_user, name='disable_user'),
    path('toggle_superuser/<int:user_id>/', views.toggle_superuser, name='toggle_superuser'),
]
