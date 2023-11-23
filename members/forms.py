from django import forms
from booking.models import Appointments


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
