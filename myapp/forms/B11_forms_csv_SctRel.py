from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json







class SctrS0(forms.Form):
    dynamic_choice_B11_1 = forms.ChoiceField(choices=[], label="First SNOMED CT ID")

    def __init__(self, *args, **kwargs):
        super(SctrS0, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/11_octRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B11_1'].choices = choices


class SctrS0_code(forms.Form):
    dynamic_choice_B11_2 = forms.ChoiceField(choices=[], label="First SNOMED CT Code")

    def __init__(self, *args, **kwargs):
        super(SctrS0_code, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/11_octRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B11_2'].choices = choices


class SctrS1(forms.Form):
    dynamic_choice_B11_3 = forms.ChoiceField(choices=[], label="Second SNOMED CT ID")

    def __init__(self, *args, **kwargs):
        super(SctrS1, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/11_octRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B11_3'].choices = choices


class SctrS1_code(forms.Form):
    dynamic_choice_B11_4 = forms.ChoiceField(choices=[], label="First SNOMED CT Code")

    def __init__(self, *args, **kwargs):
        super(SctrS1_code, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/11_octRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B11_4'].choices = choices

