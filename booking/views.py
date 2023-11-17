from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html')


def custom_login_redirect(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/dashboard')
        else:
            return redirect('/profile')
    else:
        return redirect('login')
