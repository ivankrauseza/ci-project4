from django.contrib import admin
from django.urls import path, include
from booking import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('workspace/', views.workspace, name='workspace'),
    path('meeting/', views.meeting, name='meeting'),
    path('cafe/', views.cafe, name='cafe'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('custom-login-redirect/', views.clr, name='clr'),
    path('dashboard/', include('dashboard.urls')),
    path('profile/', include('members.urls')),
]

urlpatterns += staticfiles_urlpatterns()
