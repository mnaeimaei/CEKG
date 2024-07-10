from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json







class ApIdForm(forms.Form):
    dynamic_choice_B7_1 = forms.ChoiceField(choices=[], label="Activity Feature ID")

    def __init__(self, *args, **kwargs):
        super(ApIdForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/7_acPropertiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B7_1'].choices = choices


class ApActivityNameForm(forms.Form):
    dynamic_choice_B7_2 = forms.ChoiceField(choices=[], label="Activity")

    def __init__(self, *args, **kwargs):
        super(ApActivityNameForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/7_acPropertiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B7_2'].choices = choices


class ApActivitySynonymForm(forms.Form):
    dynamic_choice_B7_3 = forms.ChoiceField(choices=[], label="Activity Synonym")

    def __init__(self, *args, **kwargs):
        super(ApActivitySynonymForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/7_acPropertiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B7_3'].choices = choices



class ApLabelForm(forms.Form):
    dynamic_choice_B7_4 = forms.ChoiceField(choices=[], label="Activity Feature")

    def __init__(self, *args, **kwargs):
        super(ApLabelForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/7_acPropertiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B7_4'].choices = choices


class ApValueForm(forms.Form):
    dynamic_choice_B7_5 = forms.ChoiceField(choices=[], label="Activity Feature Value")

    def __init__(self, *args, **kwargs):
        super(ApValueForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/7_acPropertiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B7_5'].choices = choices

