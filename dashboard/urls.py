
from django.urls import path
from . import views


urlpatterns = [       
    path('', views.dashboard, name='dashboard'),
    path('members/', views.members, name='members'),
    path('tours/', views.tours, name='tours'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/<int:pk>', views.bookings_update, name='bookings_update'),
    path('bookings/detail/<int:pk>', views.bookings_view, name='bookings_view'),
    path('staff/', views.staff, name='staff'),
    path('disable_user/<int:user_id>/', views.disable_user, name='disable_user'),
    path('toggle_superuser/<int:user_id>/', views.toggle_superuser, name='toggle_superuser'),
]
