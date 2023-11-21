from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from booking import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('demo/success/', views.demo_success, name='demo_success'),
    path('workspace/', views.workspace, name='workspace'),
    path('meeting/', views.meeting, name='meeting'),
    path('cafe/', views.cafe, name='cafe'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('custom-login-redirect/', views.custom_login_redirect, name='custom_login_redirect'),
    path('dashboard/', include('dashboard.urls')),
    path('profile/', include('members.urls')),
]

urlpatterns += staticfiles_urlpatterns()
