from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json





class Domain2DomainForm(forms.Form):
    dynamic_choice_B18_1 = forms.ChoiceField(choices=[], label="Domain")

    def __init__(self, *args, **kwargs):
        super(Domain2DomainForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/18_dk62Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B18_1'].choices = choices


class Domain2OTCForm(forms.Form):
    dynamic_choice_B18_2 = forms.ChoiceField(choices=[], label="SNOMED CT ID")

    def __init__(self, *args, **kwargs):
        super(Domain2OTCForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/18_dk62Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B18_2'].choices = choices


class Domain2SCTCodeForm(forms.Form):
    dynamic_choice_B18_3 = forms.ChoiceField(choices=[], label="SNOMED CT Code")

    def __init__(self, *args, **kwargs):
        super(Domain2SCTCodeForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/18_dk62Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B18_3'].choices = choices

