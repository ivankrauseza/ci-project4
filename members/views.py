from django.shortcuts import render


def profile(request):
    return render(request, 'profile.html')


def bookings(request):
    return render(request, 'bookings.html')
