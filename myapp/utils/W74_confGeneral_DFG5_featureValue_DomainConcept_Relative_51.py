
import A6_Scenario_Final_Step as Ne0
import A6_Scenario_Final_Step as Ne02

import B02_txt_write as txtW





print("********************************* Create the file **************************************************")
DFG=Ne0.DFG


DFG_FilePath=txtW.createEmptyGeneralFile(DFG)
print("DFG_FilePath=", DFG_FilePath)

print("********************************* Part1 **************************************************")

entityList=Ne02.entityList
print("entityList=", entityList)

EnNum=len(Ne02.entityList)
print("EnNum=", EnNum)

Type5_Rel_1_DF_Show, Type5_Rel_2_DF_Show=txtW.writeEntityDFShowType5(DFG_FilePath, EnNum, entityList,5)
print("Type5_Rel_1_DF_Show=", Type5_Rel_1_DF_Show)
print("Type5_Rel_2_DF_Show=", Type5_Rel_2_DF_Show)


print("********************************* Part2 **************************************************")

txtW.writeCount(DFG_FilePath,5)

print("********************************* Part3 **************************************************")


Type_selection1=txtW.writeIDSelectionNonRelativT5(DFG_FilePath, 5,1)
print("Type_selection=", Type_selection1)

Type=txtW.writeIDSelectionTypeFeature(Type_selection1, DFG_FilePath, 5)
print("Type5_approach=", Type)

txtW.writeIDSelectionInstancefeatureType5(Type,entityList,Type_selection1,DFG_FilePath,Type5_Rel_1_DF_Show,5)

print("********************************* Part4 **************************************************")


Type_selection2=txtW.writeIDSelectionNonRelativT5(DFG_FilePath, 5,2)
print("Type_selection2=", Type_selection2)



txtW.writeIDSelectionInstanceType5(Type_selection2,entityList,Type_selection2,DFG_FilePath,5,2)


print("********************************* write in Q **************************************************")

txtW.writeInQTyep5("DFG5_config",Type5_Rel_1_DF_Show,Type5_Rel_2_DF_Show)

print("********************************* Part5 **************************************************")


Type_Domain_selection=txtW.writeDomainIDSelection(DFG_FilePath, 5)
print("Type1_Domain_selection=", Type_Domain_selection)

DomainNode = Ne02.DomainNode
domainColTitle = Ne02.domainColTitle[0]

txtW.writeIDDomainSelectionInstance(Type_Domain_selection,DFG_FilePath,DomainNode[0],domainColTitle,5)




print("********************************* Execution **************************************************")


import subprocess

subprocess.run(['python', 'Q02_Step1_DFG_prepare_Scenario.py'])

subprocess.run(['python', 'Q04_Step2_DFG_importingNeo4J_Scneario.py'])

subprocess.run(['python', 'W73_Step_DFG5_featureValue_DomainConcept_Relative_51.py'])

'''
print("********************************* Example **************************************************")


Example:

Type5_Count = 0

#if DFG5
Type5_Rel_1_DF_Show = "Patient"  #Q02
Type5_Rel_2_DF_Show = "Concept" #Q02

Type5_Rel_1_DF_Show_selection = True # True if we wamt to select specific ID, False if we wamt to show all the table
Type5_approach=2


Type5_approach=0
    Type5_Rel_1_DF_Show_selection_ID_instances = []
    Type5_Rel_1_DF_Show_selection_feature_Name = []
    Type5_Rel_1_DF_Show_selection_feature_label = []
    Type5_Rel_1_DF_Show_selection_feature_Value = []

Type5_approach=1
    Type5_Rel_1_DF_Show_selection_ID_instances = ["2"]
    Type5_Rel_1_DF_Show_selection_feature_Name = []
    Type5_Rel_1_DF_Show_selection_feature_label = []
    Type5_Rel_1_DF_Show_selection_feature_Value = []

Type5_approach=2
    Type5_Rel_1_DF_Show_selection_ID_instances = [] then with a query we find ['2']
    Type5_Rel_1_DF_Show_selection_feature_Name = ["ABG_Test"]
    Type5_Rel_1_DF_Show_selection_feature_label = ["Label1", "Label2", "Label3", "Label4", "Label5", "Label6", "Label7"]
    Type5_Rel_1_DF_Show_selection_feature_Value = ["Value1.3", "Value2.1", "Value3.4", "Value4.3",  "Value5.4", "Value6.4", "Value7.4"]



Type5_Rel_2_DF_Show_selection = False #Q02  # True if we wamt to select specific ID, False if we wamt to show all the table
Type5_Rel_2_DF_Show_selection_ID_instances = ["1"] #Q02 # Works if True # also [47,50]


Type4_Domain_selection = False/True
Type4_Domain_ID = ["Transfer",...] or ["snomedTermA",..] or []

'''