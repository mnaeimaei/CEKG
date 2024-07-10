from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json




class BroweserButton(forms.Form):
    BroweserButtonMode = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={'type': 'submit', 'value': 'FINISH'})
    )


