
from django.urls import path
from . import views


urlpatterns = [       
    path('', views.dashboard, name='dashboard'),
    path('members/', views.members, name='members'),
    path('bookings/', views.bookings, name='bookings'),
    path('staff/', views.staff, name='staff'),
    path('disable_user/<int:user_id>/', views.disable_user, name='disable_user'),
]
