import subprocess
import A1_Scenario_Step2 as sc1
import A1_Scenario_Step3 as sc2
##################################################################################


subprocess.run(['python', 'A0_configuration.py'])

subprocess.run(['python', 'A1_Scenario_Step1_Selecting_Test.py'])

subprocess.run(['python', 'A1_Scenario_Step2.py'])

subprocess.run(['python', 'A1_Scenario_Step3.py'])

subprocess.run(['python', 'A2_FileLocation_Step1_Address_Test_Func.py'])

subprocess.run(['python', 'A2_FileLocation_Step2_xlsx_Step.py'])

subprocess.run(['python', 'A2_FileLocation_Step3_sheetName_Step.py'])
subprocess.run(['python', 'A2_FileLocation_Step4_Test_Step.py'])
subprocess.run(['python', 'A2_FileLocation_Step5_csv_Step.py'])


subprocess.run(['python', 'A3_EntryCol_Step1_Test_Step.py'])

subprocess.run(['python', 'A3_EntryCol_Step2_logConf_Step.py'])

subprocess.run(['python', 'A5_EntryCol_Step3_Step.py'])

subprocess.run(['python', 'A6_Scenario_Final_Step.py'])


##################################################################################


EventLog=sc2.EventLog
otherEntities=sc2.otherEntities
otherEntitiesRel=sc2.otherEntitiesRel
acProperties=sc2.acProperties
Domain=sc2.Domain
ICD=sc2.ICD
octNode=sc2.octNode
octRel=sc2.octRel

DK1=sc2.DK1
DK2=sc2.DK2
DK3=sc2.DK3
DK4=sc2.DK4
DK5=sc2.DK5
DK6_1=sc2.DK6_1
DK6_2=sc2.DK6_2
DK7=sc2.DK7


if EventLog==True:
    subprocess.run(['python', 'C04_Step2_Log_importingNeo4J1.py'])


if otherEntities==True :

    subprocess.run(['python', 'D04_Step2_otherEntities_importingNeo4J1.py'])

if otherEntitiesRel==True:

    subprocess.run(['python', 'D08_Step2_enRel_importingNeo4J1.py'])
    subprocess.run(['python', 'D12_Step2_enRel_importingNeo4J1.py'])

if acProperties:

    subprocess.run(['python', 'E04_Step2_acProperty_importingNeo4J1.py'])

if Domain:

    subprocess.run(['python', 'F04_Step14_Domain_importingNeo4J.py'])


if ICD:

    subprocess.run(['python', 'H04_Step18_ClinicalEntity_importingNeo4J.py'])

if octNode==True :
    subprocess.run(['python', 'I04_Step20_OCT_importingNeo4J.py'])


if octRel==True:
    subprocess.run(['python', 'I08_Step20_OCTrel_importingNeo4J.py'])

if DK1:

    subprocess.run(['python', 'J04_Step22_DK1_X_importingNeo4J.py'])

if DK2:

    subprocess.run(['python', 'K04_Step24_DK2_X_importingNeo4J.py'])


if DK3:

    subprocess.run(['python', 'L04_Step26_DK3_Linker_importingNeo4J.py'])

if DK4:

    subprocess.run(['python', 'M04_Step28_DK4_Connector_importingNeo4J.py'])

if DK5:

    subprocess.run(['python', 'N04_Step30_DK5_Mapper_importingNeo4J.py'])

if DK6_1==True and DK6_2==True:
    subprocess.run(['python', 'O04_Step32_DK6_Tied_importingNeo4J.py'])


if DK7:
    subprocess.run(['python', 'P04_Step34_DK7_Bond_importingNeo4J.py'])

##################################################################################


subprocess.run(['python', 'Q04_Step2_DFG_importingNeo4J_Scneario.py'])

##################################################################################

DFG=sc1.DFG
print("DFG=",DFG)

if DFG == "Test":  # 0
    subprocess.run(['python', 'S03_Step_DFG1_1.py'])

if DFG == "DFG1":  # 1
    subprocess.run(['python', 'S03_Step_DFG1_1.py'])

if DFG == "DFG1_Domain":  # 2
    subprocess.run(['python', 'S10_Step_DFG1_Domain_2.py'])

if DFG == "DFG1_DomainConcept":  # 3
    subprocess.run(['python', 'S17_Step_DFG1_DomainConcept_3.py'])

if DFG == "DFG1_DomainConceptLevel":  # 4
    subprocess.run(['python', 'S24_Step_DFG1_DomainConceptLevel_4.py'])

if DFG == "DFG1_featureValue":  # 6
    subprocess.run(['python', 'S31_Step_DFG1_featureValue_5.py'])

if DFG == "DFG1_featureValue_Domain":  # 7
    subprocess.run(['python', 'S38_Step_DFG1_featureValue_Domain_6.py'])

if DFG == "DFG1_featureValue_DomainConcept":  # 8
    subprocess.run(['python', 'S45_Step_DFG1_featureValue_DomainConcept_7.py'])

if DFG == "DFG1_featureValue_DomainConceptLevel":  # 9
    subprocess.run(['python', 'S52_Step_DFG1_featureValue_DomainConceptLevel_8.py'])

if DFG == "DFG2":  # 10
    subprocess.run(['python', 'T03_Step_DFG2_9.py'])

if DFG == "DFG2_Domain":  # 11
    subprocess.run(['python', 'T10_Step_DFG2_Domain_10.py'])

if DFG == "DFG2_DomainConcept":  # 12
    subprocess.run(['python', 'T17_Step_DFG2_DomainConcept_11.py'])

if DFG == "DFG2_DomainConceptLevel":  # 13
    subprocess.run(['python', 'T24_Step_DFG2_DomainConceptLevel_12.py'])
if DFG == "DFG2_featureValue":  # 14
    subprocess.run(['python', 'T31_Step_DFG2_featureValue_13.py'])

if DFG == "DFG2_featureValue_Domain":  # 15
    subprocess.run(['python', 'T38_Step_DFG2_featureValue_Domain_14.py'])

if DFG == "DFG2_featureValue_DomainConcept":  # 16
    subprocess.run(['python', 'T45_Step_DFG2_featureValue_DomainConcept_15.py'])

if DFG == "DFG2_featureValue_DomainConceptLevel":  # 17
    subprocess.run(['python', 'T52_Step_DFG2_featureValue_DomainConceptLevel_16.py'])

if DFG == "DFG3":  # 18
    subprocess.run(['python', 'U03_Step_DFG3_All_17.py'])

if DFG == "DFG3_Domain":  # 19
    subprocess.run(['python', 'U10_Step_DFG3_Domain_All_18.py'])

if DFG == "DFG3_DomainConcept":  # 20
    subprocess.run(['python', 'U17_Step_DFG3_DomainConcept_All_19.py'])

if DFG == "DFG3_DomainConceptLevel":  # 21
    subprocess.run(['python', 'U24_Step_DFG3_DomainConceptLevel_All_20.py'])

if DFG == "DFG3_feature":  # 22
    subprocess.run(['python', 'U31_Step_DFG3_feature_All_21.py'])

if DFG == "DFG3_feature_Domain":  # 23
    subprocess.run(['python', 'U38_Step_DFG3_feature_Domain_All_22.py'])

if DFG == "DFG3_feature_DomainConcept":  # 24
    subprocess.run(['python', 'U45_Step_DFG3_feature_DomainConcept_All_23.py'])

if DFG == "DFG3_feature_DomainConceptLevel":  # 25
    subprocess.run(['python', 'U52_Step_DFG3_feature_DomainConceptLevel_All_24.py'])

if DFG == "DFG3_featureValue":  # 26
    subprocess.run(['python', 'U59_Step_DFG3_featureValue_All_25.py'])

if DFG == "DFG3_featureValue_Domain":  # 27
    subprocess.run(['python', 'U66_Step_DFG3_featureValue_Domain_All_26.py'])

if DFG == "DFG3_featureValue_DomainConcept":  # 28
    subprocess.run(['python', 'U73_Step_DFG3_featureValue_DomainConcept_All_27.py'])

if DFG == "DFG3_featureValue_DomainConceptLevel":  # 29
    subprocess.run(['python', 'U80_Step_DFG3_featureValue_DomainConceptLevel_All_28.py'])

