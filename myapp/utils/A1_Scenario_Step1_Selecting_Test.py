import A1_Scenario_Step1_Selecting_Test_Func as myFunc

myFunc.selectDFG()
myFunc.selectInput()
myFunc.selectActivity()

DFG_dict = {
    0: 'Test',

    1: 'DFG1',
    2: 'DFG1_Domain',
    3: 'DFG1_DomainConcept',
    4: 'DFG1_DomainConceptLevel',
    5: 'DFG1_featureValue',
    6: 'DFG1_featureValue_Domain',
    7: 'DFG1_featureValue_DomainConcept',
    8: 'DFG1_featureValue_DomainConceptLevel',


    9: 'DFG2',
    10: 'DFG2_Domain',
    11: 'DFG2_DomainConcept',
    12: 'DFG2_DomainConceptLevel',
    13: 'DFG2_featureValue',
    14: 'DFG2_featureValue_Domain',
    15: 'DFG2_featureValue_DomainConcept',
    16: 'DFG2_featureValue_DomainConceptLevel',


    17: 'DFG3', #All
    18: 'DFG3_Domain',
    19: 'DFG3_DomainConcept',
    20: 'DFG3_DomainConceptLevel',
    21: 'DFG3_feature',  # All
    22: 'DFG3_feature_Domain',
    23: 'DFG3_feature_DomainConcept',
    24: 'DFG3_feature_DomainConceptLevel',
    25: 'DFG3_featureValue',  # All
    26: 'DFG3_featureValue_Domain',
    27: 'DFG3_featureValue_DomainConcept',
    28: 'DFG3_featureValue_DomainConceptLevel',



    29: 'DFG4', #Absolute
    30: 'DFG4_Domain',
    31: 'DFG4_DomainConcept',
    32: 'DFG4_DomainConceptLevel',
    33: 'DFG4_feature',  # Absolute
    34: 'DFG4_feature_Domain',
    35: 'DFG4_feature_DomainConcept',
    36: 'DFG4_feature_DomainConceptLevel',
    37: 'DFG4_featureValue',  # Absolute
    38: 'DFG4_featureValue_Domain',
    39: 'DFG4_featureValue_DomainConcept',
    40: 'DFG4_featureValue_DomainConceptLevel',


    41: 'DFG5', #Relative
    42: 'DFG5_Domain',
    43: 'DFG5_DomainConcept',
    44: 'DFG5_DomainConceptLevel',
    45: 'DFG5_feature',  # Relative
    46: 'DFG5_feature_Domain',
    47: 'DFG5_feature_DomainConcept',
    48: 'DFG5_feature_DomainConceptLevel',
    49: 'DFG5_featureValue',  # Relative
    50: 'DFG5_featureValue_Domain',
    51: 'DFG5_featureValue_DomainConcept',
    52: 'DFG5_featureValue_DomainConceptLevel',


    53: 'DFG6',
    55: 'DFG6_Morbid',
}

input_dict = {
    1: 'main_Entities',
    2: 'main_Entities_plus_Disorder',
    3: 'main_Entities_plus_ICD',
    4: 'main_Entities_plus_ICD_level_doesnt_work',
    5: 'main_Entities_plus_SCT',
    6: 'main_Entities_plus_SCT_level',
    7: 'main_Entities_plus_SCT_Level_One',
    8: 'main_Entities_plus_ICD_one',
    9: 'main_Entities_plus_SCT_one',
}

Activity_dict = {
    1: 'Activity_Label',
    2: 'Concept_Label',
    3: 'Concept_Label_Level',
}