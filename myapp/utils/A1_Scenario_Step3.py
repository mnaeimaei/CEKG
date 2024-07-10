
import A1_Scenario_Step2 as Sc0
import A1_Scenario_Step3_Func as Func

DFG=Sc0.DFG
print("DFG=",DFG)

myInput=Sc0.myInput
print("myInput=",myInput)

Activity=Sc0.Activity
print("Activity=",Activity)

##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
if DFG == "Test":  # 1
    EventLog_DFG = True
    otherEntities_DFG = True
    otherEntitiesRel_DFG = True
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = True
    octNode_DFG = True
    octRel_DFG = True

    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = True
    DK4_DFG = True
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = True

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG1":  # 1
    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False

    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG1_Domain":  # 2
    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False

    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG1_DomainConcept":  # 3


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG1_DomainConceptLevel":  # 4


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False


if DFG == "DFG1_featureValue":  # 6

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG1_featureValue_Domain":  # 7

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG1_featureValue_DomainConcept":  # 8

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG1_featureValue_DomainConceptLevel":  # 9

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG2":  # 10

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG2_Domain":  # 11


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG2_DomainConcept":  # 12

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG2_DomainConceptLevel":  # 13


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG2_featureValue":  # 14


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG2_featureValue_Domain":  # 15


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG2_featureValue_DomainConcept":  # 16


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG2_featureValue_DomainConceptLevel":  # 17

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3":  # 18


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_Domain":  # 19

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_DomainConcept":  # 20

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_DomainConceptLevel":  # 21

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_feature":  # 22

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_feature_Domain":  # 23

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_feature_DomainConcept":  # 24

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_feature_DomainConceptLevel":  # 25

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_featureValue":  # 26


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_featureValue_Domain":  # 27

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_featureValue_DomainConcept":  # 28


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG3_featureValue_DomainConceptLevel":  # 29
    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = True
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4":  # 30

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_Domain":  # 31

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_DomainConcept":  # 32

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_DomainConceptLevel":  # 33

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_feature":  # 34


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_feature_Domain":  # 35


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_feature_DomainConcept":  # 36


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_feature_DomainConceptLevel":  # 37


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_featureValue":  # 38
    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_featureValue_Domain":  # 39

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_featureValue_DomainConcept":  # 40



    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG4_featureValue_DomainConceptLevel":  # 41


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = True
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5":  # 42


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_Domain":  # 43


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_DomainConcept":  # 44


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_DomainConceptLevel":  # 45

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = False
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_feature":  # 46

    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_feature_Domain":  # 47



    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_feature_DomainConcept":  # 48



    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_feature_DomainConceptLevel":  # 49


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_featureValue":  # 50



    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_featureValue_Domain":  # 51



    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Domain"]
    #domainColTitle = ["Name"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_featureValue_DomainConcept":  # 52


    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False

if DFG == "DFG5_featureValue_DomainConceptLevel":  # 53




    EventLog_DFG = True
    otherEntities_DFG = False
    otherEntitiesRel_DFG = False
    acProperties_DFG = True
    Domain_DFG = True
    ICD_DFG = False
    octNode_DFG = True
    octRel_DFG = True


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = True
    DK6_1_DFG = True
    DK6_2_DFG = True
    DK7_DFG = False

    #DomainNode = ["Concept"]
    #domainColTitle = ["termA"]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = True
    step_aggregateDF_All = False
    step_aggregateEntity = False
    step_aggregateDFtwoEntity_p1 = False
    step_aggregateDFtwoEntity_p2 = False


if DFG == "DFG6":  # 54
    EventLog_DFG = True
    otherEntities_DFG = True
    otherEntitiesRel_DFG = True
    acProperties_DFG = False
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = True
    step_aggregateDFtwoEntity_p1 = True
    step_aggregateDFtwoEntity_p2 = True



