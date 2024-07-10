
import A6_Scenario_Final_Step as Ne0
import A6_Scenario_Final_Step as Ne02

import B02_txt_write as txtW



print("********************************* Create the file **************************************************")
DFG = Ne0.DFG

DFG_FilePath = txtW.createEmptyGeneralFile(DFG)
print("DFG_FilePath=", DFG_FilePath)

print("********************************* Part1 **************************************************")

entityList = Ne02.entityList
print("entityList=", entityList)

EnNum = len(Ne02.entityList)
print("EnNum=", EnNum)

TypeShow = txtW.writeEntityDFShiw(DFG_FilePath, EnNum, entityList, 3)
print("TypeShow=", TypeShow)

print("********************************* Part2 **************************************************")

txtW.writeCount(DFG_FilePath, 3)

print("********************************* Part3 **************************************************")

Type3=txtW.writeTypeNumber(DFG_FilePath, 3)
print("Type3=", Type3)

print("********************************* Part4 **************************************************")

Type3_non_Relative_selection=txtW.writeIDSelectionNonRelativeType3(Type3, DFG_FilePath, 3)
print("Type3_non_Relative_selection=", Type3_non_Relative_selection)



print("********************************* Part5 **************************************************")

Type3_non_Relative_approach=txtW.writeType3_non_Relative_approach(Type3, Type3_non_Relative_selection, DFG_FilePath, 3)
print("Type3_non_Relative_approach=", Type3_non_Relative_approach)

print("********************************* Part6 **************************************************")

Type3_non_Relative_selection_ID_instances = txtW.writeIDSelectionInstancefeatureType3Feature(Type3_non_Relative_approach, entityList,TypeShow,DFG_FilePath,3)
print("Type3_non_Relative_selection_ID_instances=", Type3_non_Relative_selection_ID_instances)



print("********************************* write in Q **************************************************")

txtW.writeInQTyep3Feature("DFG3_config",Type3,Type3_non_Relative_selection,Type3_non_Relative_selection_ID_instances)



print("********************************* Part7 **************************************************")


Type_Domain_selection=txtW.writeDomainIDSelection(DFG_FilePath, 3)
print("Type1_Domain_selection=", Type_Domain_selection)

DomainNode = Ne02.DomainNode
domainColTitle = Ne02.domainColTitle[0]

txtW.writeIDDomainSelectionInstance(Type_Domain_selection,DFG_FilePath,DomainNode[0],domainColTitle,3)


print("********************************* Execution **************************************************")


import subprocess

subprocess.run(['python', 'Q02_Step1_DFG_prepare_Scenario.py'])

subprocess.run(['python', 'Q04_Step2_DFG_importingNeo4J_Scneario.py'])

subprocess.run(['python', 'U38_Step_DFG3_feature_Domain_All_22.py'])


print("********************************* Example **************************************************")

'''
Example:

Type3_Entity1_DF_Show=1
Type3_Entity2_DF_Show=1
Type3_Entity3_DF_Show=1

Type3_Count=0

Type3 = 1 # 1=RelateveAndAbsolute  2=OnlyAbsolute (non Relative)


Type3=1   RelateveAndAbsolut

    Type3_non_Relative_selection=False#
    Type3_non_Relative_approach=0
    Type3_non_Relative_selection_ID_instances=[]
    Type3_non_Relative_selection_feature_Name=[]
    Type3_non_Relative_selection_feature_label=[]
    Type3_non_Relative_selection_feature_Value=[]


Type3=2   OnlyAbsolute
    Type3_non_Relative_selection=False#
    Type3_non_Relative_approach=0
    Type3_non_Relative_selection_ID_instances=[]
    Type3_non_Relative_selection_feature_Name=[]
    Type3_non_Relative_selection_feature_label=[]
    Type3_non_Relative_selection_feature_Value=[] 

Type3=2  OnlyAbsolute
    Type3_non_Relative_selection=True#
    Type3_non_Relative_approach=1
    Type3_non_Relative_selection_ID_instances=[["1"],["13"],["44054006"]] 
    Type3_non_Relative_selection_feature_Name=[]
    Type3_non_Relative_selection_feature_label=[]
    Type3_non_Relative_selection_feature_Value=[]


Type3=2  OnlyAbsolute
    Type3_non_Relative_selection=True#
    Type3_non_Relative_approach=2
    Type3_non_Relative_selection_ID_instances=[] 
    Type3_non_Relative_selection_feature_Name=["ABG_Test"]
    Type3_non_Relative_selection_feature_label=["Label1", "Label2", "Label3", "Label4", "Label5", "Label6", "Label7"]
    Type3_non_Relative_selection_feature_Value=["Value1.3", "Value2.1", "Value3.4", "Value4.3",  "Value5.4", "Value6.4", "Value7.4"]



Type1_Domain_selection = False/True
Type1_Domain_ID = ["Transfer",...] or ["snomedTermA",..] or []


'''

