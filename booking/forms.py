from django import forms
from .models import Demonstration, CalendarInstance


class DemonstrationForm(forms.ModelForm):
    class Meta:
        model = Demonstration
        fields = ['demo_guest', 'demo_email', 'demo_phone', 'demo_date', 'demo_time']

    def __init__(self, *args, **kwargs):
        super(DemonstrationForm, self).__init__(*args, **kwargs)
        self.fields['demo_guest'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Full Name',
            }),
        self.fields['demo_email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email Address',
            }),
        self.fields['demo_phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Phone',
            }),
        self.fields['demo_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Date',
            }),
        self.fields['demo_time'].widget.attrs.update({
            'class': 'form-control'
            }),


class CalendarInstanceForm(forms.ModelForm):
    class Meta:
        model = CalendarInstance
        fields = ['request', 'booked']
        labels = {'request': 'Need anything special?'}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label
