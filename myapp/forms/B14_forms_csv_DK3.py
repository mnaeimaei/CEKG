from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json





class Dk3DisordersForm(forms.Form):
    dynamic_choice_B14_1 = forms.ChoiceField(choices=[], label="Disorder Entity Descriptor")

    def __init__(self, *args, **kwargs):
        super(Dk3DisordersForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/14_dk3Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B14_1'].choices = choices


class Dk3IcdCodeForm(forms.Form):
    dynamic_choice_B14_2 = forms.ChoiceField(choices=[], label="ICD Code")

    def __init__(self, *args, **kwargs):
        super(Dk3IcdCodeForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/14_dk3Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B14_2'].choices = choices

