from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField


class StartButton(forms.Form):
    StartButtonMode = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={'type': 'submit', 'value': 'START'})
    )


