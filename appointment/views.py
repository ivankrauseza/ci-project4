from django.shortcuts import render, redirect


def index(request):  # Default root:
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/dashboard')
        else:
            return redirect('/profile')
    else:
        return render(request, 'index.html')


def clr(request):  # LOGIN_REDIRECT_URL = 'clr'
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('login')
