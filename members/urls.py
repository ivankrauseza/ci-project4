from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='myprofile'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/<int:post_id>', views.appointments_detail, name='appointments_detail'),
    path('appointments_delete/<int:post_id>/', views.appointments_delete, name='appointments_delete'),
    path('bookings', views.bookings, name='mybookings'),
]
