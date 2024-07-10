
from django import forms





class BrowsingMethodForm(forms.Form):
    browsingMethodMode = forms.ChoiceField(
        choices=[
            ('1', 'Google Drive'),
            ('2', 'Local')
        ],
        widget=forms.RadioSelect,
        label=''
    )


class FileNameBox(forms.Form):
    fileNameMode = forms.CharField(
        label='File Name:',
        max_length=100,
        required=True
    )


class LocationTextBox(forms.Form):
    locationTextMode = forms.CharField(
        label='Please Enter Location of File?',
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'size': '200'})
    )

class ServiceKeyTextBox(forms.Form):
    serviceKeyTextMode = forms.CharField(
        label='Please Enter the location of Service Account Key file for Google Cloud Platform?',
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'size': '200'})
    )




