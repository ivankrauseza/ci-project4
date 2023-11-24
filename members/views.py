from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from appointment.models import Appointments
from django.contrib import messages
from .forms import AppointmentForm


def profile(request):
    return render(request, 'member.html')


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
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment saved!")
            return redirect('appointments')  # Redirect to a success page
    else:
        form = AppointmentForm()

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
        form = AppointmentForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            # Send message toast:
            messages.success(request, "Data is saved!")
            # Redirect to appointments:
            return redirect('appointments')
    else:
        form = AppointmentForm()

    context = {
        'record': record,
        'form': form,
    }

    return render(request, 'appointments_detail.html', context)


@login_required
def appointments_update(request, post_id):
    record = get_object_or_404(Appointments, pk=post_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            # Send message toast:
            messages.success(request, "Update saved!")
            # Redirect to appointments:
            return redirect('appointments')
        else:
            # Send message toast:
            print("Form errors:", form.errors)
            messages.error(request, "Something went wrong")
            form = AppointmentForm(instance=record)
    else:
        form = AppointmentForm(instance=record)

    context = {
        'record': record,
        'form': form,
    }

    return render(request, 'appointments_update.html', context)


def appointments_delete(request, post_id):
    post = get_object_or_404(Appointments, pk=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('appointments')

    return render(request, 'appointments_delete.html', {'post': post})