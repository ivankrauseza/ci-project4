from django.contrib import admin
from django.urls import path, include
from appointment import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('', views.index, name='index'),
    path('clr/', views.clr, name='clr'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('profile/', include('members.urls')),
]

urlpatterns += staticfiles_urlpatterns()