if DFG == "DFG6_Morbid":  # 56
    EventLog_DFG = False
    otherEntities_DFG = True
    otherEntitiesRel_DFG = True
    acProperties_DFG = False
    Domain_DFG = False
    ICD_DFG = False
    octNode_DFG = False
    octRel_DFG = False


    DK1_DFG = False
    DK2_DFG = False
    DK3_DFG = False
    DK4_DFG = False
    DK5_DFG = False
    DK6_1_DFG = False
    DK6_2_DFG = False
    DK7_DFG = False

    #DomainNode = [" "]
    #domainColTitle = [" "]

    step_aggregateDF_Absolute = False
    step_aggregateDF_Relative = False
    step_aggregateDF_All = False
    step_aggregateEntity = True
    step_aggregateDFtwoEntity_p1 = True
    step_aggregateDFtwoEntity_p2 = True



##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

if myInput == "main_Entities" :
    EventLog_Input = True
    otherEntities_Input = False
    otherEntitiesRel_Input = False
    acProperties_Input = False
    Domain_Input = False
    ICD_Input = False
    octNode_Input = False
    octRel_Input = False


    DK1_input = False
    DK2_input = False
    DK3_input = False
    DK4_input = False
    DK5_input = False
    DK6_1_input = False
    DK6_2_input = False
    DK7_input = False

    #entityList = ["Patient", "Admission"]
    #entityListIDproperty = ["ID", "ID"]
    #conditionProperty = ["Category", "Category"]
    #conditionPropertyValue = ["Absolute", "Absolute"]






#2
if myInput == "main_Entities_plus_Disorder" :
    EventLog_Input = True
    otherEntities_Input = True
    otherEntitiesRel_Input = True
    acProperties_Input = False
    Domain_Input = False
    ICD_Input = True
    octNode_Input = False
    octRel_Input = False


    DK1_input = False
    DK2_input = False
    DK3_input = False
    DK4_input = False
    DK5_input = False
    DK6_1_input = False
    DK6_2_input = False
    DK7_input = True

    #entityList = ["Patient", "Admission", "Disorder"]
    #entityListIDproperty = ["ID", "ID", "ID"]
    #conditionProperty = ["Category", "Category", "Category"]
    #conditionPropertyValue = ["Absolute", "Absolute", "Absolute"]


#3
if myInput == "main_Entities_plus_ICD" :
    EventLog_Input = True
    otherEntities_Input = True
    otherEntitiesRel_Input = True
    acProperties_Input = False
    Domain_Input = False
    ICD_Input = True
    octNode_Input = False
    octRel_Input = False


    DK1_input = False
    DK2_input = False
    DK3_input = True
    DK4_input = False
    DK5_input = False
    DK6_1_input = False
    DK6_2_input = False
    DK7_input = True

    #entityList = ["Patient", "Admission", "Clinical"]
    #entityListIDproperty = ["ID", "ID", "ID"]
    #conditionProperty = ["Category", "Category", "Category"]
    #conditionPropertyValue = ["Absolute", "Absolute", "Absolute"]



#4
if myInput == "main_Entities_plus_ICD_level_doesnt_work" :
    EventLog_Input = True
    otherEntities_Input = True
    otherEntitiesRel_Input = True
    acProperties_Input = False
    Domain_Input = False
    ICD_Input = True
    octNode_Input = False
    octRel_Input = False


    DK1_input = False
    DK2_input = False
    DK3_input = True
    DK4_input = False
    DK5_input = False
    DK6_1_input = False
    DK6_2_input = False
    DK7_input = True

    #entityList = ["Patient", "Admission", "Clinical"]
    #entityListIDproperty = ["ID", "ID", "ID"]
    #conditionProperty = ["Category", "Category", "Category"]
    #conditionPropertyValue = ["Absolute", "Absolute", "Absolute"]

