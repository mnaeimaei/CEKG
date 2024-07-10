from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json






class Domain1ActivityForm(forms.Form):
    dynamic_choice_B17_1 = forms.ChoiceField(choices=[], label="Activity")

    def __init__(self, *args, **kwargs):
        super(Domain1ActivityForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/17_dk61Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B17_1'].choices = choices


class Domain1ActivitySynonymForm(forms.Form):
    dynamic_choice_B17_2 = forms.ChoiceField(choices=[], label="Activity Synonym")

    def __init__(self, *args, **kwargs):
        super(Domain1ActivitySynonymForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/17_dk61Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B17_2'].choices = choices


class Domain1DomainForm(forms.Form):
    dynamic_choice_B17_3 = forms.ChoiceField(choices=[], label="Domain")

    def __init__(self, *args, **kwargs):
        super(Domain1DomainForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/17_dk61Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B17_3'].choices = choices

