# from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.core.management import call_command
from django.contrib.auth.decorators import login_required
from booking.models import Booking, Demonstration, Calendar, CalendarInstance
from django.contrib.auth.models import User
# Disable User
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date, datetime
from booking.forms import CalendarInstanceForm


# User = get_user_model()


def dashboard(request):
    today = date.today()
    formatted_today = today.strftime("%Y-%m-%d")
    print(formatted_today)
    booking_data = Booking.objects.filter(date__exact=today).count()
    tour_data = Demonstration.objects.filter(demo_date__exact=today).count()
    context = {
        'booking_data_count': booking_data,
        'tour_data_count': tour_data,
    }
    return render(request, 'dashboard.html', context)


@login_required
def tours(request):
    tour_data = Demonstration.objects.all().order_by('demo_date')
    return render(request, 'tours.html', {'tour_data': tour_data})


@login_required
def bookings(request):
    cal_data = Calendar.objects.all()
    today = datetime.now()
    js_timestamp = int(today.timestamp() * 1000)
    cal_instance = CalendarInstance.objects.filter(date__gte=js_timestamp)

    context = {
        'cal_data': cal_data,
        'cal_instance': cal_instance,
    }

    return render(request, 'bookings.html', context)


@login_required
def bookings_update(request, pk):
    record = CalendarInstance.objects.get(pk=pk)

    if request.method == 'POST':
        form = CalendarInstanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    else:
        form = CalendarInstanceForm(instance=record)

    context = {
        'record': record,
        'form': form
    }
    return render(request, 'update_record.html', context)


@login_required
def bookings_view(request, pk):
    your_object = get_object_or_404(CalendarInstance, pk=pk)
    return render(request, 'view_record.html', {'your_object': your_object})


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