#5
if myInput == "main_Entities_plus_SCT" :
    EventLog_Input = True
    otherEntities_Input = True
    otherEntitiesRel_Input = True
    acProperties_Input = False
    Domain_Input = False
    ICD_Input = True
    octNode_Input = True
    octRel_Input = True


    DK1_input = False
    DK2_input = False
    DK3_input = True
    DK4_input = True
    DK5_input = False
    DK6_1_input = False
    DK6_2_input = False
    DK7_input = True

    #entityList = ["Patient", "Admission", "Concept"]
    #entityListIDproperty = ["ID", "ID", "ID"]
    #conditionProperty = ["Category", "Category", "Category"]
    #conditionPropertyValue = ["Absolute", "Absolute", "Absolute"]

#6
if myInput == "main_Entities_plus_SCT_level":
    EventLog_Input = True
    otherEntities_Input = True
    otherEntitiesRel_Input = True
    acProperties_Input = False
    Domain_Input = False
    ICD_Input = True
    octNode_Input = True
    octRel_Input = True


    DK1_input = False
    DK2_input = False
    DK3_input = True
    DK4_input = True
    DK5_input = False
    DK6_1_input = False
    DK6_2_input = False
    DK7_input = True

    #entityList = ["Patient", "Admission", "Concept"]
    #entityListIDproperty = ["ID", "ID", "ID"]
    #conditionProperty = ["Category", "Category", "Category"]
    #conditionPropertyValue = ["Absolute", "Absolute", "Absolute"]


#7
if myInput == "main_Entities_plus_SCT_Level_One":
    EventLog_Input = True
    otherEntities_Input = True
    otherEntitiesRel_Input = True
    acProperties_Input = False
    Domain_Input = False
    ICD_Input = True
    octNode_Input = True
    octRel_Input = True


    DK1_input = False
    DK2_input = False
    DK3_input = True
    DK4_input = True
    DK5_input = False
    DK6_1_input = False
    DK6_2_input = False
    DK7_input = True

    #entityList = ["Patient", "Admission", "Concept"]
    #entityListIDproperty = ["ID", "ID", "ID"]
    #conditionProperty = ["Category", "Category", "Category"]
    #conditionPropertyValue = ["Absolute", "Absolute", "Absolute"]



#8
if myInput == "main_Entities_plus_ICD_one":
    EventLog_Input = True
    otherEntities_Input = True
    otherEntitiesRel_Input = True
    acProperties_Input = False
    Domain_Input = False
    ICD_Input = True
    octNode_Input = False
    octRel_Input = False


    DK1_input = False
    DK2_input = False
    DK3_input = True
    DK4_input = False
    DK5_input = False
    DK6_1_input = False
    DK6_2_input = False
    DK7_input = True

    #entityList = ["Patient", "Admission", "Clinical"]
    #entityListIDproperty = ["ID", "ID", "ID"]
    #conditionProperty = ["Category", "Category", "Category"]
    #conditionPropertyValue = ["Absolute", "Absolute", "Absolute"]





#9
if myInput == "main_Entities_plus_SCT_one":
    EventLog_Input = True
    otherEntities_Input = True
    otherEntitiesRel_Input = True
    acProperties_Input = False
    Domain_Input = False
    ICD_Input = True
    octNode_Input = True
    octRel_Input = True


    DK1_input = False
    DK2_input = False
    DK3_input = True
    DK4_input = True
    DK5_input = False
    DK6_1_input = False
    DK6_2_input = False
    DK7_input = True

    #entityList = ["Patient", "Admission", "Concept"]
    #entityListIDproperty = ["ID", "ID", "ID"]
    #conditionProperty = ["Category", "Category", "Category"]
    #conditionPropertyValue = ["Absolute", "Absolute", "Absolute"]






##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

if Activity == "Activity_Label" :
    EventLog_activity = True
    otherEntities_activity = False
    otherEntitiesRel_activity = False
    acProperties_activity = False
    Domain_activity = False
    ICD_activity = False
    octNode_activity = False
    octRel_activity = False


    DK1_activity  = False
    DK2_activity  = False
    DK3_activity  = False
    DK4_activity  = False
    DK5_activity  = False
    DK6_1_activity  = False
    DK6_2_activity  = False
    DK7_activity  = False

    #ActivityNode = ["Activity"]
    #colTitle = "Syn"

