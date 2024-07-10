from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json





class Dk4IcdCodeForm(forms.Form):
    dynamic_choice_B15_1 = forms.ChoiceField(choices=[], label="ICD Code")

    def __init__(self, *args, **kwargs):
        super(Dk4IcdCodeForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/15_dk4Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B15_1'].choices = choices


class Dk4OtcForm(forms.Form):
    dynamic_choice_B15_2 = forms.ChoiceField(choices=[], label="SNOMED CT ID")

    def __init__(self, *args, **kwargs):
        super(Dk4OtcForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/15_dk4Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B15_2'].choices = choices

