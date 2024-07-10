from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json








class IdcClinicalEntityForm(forms.Form):
    dynamic_choice_B9_1 = forms.ChoiceField(choices=[], label="ICD column")

    def __init__(self, *args, **kwargs):
        super(IdcClinicalEntityForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/9_icdOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B9_1'].choices = choices


class IdcCodeForm(forms.Form):
    dynamic_choice_B9_2 = forms.ChoiceField(choices=[], label="ICD Code")

    def __init__(self, *args, **kwargs):
        super(IdcCodeForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/9_icdOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B9_2'].choices = choices


class IdcVersionForm(forms.Form):
    dynamic_choice_B9_3 = forms.ChoiceField(choices=[], label="ICD Code Version")

    def __init__(self, *args, **kwargs):
        super(IdcVersionForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/9_icdOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B9_3'].choices = choices


class IdcCodeTitleForm(forms.Form):
    dynamic_choice_B9_4 = forms.ChoiceField(choices=[], label="ICD Code Title")

    def __init__(self, *args, **kwargs):
        super(IdcCodeTitleForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/9_icdOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B9_4'].choices = choices