if Activity == "Concept_Label" :
    EventLog_activity = True
    otherEntities_activity = False
    otherEntitiesRel_activity = False
    acProperties_activity = False
    Domain_activity = False
    ICD_activity = False
    octNode_activity = True
    octRel_activity = True


    DK1_activity  = False
    DK2_activity  = False
    DK3_activity  = False
    DK4_activity  = False
    DK5_activity  = True
    DK6_1_activity  = False
    DK6_2_activity  = False
    DK7_activity  = False

    #ActivityNode = ["Concept"]
    #colTitle = "termA"

if Activity == "Concept_Label_Level" :
    EventLog_activity = True
    otherEntities_activity = False
    otherEntitiesRel_activity = False
    acProperties_activity = False
    Domain_activity = False
    ICD_activity = False
    octNode_activity = True
    octRel_activity = True


    DK1_activity  = False
    DK2_activity  = False
    DK3_activity  = False
    DK4_activity  = False
    DK5_activity  = True
    DK6_1_activity  = False
    DK6_2_activity  = False
    DK7_activity  = False

    #ActivityNode = ["Concept"]
    #colTitle = "termA"



##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################



EventLog = EventLog_DFG or EventLog_Input or EventLog_activity
otherEntities = otherEntities_DFG or otherEntities_Input or otherEntities_activity
otherEntitiesRel = otherEntitiesRel_DFG or otherEntitiesRel_Input or otherEntitiesRel_activity
acProperties = acProperties_DFG or acProperties_Input or acProperties_activity
Domain = Domain_DFG or Domain_Input or Domain_activity
ICD = ICD_DFG or ICD_Input or ICD_activity
octNode = octNode_DFG or octNode_Input or octNode_activity
octRel = octRel_DFG or octRel_Input or octRel_activity



DK1 = DK1_activity or DK1_DFG or DK1_input
DK2 = DK2_activity or DK2_DFG or DK2_input
DK3 = DK3_activity or DK3_DFG or DK3_input
DK4 = DK4_activity or DK4_DFG or DK4_input
DK5 = DK5_activity or DK5_DFG or DK5_input
DK6_1 = DK6_1_activity or DK6_1_DFG or DK6_1_input
DK6_2 = DK6_2_activity or DK6_2_DFG or DK6_2_input
DK7 = DK7_activity or DK7_DFG or DK7_input

print(" ")
print("EventLog=", EventLog)
print("otherEntities=", otherEntities)
print("otherEntitiesRel=", otherEntitiesRel)
print("acProperties=", acProperties)
print("Domain=", Domain)
print("ICD=", ICD)
print("octNode=", octNode)
print("octRel=", octRel)


print("DK1=", DK1)
print("DK2=", DK2)
print("DK3=", DK3)
print("DK4=", DK4)
print("DK5=", DK5)
print("DK6_1=", DK6_1)
print("DK6_2=", DK6_2)
print("DK7=", DK7)






print(" ")
print("Output for Q:")
print("step_aggregateDF_All=", step_aggregateDF_All)
print("step_aggregateDF_Absolute=", step_aggregateDF_Absolute)
print("step_aggregateDF_Relative=", step_aggregateDF_Relative)
print("step_aggregateEntity=", step_aggregateEntity)
print("step_aggregateDFtwoEntity_p1=", step_aggregateDFtwoEntity_p1)
print("step_aggregateDFtwoEntity_p2=", step_aggregateDFtwoEntity_p2)


# 555555555555555555555555555555555555555555555555555555555555555555555555555
# 555555555555555555555555555555555555555555555555555555555555555555555555555
# 555555555555555555555555555555555555555555555555555555555555555555555555555
# 555555555555555555555555555555555555555555555555555555555555555555555555555
# 555555555555555555555555555555555555555555555555555555555555555555555555555


