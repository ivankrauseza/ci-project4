
from django.urls import path
from . import views


urlpatterns = [        
    path('logout/', views.dashboard_logout, name='dashboard_logout'),
]
