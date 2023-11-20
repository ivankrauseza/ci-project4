from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib import messages
from .forms import DemonstrationForm


def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/dashboard')
        else:
            return redirect('/profile')
    else:
        return render(request, 'index.html')


def custom_login_redirect(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('login')


def demo_success(request):
    return render(request, 'demo_success.html')


def demo(request):

    if request.method == 'POST':
        form = DemonstrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is saved!")
            return redirect('demo')  # Redirect to a success page
    else:
        form = DemonstrationForm()

    return render(request, 'demo.html', {'form': form})
