from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json







class Dk5ActivityForm(forms.Form):
    dynamic_choice_B16_1 = forms.ChoiceField(choices=[], label="Activity")

    def __init__(self, *args, **kwargs):
        super(Dk5ActivityForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/16_dk5Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B16_1'].choices = choices


class Dk5ActivitySynonymForm(forms.Form):
    dynamic_choice_B16_2 = forms.ChoiceField(choices=[], label="Activity Synonym")

    def __init__(self, *args, **kwargs):
        super(Dk5ActivitySynonymForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/16_dk5Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B16_2'].choices = choices


class Dk5OtcForm(forms.Form):
    dynamic_choice_B16_3 = forms.ChoiceField(choices=[], label="SNOMED CT ID")

    def __init__(self, *args, **kwargs):
        super(Dk5OtcForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/16_dk5Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B16_3'].choices = choices


class Dk5SctCodeForm(forms.Form):
    dynamic_choice_B16_4 = forms.ChoiceField(choices=[], label="SNOMED CT Code")

    def __init__(self, *args, **kwargs):
        super(Dk5SctCodeForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/16_dk5Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B16_4'].choices = choices

