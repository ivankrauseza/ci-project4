from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from booking import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('profile/', include('members.urls')),
]
