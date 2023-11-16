# from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.core.management import call_command
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Disable User
from django.http import HttpResponseRedirect
from django.urls import reverse


User = get_user_model()


def dashboard(request):
    return render(request, 'dashboard.html')


def bookings(request):
    return render(request, 'bookings.html')


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
        staff_users = User.objects.filter(is_staff=True)

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
    }

    return render(request, 'staff.html', context)


@login_required
def disable_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Toggle the is_disabled field
    user.is_active = not user.is_active
    user.save()

    return HttpResponseRedirect(reverse('staff'))
