
from django import forms


class UserNameNeo(forms.Form):
    userNameNeoMode = forms.CharField(
        label='',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'size': '100'})
    )


class PassWordNeo(forms.Form):
    passWordNeoMode = forms.CharField(
        label='',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'size': '100'})
    )




