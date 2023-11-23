# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from booking.models import Appointments


User = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['app_member', 'app_type', 'app_date', 'app_time']

    def __init__(self, *args, **kwargs):
        super(AppointmentsForm, self).__init__(*args, **kwargs)
        self.fields['app_type'].widget.attrs.update({
            'class': 'form-control',
            }),
        self.fields['app_date'].widget.attrs.update({
            'class': 'form-control',
            'id': 'id_demo_date',
            'placeholder': 'Date',
            }),
        self.fields['app_time'].widget.attrs.update({
            'class': 'form-control'
            }),