goalList=[]
sheetTitleshelper=[]
pageNext=[]
pageNextName=[]
pageNextName2=[]
pageNextName3=[]


if EventLog==True:
    goalList.append('eventLogDiv')
    sheetTitleshelper.append('ED_Event_FileName')
    pageNext.append("1")
    pageNextName.append("eventLogName")
    pageNextName2.append("eventLogNeo4jName")
    scripts = [
        'A3_EntryCol_Step2_logConf_Step.py',
        'A5_EntryCol_Step3_Step.py',
        'A6_Scenario_Final_Step.py',
        'C04_Step2_Log_importingNeo4J1.py',
    ]
    pageNextName3.append(scripts)

if otherEntities==True:
    goalList.append('otherEntitiesDiv')
    sheetTitleshelper.append('EnP_PoNode_FileName_1')
    pageNext.append("2")
    pageNextName.append("otherEntitiesName")
    pageNextName2.append("otherEntitiesNeo4jName")
    scripts = [
        'D04_Step2_otherEntities_importingNeo4J1.py'
    ]
    pageNextName3.append(scripts)

if otherEntitiesRel==True:
    goalList.append('otherEntitiesRelDiv')
    sheetTitleshelper.append('EnP_PoNode_FileName_2')
    pageNext.append("3")
    pageNextName.append("entityRelName")
    pageNextName2.append("entityRelNeo4jName")
    scripts = [
        'D08_Step2_enRel_importingNeo4J1.py',
        'D12_Step2_enRel_importingNeo4J1.py'
    ]
    pageNextName3.append(scripts)

if acProperties==True:
    goalList.append('activitiesValueDiv')
    sheetTitleshelper.append('AcP_PoNode_FileName')
    pageNext.append("4")
    pageNextName.append("activityPropertiesName")
    pageNextName2.append("activityPropertiesNeo4jName")
    scripts = [
        'E04_Step2_acProperty_importingNeo4J1.py'
    ]
    pageNextName3.append(scripts)

if Domain==True:
    goalList.append('domainDiv')
    sheetTitleshelper.append('ACT_PoNode_FileName')
    pageNext.append("5")
    pageNextName.append("DomainName")
    pageNextName2.append("DomainNeo4jName")
    scripts = [
        'F04_Step14_Domain_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if ICD==True:
    goalList.append('iCDDiv')
    sheetTitleshelper.append('CE_PoNode_FileName')
    pageNext.append("6")
    pageNextName.append("ICDName")
    pageNextName2.append("ICDNeo4jName")
    scripts = [
        'H04_Step18_ClinicalEntity_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if octNode==True:
    goalList.append('snomedCtRelNodeDiv')
    sheetTitleshelper.append('OCT_OCT_Node_FileName')
    pageNext.append("7")
    pageNextName.append("SctNodeName")
    pageNextName2.append("SctNodeNeo4jName")
    scripts = [
        'I04_Step20_OCT_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if octRel==True:
    goalList.append('snomedCtRelDiv')
    sheetTitleshelper.append('OCT_OCT_REL_FileName')
    pageNext.append("8")
    pageNextName.append("SctRelName")
    pageNextName2.append("SctRelNeo4jName")
    scripts = [
        'I08_Step20_OCTrel_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if DK1==True:
    goalList.append('dk1Div')
    sheetTitleshelper.append('DK1_EnPo_FileName')
    pageNext.append("9")
    pageNextName.append("DK1Name")
    pageNextName2.append("DK1Neo4jName")
    scripts = [
        'J04_Step22_DK1_X_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if DK2==True:
    goalList.append('dk2Div')
    sheetTitleshelper.append('DK2_EnPo_FileName')
    pageNext.append("10")
    pageNextName.append("DK2Name")
    pageNextName2.append("DK2Neo4jName")
    scripts = [
        'K04_Step24_DK2_X_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if DK3==True:
    goalList.append('dk3Div')
    sheetTitleshelper.append('DK3_Potential_DK3_FileName')
    pageNext.append("11")
    pageNextName.append("DK3Name")
    pageNextName2.append("DK3Neo4jName")
    scripts = [
        'L04_Step26_DK3_Linker_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if DK4==True:
    goalList.append('dk4Div')
    sheetTitleshelper.append('DK4_ICD_OCT_FileName')
    pageNext.append("12")
    pageNextName.append("DK4Name")
    pageNextName2.append("DK4Neo4jName")
    scripts = [
        'M04_Step28_DK4_Connector_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if DK5==True:
    goalList.append('dk5Div')
    sheetTitleshelper.append('DK5_FileName')
    pageNext.append("13")
    pageNextName.append("DK5Name")
    pageNextName2.append("DK5Neo4jName")
    scripts = [
        'N04_Step30_DK5_Mapper_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if DK6_1==True:
    goalList.append('dk61Div')
    sheetTitleshelper.append('Domain_FileName_1')
    pageNext.append("14")
    pageNextName.append("DK61Name")
    pageNextName2.append("DK6Neo4jName")
    scripts = [
        'O04_Step32_DK6_Tied_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)

if DK6_2==True:
    goalList.append('dk62Div')
    sheetTitleshelper.append('Domain_FileName_2')
    pageNext.append("15")
    pageNextName.append("DK62Name")
    pageNextName2.append("DK62Neo4jName")
    scripts = [
        'ZZZZZ.py'
    ]
    pageNextName3.append(scripts)

if DK7==True:
    goalList.append('dk7Div')
    sheetTitleshelper.append('DK7_Activity_DK7_FileName')
    pageNext.append("16")
    pageNextName.append("DK7Name")
    pageNextName2.append("DK7Neo4jName")
    scripts = [
        'P04_Step34_DK7_Bond_importingNeo4J.py'
    ]
    pageNextName3.append(scripts)


print("goalList=", goalList)
print("sheetTitleshelper=", sheetTitleshelper)
print("pageNext=", pageNext)
print("pageNextName=", pageNextName)
print("pageNextName2=", pageNextName2)
print("pageNextName3=", pageNextName3)
pageNextHelper=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
print("pageNextHelper=", pageNextHelper)

import os
confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)
inputTex_FilePath2 = confPath + "/" + "3_previewNumberOfQuestions.txt"
with open(inputTex_FilePath2, 'w') as file:
    file.write(f'''{goalList}''')

print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS\n")
print("pageNext=", pageNext)
print("pageNextHelper=", pageNextHelper)
print("pageNextName=", pageNextName)


confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)
savingPageSequence = confPath + "/" + "3_pageSequence.txt"
pageNextFinal1=Func.pageSequence(pageNext,pageNextHelper,pageNextName,"convertingNeo4jName",savingPageSequence)
print("pageNextFinal1=", pageNextFinal1)


print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS\n")
print("pageNext=", pageNext)
print("pageNextHelper=", pageNextHelper)
print("pageNextName2=", pageNextName2)

savingPageSequence = confPath + "/" + "3_pageSequencePart2.txt"
pageNextFinal2=Func.pageSequence2(pageNext,pageNextHelper,pageNextName2,"queryLister",savingPageSequence)
print("pageNextFinal2=", pageNextFinal2)



print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS\n")
print("pageNext=", pageNext)
print("pageNextHelper=", pageNextHelper)
print("pageNextName3=", pageNextName3)

savingPageSequence = confPath + "/" + "3_pageSequencePart3.txt"
pageNextFinal2=Func.pageSequence3(pageNext,pageNextHelper,pageNextName3,['Q04_Step2_DFG_importingNeo4J_Scneario.py'],savingPageSequence)
print("pageNextFinal2=", pageNextFinal2)


