
from django.urls import path
from . import views


urlpatterns = [       
    path('', views.dashboard, name='dashboard'),
    path('patients/', views.patients, name='patients'),
    path('patients/<int:post_id>', views.patients_detail, name='patients_detail'),
    path('patients/delete/<int:post_id>/', views.patients_delete, name='patients_delete'),
    path('patients/accept/<int:post_id>/', views.patients_accept, name='patients_accept'),
    path('members/', views.members, name='members'),
    path('staff/', views.staff, name='staff'),
    path('disable_user/<int:user_id>/', views.disable_user, name='disable_user'),
    path('toggle_superuser/<int:user_id>/', views.toggle_superuser, name='toggle_superuser'),
]
