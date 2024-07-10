from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json





class EventLogForm(forms.Form):
    dynamic_choice_EventLog = forms.ChoiceField(choices=[], label="Event Log")
    def __init__(self, *args, **kwargs):
        super(EventLogForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_EventLog'].choices = choices

class OtherEntitiesForm(forms.Form):
    dynamic_choice_OtherEntities = forms.ChoiceField(choices=[], label="Other Entities")
    def __init__(self, *args, **kwargs):
        super(OtherEntitiesForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_OtherEntities'].choices = choices


class OtherEntitiesRelForm(forms.Form):
    dynamic_choice_OtherEntitiesRel = forms.ChoiceField(choices=[], label="Other Entries Relationship")
    def __init__(self, *args, **kwargs):
        super(OtherEntitiesRelForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_OtherEntitiesRel'].choices = choices


class ActivitiesValueForm(forms.Form):
    dynamic_choice_ActivitiesValue = forms.ChoiceField(choices=[], label="Activities Value")
    def __init__(self, *args, **kwargs):
        super(ActivitiesValueForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_ActivitiesValue'].choices = choices


class DomainSelectionForm(forms.Form):
    dynamic_choice_Domain = forms.ChoiceField(choices=[], label="Domain")
    def __init__(self, *args, **kwargs):
        super(DomainSelectionForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_Domain'].choices = choices


class ICDForm(forms.Form):
    dynamic_choice_ICD = forms.ChoiceField(choices=[], label="ICD")
    def __init__(self, *args, **kwargs):
        super(ICDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_ICD'].choices = choices



class SnomedCtNodeForm(forms.Form):
    dynamic_choice_SnomedCt_Node = forms.ChoiceField(choices=[], label="SNOMED CT NODE")
    def __init__(self, *args, **kwargs):
        super(SnomedCtNodeForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_SnomedCt_Node'].choices = choices



class SnomedCtRelForm(forms.Form):
    dynamic_choice_SnomedCtRel = forms.ChoiceField(choices=[], label="SNOMED CT Relationship")
    def __init__(self, *args, **kwargs):
        super(SnomedCtRelForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_SnomedCtRel'].choices = choices



class DK1(forms.Form):
    dynamic_choice_DK1 = forms.ChoiceField(choices=[], label="DK1")
    def __init__(self, *args, **kwargs):
        super(DK1, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_DK1'].choices = choices



class DK2(forms.Form):
    dynamic_choice_DK2 = forms.ChoiceField(choices=[], label="DK2")
    def __init__(self, *args, **kwargs):
        super(DK2, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_DK2'].choices = choices


class DK3(forms.Form):
    dynamic_choice_DK3 = forms.ChoiceField(choices=[], label="The Relationship between Disorder and ICD Code")
    def __init__(self, *args, **kwargs):
        super(DK3, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_DK3'].choices = choices


class DK4(forms.Form):
    dynamic_choice_DK4 = forms.ChoiceField(choices=[], label="The relationship between ICD Code and SNOMED CT ID")
    def __init__(self, *args, **kwargs):
        super(DK4, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_DK4'].choices = choices

class DK5(forms.Form):
    dynamic_choice_DK5 = forms.ChoiceField(choices=[], label="The relationship between Event Activities and SNOMED CT ID")
    def __init__(self, *args, **kwargs):
        super(DK5, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_DK5'].choices = choices


class DK61(forms.Form):
    dynamic_choice_DK61 = forms.ChoiceField(choices=[], label="The relationship between Event Activities and Domain")
    def __init__(self, *args, **kwargs):
        super(DK61, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_DK61'].choices = choices

class DK62(forms.Form):
    dynamic_choice_DK62 = forms.ChoiceField(choices=[], label="The relationship between Domain and SNOMED CT ID")
    def __init__(self, *args, **kwargs):
        super(DK62, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_DK62'].choices = choices


class DK7(forms.Form):
    dynamic_choice_DK7 = forms.ChoiceField(choices=[], label="The relationship between Events and Disorders")
    def __init__(self, *args, **kwargs):
        super(DK7, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/3_previewOptionSheetNames.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_DK7'].choices = choices


