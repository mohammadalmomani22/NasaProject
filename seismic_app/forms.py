# seismic_app/forms.py
from django import forms

class DateRangeForm(forms.Form):
    from_date = forms.CharField(
        label='From Date (YYYY-MM-DD)',
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )
    to_date = forms.CharField(
        label='To Date (YYYY-MM-DD)',
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )
