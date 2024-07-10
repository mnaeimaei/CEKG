from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json







class OerOrigin1Form(forms.Form):
    dynamic_choice_B6_1 = forms.ChoiceField(choices=[], label="First Entity Origin")

    def __init__(self, *args, **kwargs):
        super(OerOrigin1Form, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/6_otherEntitiesRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B6_1'].choices = choices


class OerID1Form(forms.Form):
    dynamic_choice_B6_2 = forms.ChoiceField(choices=[], label="First Entity ID")

    def __init__(self, *args, **kwargs):
        super(OerID1Form, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/6_otherEntitiesRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B6_2'].choices = choices


class OerOrigin2Form(forms.Form):
    dynamic_choice_B6_3 = forms.ChoiceField(choices=[], label="Second Entity Origin")

    def __init__(self, *args, **kwargs):
        super(OerOrigin2Form, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/6_otherEntitiesRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B6_3'].choices = choices


class OerID2Form(forms.Form):
    dynamic_choice_B6_4 = forms.ChoiceField(choices=[], label="Second Entity ID")

    def __init__(self, *args, **kwargs):
        super(OerID2Form, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/6_otherEntitiesRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B6_4'].choices = choices

