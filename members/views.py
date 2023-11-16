from django.shortcuts import render


def profile(request):
    return render(request, 'myprofile.html')


def bookings(request):
    return render(request, 'mybookings.html')
