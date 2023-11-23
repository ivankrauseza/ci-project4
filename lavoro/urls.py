from django.contrib import admin
from django.urls import path, include
from booking import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('custom-login-redirect/', views.clr, name='clr'),
    path('dashboard/', include('dashboard.urls')),
    path('profile/', include('members.urls')),
]

urlpatterns += staticfiles_urlpatterns()
