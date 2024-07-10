from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField

class LoginForm(forms.Form):
    usernameMode = forms.CharField(label='Username', max_length=100)
    passwordMode = forms.CharField(label='Password', widget=forms.PasswordInput)


class LoginButton(forms.Form):
    LoginButtonMode = forms.CharField(
        label='Click to Login',
        widget=forms.TextInput(attrs={'type': 'submit', 'value': 'Login'})
    )

