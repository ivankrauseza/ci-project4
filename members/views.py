from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from booking.models import Appointments
from django.contrib import messages
from .forms import AppointmentsForm


def profile(request):
    return render(request, 'myprofile.html')


@login_required
def appointments(request):
    appointments = Appointments.objects.filter(
        app_member=request.user,
        completed=False
    ).order_by('app_date')
    completed = Appointments.objects.filter(
        completed=True
    ).order_by('app_date')

    if request.method == 'POST':
        # user_id = request.POST.get('user_id')
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is saved!")
            return redirect('appointments')  # Redirect to a success page
    else:
        form = AppointmentsForm()

    context = {
        'appointments': appointments,
        'completed': completed,
        'form': form
    }

    return render(request, 'appointments.html', context)


@login_required
def appointments_detail(request, post_id):
    record = get_object_or_404(Appointments, id=post_id)
    if request.method == 'POST':
        form = AppointmentsForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is saved!")
            return redirect('appointments')  # Redirect to a success page
    else:
        form = AppointmentsForm()

    context = {
        'record': record,
        'form': form,
    }

    return render(request, 'appointments_detail.html', context)


def appointments_delete(request, post_id):
    post = get_object_or_404(Appointments, pk=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('appointments')

    return render(request, 'appointments_delete.html', {'post': post})


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


# BOOKING A MEETING
def meeting_book(request, pk):
    record = CalendarInstance.objects.get(pk=pk)
    if request.method == 'POST':
        form = MeetingBookForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = MeetingBookForm(instance=record)
    context = {
        'record': record,
        'form': form
    }
    return render(request, 'meeting_book.html', context)