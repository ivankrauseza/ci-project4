from django import forms
from booking.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['member', 'date', 'meal']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['member'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Full Name',
            }),
        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Date',
            }),
        self.fields['meal'].widget.attrs.update({
            'class': 'form-control'
            }),
