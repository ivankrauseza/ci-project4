# from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Users
from django.contrib.auth.models import User
# Booking Modals
from booking.models import Appointments
# Disable User
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from .forms import AppointmentsForm


# User = get_user_model()


@login_required
def dashboard(request):
    today = date.today()
    formatted_today = today.strftime("%Y-%m-%d")
    print(formatted_today)
    open_appointments = Appointments.objects.filter(confirmed=False).count()
    context = {
        'open_appointments': open_appointments,
    }
    return render(request, 'dashboard.html', context)


@login_required
def patients(request):
    print(request.user.id)
    patients = Appointments.objects.all().filter(confirmed=False).order_by('app_date')
    birds = Appointments.objects.all().filter(completed=False, doctor=request.user.id).order_by('app_date')
    context = {
        'patients': patients,
        'birds': birds
    }
    return render(request, 'patients.html', context)
# GP sets the owner field to themselves


@login_required
def patients_detail(request, post_id):
    record = get_object_or_404(Appointments, id=post_id)
    if request.method == 'POST':
        form = AppointmentsForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is saved!")
            return redirect('patients')  # Redirect to a success page
    else:
        form = AppointmentsForm()

    context = {
        'record': record,
        'form': form,
    }

    return render(request, 'patients_detail.html', context)


def patients_accept(request, post_id):
    post = get_object_or_404(Appointments, pk=post_id)

    if request.method == 'POST':
        post.doctor = request.user.id
        post.confirmed = True
        post.save()
        return redirect('patients')

    return render(request, 'patients_accept.html', {'post': post})


def patients_delete(request, post_id):
    post = get_object_or_404(Appointments, pk=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('patients')

    return render(request, 'patients_delete.html', {'post': post})


def members(request):
    if request.method == 'GET':
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


def staff(request):

    if request.method == 'GET':
        staff_users = User.objects.order_by('email').filter(is_staff=True, is_superuser=False)
        super_users = User.objects.order_by('email').filter(is_staff=True, is_superuser=True)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create an inactive user
            user = form.save(request)
            user.is_staff = True
            user.is_superuser = False
            user.save()

            # Activate the user
            email_address = EmailAddress.objects.get(email=user.email)
            email_address.verified = True
            email_address.save()

            return redirect('staff')  # Redirect to a success page
    else:
        form = SignupForm()

    context = {
        'form': form,
        'staff_users': staff_users,
        'super_users': super_users,
    }

    return render(request, 'staff.html', context)


# ENABLE/DISABLE A STAFF MEMBERS ACCOUNT:
@login_required
def disable_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Toggle the is_disabled field
    user.is_active = not user.is_active
    user.save()

    return HttpResponseRedirect(reverse('staff'))


# ENABLE/DISABLE A SUPERUSER FROM A STAFF ACCOUNT:
@login_required
def toggle_superuser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if not user.is_active:
        print('user is disabled')
    else:
        user.is_superuser = not user.is_superuser
        user.save()

    return HttpResponseRedirect(reverse('staff'))
