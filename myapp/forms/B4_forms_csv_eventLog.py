from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json


class EnNumForm(forms.Form):

    dynamic_choice_B4_1 = forms.ChoiceField(
        choices=[('0', 'please select')] + [(str(i), str(i)) for i in range(1, 21)],
        label="Number of Entities",
    )



class EventIdTitleForm(forms.Form):
    dynamic_choice_B4_2 = forms.ChoiceField(choices=[], label="Event ID")
    def __init__(self, *args, **kwargs):
        super(EventIdTitleForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_2'].choices = choices

class ActivityForm(forms.Form):
    dynamic_choice_B4_3 = forms.ChoiceField(choices=[], label="Activity")
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_3'].choices = choices


class ActivitySynonymForm(forms.Form):
    dynamic_choice_B4_4 = forms.ChoiceField(choices=[], label="Activity Synonym")
    def __init__(self, *args, **kwargs):
        super(ActivitySynonymForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_4'].choices = choices


class TimestampForm(forms.Form):
    dynamic_choice_B4_5 = forms.ChoiceField(choices=[], label="Timestamp")
    def __init__(self, *args, **kwargs):
        super(TimestampForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_5'].choices = choices


class ActivityValueIDForm(forms.Form):
    dynamic_choice_B4_6 = forms.ChoiceField(choices=[], label="Activity ID")
    def __init__(self, *args, **kwargs):
        super(ActivityValueIDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_6'].choices = choices


class ActivityPropertiesIDForm(forms.Form):
    dynamic_choice_B4_7 = forms.ChoiceField(choices=[], label="Activity Features ID")
    def __init__(self, *args, **kwargs):
        super(ActivityPropertiesIDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_7'].choices = choices



class Entity1IDForm(forms.Form):
    dynamic_choice_B4_8 = forms.ChoiceField(choices=[], label="Entity 1 ID")
    def __init__(self, *args, **kwargs):
        super(Entity1IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_8'].choices = choices



class Entity2IDForm(forms.Form):
    dynamic_choice_B4_9 = forms.ChoiceField(choices=[], label="Entity 2 ID")
    def __init__(self, *args, **kwargs):
        super(Entity2IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_9'].choices = choices



class Entity3IDForm(forms.Form):
    dynamic_choice_B4_10 = forms.ChoiceField(choices=[], label="Entity 3 ID")
    def __init__(self, *args, **kwargs):
        super(Entity3IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_10'].choices = choices



class Entity4IDForm(forms.Form):
    dynamic_choice_B4_11 = forms.ChoiceField(choices=[], label="Entity 4 ID")
    def __init__(self, *args, **kwargs):
        super(Entity4IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_11'].choices = choices


class Entity5IDForm(forms.Form):
    dynamic_choice_B4_12 = forms.ChoiceField(choices=[], label="Entity 5 ID")
    def __init__(self, *args, **kwargs):
        super(Entity5IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_12'].choices = choices


class Entity6IDForm(forms.Form):
    dynamic_choice_B4_13 = forms.ChoiceField(choices=[], label="Entity 6 ID")
    def __init__(self, *args, **kwargs):
        super(Entity6IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_13'].choices = choices

class Entity7IDForm(forms.Form):
    dynamic_choice_B4_14 = forms.ChoiceField(choices=[], label="Entity 7 ID")
    def __init__(self, *args, **kwargs):
        super(Entity7IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_14'].choices = choices


class Entity8IDForm(forms.Form):
    dynamic_choice_B4_15 = forms.ChoiceField(choices=[], label="Entity 8 ID")
    def __init__(self, *args, **kwargs):
        super(Entity8IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_15'].choices = choices

class Entity9IDForm(forms.Form):
    dynamic_choice_B4_16 = forms.ChoiceField(choices=[], label="Entity 9 ID")
    def __init__(self, *args, **kwargs):
        super(Entity9IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_16'].choices = choices


class Entity10IDForm(forms.Form):
    dynamic_choice_B4_17 = forms.ChoiceField(choices=[], label="Entity 10 ID")
    def __init__(self, *args, **kwargs):
        super(Entity10IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_17'].choices = choices


class Entity11IDForm(forms.Form):
    dynamic_choice_B4_18 = forms.ChoiceField(choices=[], label="Entity 11 ID")
    def __init__(self, *args, **kwargs):
        super(Entity11IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_18'].choices = choices

class Entity12IDForm(forms.Form):
    dynamic_choice_B4_19 = forms.ChoiceField(choices=[], label="Entity 12 ID")
    def __init__(self, *args, **kwargs):
        super(Entity12IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_19'].choices = choices


class Entity13IDForm(forms.Form):
    dynamic_choice_B4_20 = forms.ChoiceField(choices=[], label="Entity 13 ID")
    def __init__(self, *args, **kwargs):
        super(Entity13IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_20'].choices = choices


class Entity14IDForm(forms.Form):
    dynamic_choice_B4_21 = forms.ChoiceField(choices=[], label="Entity 14 ID")
    def __init__(self, *args, **kwargs):
        super(Entity14IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_21'].choices = choices


class Entity15IDForm(forms.Form):
    dynamic_choice_B4_22 = forms.ChoiceField(choices=[], label="Entity 15 ID")
    def __init__(self, *args, **kwargs):
        super(Entity15IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_22'].choices = choices


class Entity16IDForm(forms.Form):
    dynamic_choice_B4_23 = forms.ChoiceField(choices=[], label="Entity 16 ID")
    def __init__(self, *args, **kwargs):
        super(Entity16IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_23'].choices = choices



class Entity17IDForm(forms.Form):
    dynamic_choice_B4_24 = forms.ChoiceField(choices=[], label="Entity 17 ID")
    def __init__(self, *args, **kwargs):
        super(Entity17IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_24'].choices = choices



class Entity18IDForm(forms.Form):
    dynamic_choice_B4_25 = forms.ChoiceField(choices=[], label="Entity 18 ID")
    def __init__(self, *args, **kwargs):
        super(Entity18IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_25'].choices = choices



class Entity19IDForm(forms.Form):
    dynamic_choice_B4_26 = forms.ChoiceField(choices=[], label="Entity 19 ID")
    def __init__(self, *args, **kwargs):
        super(Entity19IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_26'].choices = choices



class Entity20IDForm(forms.Form):
    dynamic_choice_B4_27 = forms.ChoiceField(choices=[], label="Entity 20 ID")
    def __init__(self, *args, **kwargs):
        super(Entity20IDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_27'].choices = choices


class Entity1OriginForm(forms.Form):
    dynamic_choice_B4_28 = forms.ChoiceField(choices=[], label="Entity 1 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity1OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_28'].choices = choices


class Entity2OriginForm(forms.Form):
    dynamic_choice_B4_29 = forms.ChoiceField(choices=[], label="Entity 2 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity2OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_29'].choices = choices

class Entity3OriginForm(forms.Form):
    dynamic_choice_B4_30 = forms.ChoiceField(choices=[], label="Entity 3 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity3OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_30'].choices = choices


class Entity4OriginForm(forms.Form):
    dynamic_choice_B4_31 = forms.ChoiceField(choices=[], label="Entity 4 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity4OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_31'].choices = choices

class Entity5OriginForm(forms.Form):
    dynamic_choice_B4_32 = forms.ChoiceField(choices=[], label="Entity 5 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity5OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_32'].choices = choices


class Entity6OriginForm(forms.Form):
    dynamic_choice_B4_33 = forms.ChoiceField(choices=[], label="Entity 6 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity6OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_33'].choices = choices






class Entity7OriginForm(forms.Form):
    dynamic_choice_B4_34 = forms.ChoiceField(choices=[], label="Entity 7 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity7OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_34'].choices = choices

class Entity8OriginForm(forms.Form):
    dynamic_choice_B4_35 = forms.ChoiceField(choices=[], label="Entity 8 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity8OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_35'].choices = choices


class Entity9OriginForm(forms.Form):
    dynamic_choice_B4_36 = forms.ChoiceField(choices=[], label="Entity 9 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity9OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_36'].choices = choices


class Entity10OriginForm(forms.Form):
    dynamic_choice_B4_37 = forms.ChoiceField(choices=[], label="Entity 10 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity10OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_37'].choices = choices


class Entity11OriginForm(forms.Form):
    dynamic_choice_B4_38 = forms.ChoiceField(choices=[], label="Entity 11 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity11OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_38'].choices = choices


class Entity12OriginForm(forms.Form):
    dynamic_choice_B4_39 = forms.ChoiceField(choices=[], label="Entity 12 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity12OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_39'].choices = choices



class Entity13OriginForm(forms.Form):
    dynamic_choice_B4_40 = forms.ChoiceField(choices=[], label="Entity 13 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity13OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_40'].choices = choices



class Entity14OriginForm(forms.Form):
    dynamic_choice_B4_41 = forms.ChoiceField(choices=[], label="Entity 14 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity14OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_41'].choices = choices



class Entity15OriginForm(forms.Form):
    dynamic_choice_B4_42 = forms.ChoiceField(choices=[], label="Entity 15 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity15OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_42'].choices = choices



class Entity16OriginForm(forms.Form):
    dynamic_choice_B4_43 = forms.ChoiceField(choices=[], label="Entity 16 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity16OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_43'].choices = choices


class Entity17OriginForm(forms.Form):
    dynamic_choice_B4_44 = forms.ChoiceField(choices=[], label="Entity 17 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity17OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_44'].choices = choices


class Entity18OriginForm(forms.Form):
    dynamic_choice_B4_45 = forms.ChoiceField(choices=[], label="Entity 18 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity18OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_45'].choices = choices

class Entity19OriginForm(forms.Form):
    dynamic_choice_B4_46 = forms.ChoiceField(choices=[], label="Entity 19 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity19OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_46'].choices = choices


class Entity20OriginForm(forms.Form):
    dynamic_choice_B4_47 = forms.ChoiceField(choices=[], label="Entity 20 Origin")
    def __init__(self, *args, **kwargs):
        super(Entity20OriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory = "./myapp/Data/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/4_eventLogOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B4_47'].choices = choices


