from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import Booking


def profile(request):
    return render(request, 'myprofile.html')


@login_required
def bookings(request):
    booking_data = Booking.objects.filter(member=request.user)
    return render(request, 'mybookings.html', {'booking_data': booking_data})