if DFG == "DFG4":  # 30
    subprocess.run(['python', 'V03_Step_DFG4_Absolute_29.py'])

if DFG == "DFG4_Domain":  # 31
    subprocess.run(['python', 'V10_Step_DFG4_Domain_Absolute_30.py'])

if DFG == "DFG4_DomainConcept":  # 32
    subprocess.run(['python', 'V17_Step_DFG4_DomainConcept_Absolute_31.py'])

if DFG == "DFG4_DomainConceptLevel":  # 33
    subprocess.run(['python', 'V24_Step_DFG4_DomainConceptLevel_Absolute_32.py'])

if DFG == "DFG4_feature":  # 34
    subprocess.run(['python', 'V31_Step_DFG4_feature_Absolute_33.py'])

if DFG == "DFG4_feature_Domain":  # 35
    subprocess.run(['python', 'V38_Step_DFG4_feature_Domain_Absolute_34.py'])

if DFG == "DFG4_feature_DomainConcept":  # 36
    subprocess.run(['python', 'V45_Step_DFG4_feature_DomainConcept_Absolute_35.py'])

if DFG == "DFG4_feature_DomainConceptLevel":  # 37
    subprocess.run(['python', 'V52_Step_DFG4_feature_DomainConceptLevel_Absolute_36.py'])

if DFG == "DFG4_featureValue":  # 38
    subprocess.run(['python', 'V59_Step_DFG4_featureValue_Absolute_37.py'])

if DFG == "DFG4_featureValue_Domain":  # 39
    subprocess.run(['python', 'V66_Step_DFG4_featureValue_Domain_Absolute_38.py'])

if DFG == "DFG4_featureValue_DomainConcept":  # 40
    subprocess.run(['python', 'V73_Step_DFG4_featureValue_DomainConcept_Absolute_39.py'])

if DFG == "DFG4_featureValue_DomainConceptLevel":  # 41
    subprocess.run(['python', 'V80_Step_DFG4_featureValue_DomainConceptLevel_Absolute_40.py'])

if DFG == "DFG5":  # 42
    subprocess.run(['python', 'W03_Step_DFG5_Relative_41.py'])

if DFG == "DFG5_Domain":  # 43
    subprocess.run(['python', 'W10_Step_DFG5_Domain_Relative_42.py'])

if DFG == "DFG5_DomainConcept":  # 44
    subprocess.run(['python', 'W17_Step_DFG5_DomainConcept_Relative_43.py'])

if DFG == "DFG5_DomainConceptLevel":  # 45
    subprocess.run(['python', 'W24_Step_DFG5_DomainConceptLevel_Relative_44.py'])

if DFG == "DFG5_feature":  # 46
    subprocess.run(['python', 'W31_Step_DFG5_feature_Relative_45.py'])

if DFG == "DFG5_feature_Domain":  # 47
    subprocess.run(['python', 'W38_Step_DFG5_feature_Domain_Relative_46.py'])

if DFG == "DFG5_feature_DomainConcept":  # 48
    subprocess.run(['python', 'W45_Step_DFG5_feature_DomainConcept_Relative_47.py'])

if DFG == "DFG5_feature_DomainConceptLevel":  # 49
    subprocess.run(['python', 'W52_Step_DFG5_feature_DomainConceptLevel_Relative_48.py'])

if DFG == "DFG5_featureValue":  # 50
    subprocess.run(['python', 'W59_Step_DFG5_featureValue_Relative_49.py'])

if DFG == "DFG5_featureValue_Domain":  # 51
    subprocess.run(['python', 'W66_Step_DFG5_featureValue_Domain_Relative_50.py'])

if DFG == "DFG5_featureValue_DomainConcept":  # 52
    subprocess.run(['python', 'W73_Step_DFG5_featureValue_DomainConcept_Relative_51.py'])

if DFG == "DFG5_featureValue_DomainConceptLevel":  # 53
    subprocess.run(['python', 'W80_Step_DFG5_featureValue_DomainConceptLevel_Relative_52.py'])

if DFG == "DFG6":  # 54
    subprocess.run(['python', 'X03_Step_DFG6_53.py'])

if DFG == "DFG6_Morbid":  # 56
    subprocess.run(['python', 'X10_Step_DFG6_Morbid_54.py'])


