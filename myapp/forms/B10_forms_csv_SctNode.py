from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json










class SctnConceptId(forms.Form):
    dynamic_choice_B10_1 = forms.ChoiceField(choices=[], label="SNOMED CT ID")

    def __init__(self, *args, **kwargs):
        super(SctnConceptId, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/10_octNodeOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B10_1'].choices = choices


class SctnConceptCode(forms.Form):
    dynamic_choice_B10_2 = forms.ChoiceField(choices=[], label="SNOMED CT Code")

    def __init__(self, *args, **kwargs):
        super(SctnConceptCode, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/10_octNodeOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B10_2'].choices = choices


class SctnTermA(forms.Form):
    dynamic_choice_B10_3 = forms.ChoiceField(choices=[], label="SNOMED CT Description Part1")

    def __init__(self, *args, **kwargs):
        super(SctnTermA, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/10_octNodeOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B10_3'].choices = choices


class SctnTermB(forms.Form):
    dynamic_choice_B10_4 = forms.ChoiceField(choices=[], label="SNOMED CT Description Part2")

    def __init__(self, *args, **kwargs):
        super(SctnTermB, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/10_octNodeOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B10_4'].choices = choices


class SctnSemanticTags(forms.Form):
    dynamic_choice_B10_5 = forms.ChoiceField(choices=[], label="SNOMED CT Semantic Tags")

    def __init__(self, *args, **kwargs):
        super(SctnSemanticTags, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/10_octNodeOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B10_5'].choices = choices


class SctnConceptType(forms.Form):
    dynamic_choice_B10_6 = forms.ChoiceField(choices=[], label="SNOMED CT Concept Type")

    def __init__(self, *args, **kwargs):
        super(SctnConceptType, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/10_octNodeOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B10_6'].choices = choices


class SctnLevels(forms.Form):
    dynamic_choice_B10_7 = forms.ChoiceField(choices=[], label="SNOMED CT Level")

    def __init__(self, *args, **kwargs):
        super(SctnLevels, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/10_octNodeOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B10_7'].choices = choices

