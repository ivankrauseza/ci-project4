from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import Booking
from django.contrib import messages
from .forms import BookingForm


def profile(request):
    return render(request, 'myprofile.html')


@login_required
def bookings(request):
    booking_data = Booking.objects.filter(member=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is saved!")
            return redirect('bookings')  # Redirect to a success page
    else:
        form = BookingForm()

    context = {
        'form': form,
        'booking_data': booking_data
    }

    return render(request, 'mybookings.html', context)
