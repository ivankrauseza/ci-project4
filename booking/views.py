from django.shortcuts import render, redirect


# Default root for logged in user:
def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/dashboard')
        else:
            return redirect('/profile')
    else:
        return render(request, 'index.html')


# Redirect logged in user to appropriate path:
def clr(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('login')
