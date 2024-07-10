from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField


class MainDfgForm(forms.Form):
    mainDfgMode = forms.ChoiceField(
        choices=[('dfg1Mode', 'Independent Multi-Morbid Patient Care Pathways'),
                 ('dfg2Mode', 'Dependent Multi-Morbid Patient Care Pathways'),
                 ('dfg3Mode', 'Consolidated Multi-Morbid Patient Care Pathways with Overlapping Activities'),
                 ('dfg4Mode', 'Consolidated Multi-Morbid Patient Care Pathways with Individual Counts'),
                 ('dfg5Mode', 'Consolidated Patient Care Pathways with Aggregated Occurrences'),
                 ('dfg6Mode', 'Multi-Morbid Patient Care Pathways Based on Admission')
    ],
        widget=forms.RadioSelect,
        label=''
    )

class Dfg1Form(forms.Form):
    dfg1Mode = forms.ChoiceField(
        choices=[
            ('1', 'Activities label'),
            ('2', 'Activities label + Domain of activities'),
            ('3', 'Activities label + Domain of activities using SNOMED_CT'),
            ('4', 'Activities label + Domain of activities using SNOMED_CT in specific distance'),
            ('5', 'Activities value + Activities feature'),
            ('6', 'Activities value + Activities feature + Domain of activities'),
            ('7', 'Activities value + Activities feature + Domain of activities using SNOMED_CT'),
            ('8','Activities value + Activities feature + Domain of activities using SNOMED_CT in specific distance')
        ],
        widget=forms.RadioSelect,
        label = '',
    required = False

    )


class Dfg2Form(forms.Form):
    dfg2Mode = forms.ChoiceField(
        choices=[
            ('9', 'Activities label'),
            ('10', 'Activities label + Domain of activities'),
            ('11', 'Activities label + Domain of activities using SNOMED_CT'),
            ('12', 'Activities label + Domain of activities using SNOMED_CT in specific distance'),
            ('13', 'Activities value + Activities feature'),
            ('14', 'Activities value + Activities feature + Domain of activities'),
            ('15', 'Activities value + Activities feature + Domain of activities using SNOMED_CT'),
            ('16','Activities value + Activities feature + Domain of activities using SNOMED_CT in specific distance')
        ],
        widget=forms.RadioSelect,
        label='',
    required = False
    )

class Dfg3Form(forms.Form):
    dfg3Mode = forms.ChoiceField(
        choices=[
            ('17', 'Activities label'),
            ('18', 'Activities label + Domain of activities'),
            ('19', 'Activities label + Domain of activities using SNOMED_CT'),
            ('20', 'Activities label + Domain of activities using SNOMED_CT in specific distance'),
            ('21', 'Activities value'),
            ('22', 'Activities value + Domain of activities'),
            ('23', 'Activities value + Domain of activities using SNOMED_CT'),
            ('24', 'Activities value + Domain of activities using SNOMED_CT in specific distance'),
            ('25', 'Activities value + Activities feature'),
            ('26', 'Activities value + Activities feature + Domain of activities'),
            ('27', 'Activities value + Activities feature + Domain of activities using SNOMED_CT'),
            ('28','Activities value + Activities feature + Domain of activities using SNOMED_CT in specific distance')
        ],
        widget=forms.RadioSelect,
        label='',
    required = False
    )

class Dfg4Form(forms.Form):
    dfg4Mode = forms.ChoiceField(
        choices=[
            ('29', 'Activities label'),
            ('30', 'Activities label + Domain of activities'),
            ('31', 'Activities label + Domain of activities using SNOMED_CT'),
            ('32', 'Activities label + Domain of activities using SNOMED_CT in specific distance'),
            ('33', 'Activities value'),
            ('34', 'Activities value + Domain of activities'),
            ('35', 'Activities value + Domain of activities using SNOMED_CT'),
            ('36', 'Activities value + Domain of activities using SNOMED_CT in specific distance'),
            ('37', 'Activities value + Activities feature'),
            ('38', 'Activities value + Activities feature + Domain of activities'),
            ('39', 'Activities value + Activities feature + Domain of activities using SNOMED_CT'),
            ('40','Activities value + Activities feature + Domain of activities using SNOMED_CT in specific distance')
        ],
        widget=forms.RadioSelect,
        label='',
    required = False
    )

class Dfg5Form(forms.Form):
    dfg5Mode = forms.ChoiceField(
        choices=[
            ('41', 'Activities label'),
            ('42', 'Activities label + Domain of activities'),
            ('43', 'Activities label + Domain of activities using SNOMED_CT'),
            ('44', 'Activities label + Domain of activities using SNOMED_CT in specific distance'),
            ('45', 'Activities value'),
            ('46', 'Activities value + Domain of activities'),
            ('47', 'Activities value + Domain of activities using SNOMED_CT'),
            ('48', 'Activities value + Domain of activities using SNOMED_CT in specific distance'),
            ('49', 'Activities value + Activities feature'),
            ('50', 'Activities value + Activities feature + Domain of activities'),
            ('51', 'Activities value + Activities feature + Domain of activities using SNOMED_CT'),
            ('52','Activities value + Activities feature + Domain of activities using SNOMED_CT in specific distance')
        ],
        widget=forms.RadioSelect,
        label='',
    required = False
    )

class Dfg6Form(forms.Form):
    dfg6Mode = forms.ChoiceField(
        choices=[
            ('53', 'Not Showing Morbids'),
            ('54', 'Showing Morbids')
        ],
        widget=forms.RadioSelect,
        label='',
        required = False
    )


class InputForm(forms.Form):
    inputMode = forms.ChoiceField(
        choices=[
            ('1', 'For Event Log Entities'),
            ('2', 'For Event Log Entities + Disorders'),
            ('3', 'For Event Log Entities + Disorders Using ICD Codes'),
            ('4', 'For Event Log Entities + Disorders Using ICD Codes of Ancestors with a distance of N '),
            ('5', 'For Event Log Entities + Disorders Using SNOMED CT ID'),
            ('6', 'For Event Log Entities + Disorders Using SNOMED CT ID of Ancestors with a distance of N'),
            ('7', 'For Event Log Entities + Disorders Using SNOMED CT ID of Ancestors with a distance of 1'),
            ('8', 'For Event Log Entities + One Disorder Using its ICD Codes'),
            ('9', 'For Event Log Entities + One Disorder Using its SNOMED CT Codes')
        ],
        widget=forms.RadioSelect,
        label='',
        required = False
    )


class InputFormDFG6(forms.Form):
    inputModeDFG6 = forms.ChoiceField(
        choices=[
            ('option', 'For Event Log Entities, Disorders')
        ],
        widget=forms.RadioSelect,
        label='',
        required = False
    )





class ActivitySelectionForm(forms.Form):
    activityMode = forms.ChoiceField(
        choices=[
            ('1', 'Activity label'),
            ('2', 'Using SCT Concept for Activity label'),
            ('3', 'Using SCT Concept for of Ancestors with a specific distance for Activity label ,(Default =1)')
        ],
        widget=forms.RadioSelect,
        label='',
        required = False
    )

class ActivityFormDFG6(forms.Form):
    activityModeDFG6 = forms.ChoiceField(
        choices=[
            ('option', 'without label')
        ],
        widget=forms.RadioSelect,
        label='',
        required = False
    )




class NextButton1(forms.Form):
    nextButton1Mode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'type': 'submit', 'value': 'Next'})
    )



