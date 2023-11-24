# from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Users
from django.contrib.auth.models import User
# Booking Modals
from appointment.models import Appointments
# Disable User
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .forms import AppointmentsForm


# User = get_user_model()


@login_required
def dashboard(request):
    # get all appointments
    appointments = Appointments.objects.all().order_by('app_date')
    # filter by unique staff incomplete appointments
    myappointments = appointments.filter(doctor=request.user.id)
    context = {
        'myappointments': myappointments
    }
    return render(request, 'dashboard.html', context)


@login_required
def appointments(request):
    # get all appointments
    appointments = Appointments.objects.all().order_by('app_date')
    # filter by unconfirmed appointments
    requests = appointments.filter(confirmed=False)

    context = {
        'requests': requests,
    }
    return render(request, 'db_appointments.html', context)
# GP sets the owner field to themselves


@login_required
def appointment_detail(request, post_id):
    # get appointments by id
    record = get_object_or_404(Appointments, id=post_id)
    if request.method == 'POST':
        form = AppointmentsForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is saved!")
            return redirect('dashboard_appointments')  # Redirect to a success page
    else:
        form = AppointmentsForm()

    context = {
        'record': record,
        'form': form,
    }

    return render(request, 'db_appointment_detail.html', context)


def appointment_accept(request, post_id):
    post = get_object_or_404(Appointments, pk=post_id)

    if request.method == 'POST':

        # Access the field value you're interested in
        field_value = post.doctor

        # Check if the field value is 0
        if field_value == 0:
            # Do something if the field value is 0
            print('Field value is 0')
            post.doctor = request.user.id
            post.confirmed = True
            post.save()
            return redirect('dashboard')
        else:
            # Do something else if the field value is not 0
            messages.info(request, 'Sorry, it looks like another Doctor has accepted this appointment before you.')
        
    return render(request, 'db_appointment_error.html', {'post': post})


def appointment_cancel(request, post_id):
    post = get_object_or_404(Appointments, pk=post_id)

    if request.method == 'POST':
        post.doctor = 0
        post.confirmed = False
        post.save()
        return redirect('dashboard_appointments')

    return render(request, 'db_appointment_cancel.html', {'post': post})


def members(request):
    users_members = User.objects.filter(is_staff=False)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create an inactive user
            user = form.save(request)
            user.is_staff = False
            user.is_superuser = False
            user.save()

            # Activate the user
            email_address = EmailAddress.objects.get(email=user.email)
            email_address.verified = True
            email_address.save()

            return redirect('members')  # Redirect to a success page
    else:
        form = SignupForm()

    context = {
        'form': form,
        'users_members': users_members,
    }

    return render(request, 'members.html', context)


def doctors(request):
    doctors = User.objects.order_by('email').filter(is_staff=True).filter(is_superuser=False)
    superusers = User.objects.order_by('email').filter(is_superuser=True)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create a doctor
            user = form.save(request)
            user.is_staff = True
            user.is_superuser = False
            user.save()

            # Activate the user
            email_address = EmailAddress.objects.get(email=user.email)
            email_address.verified = True
            email_address.save()

            return redirect('doctors')  # Redirect to a success page
    else:
        form = SignupForm()

    context = {
        'doctors': doctors,
        'superusers': superusers,
        'form': form,
    }

    return render(request, 'doctors.html', context)


# ENABLE/DISABLE A STAFF MEMBERS ACCOUNT:
@login_required
def disable_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Toggle the is_disabled field
    user.is_active = not user.is_active
    user.save()

    return HttpResponseRedirect(reverse('doctors'))


# ENABLE/DISABLE A SUPERUSER FROM A STAFF ACCOUNT:
@login_required
def toggle_superuser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if not user.is_active:
        print('user is disabled')
    else:
        user.is_superuser = not user.is_superuser
        user.save()

    return HttpResponseRedirect(reverse('doctors'))
