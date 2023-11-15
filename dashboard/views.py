from django.shortcuts import render


def dashboard_logout(request):
    return render(request, 'auth_logout.html')
