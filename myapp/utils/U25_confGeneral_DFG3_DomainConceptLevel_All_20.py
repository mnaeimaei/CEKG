
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

print("********************************* Part6 **************************************************")

Type3_non_Relative_selection_ID_instances=txtW.writeIDSelectionInstanceType3(Type3,Type3_non_Relative_selection,entityList, TypeShow, DFG_FilePath, 3)
print("Type3_non_Relative_selection_ID_instances=", Type3_non_Relative_selection_ID_instances)


print("********************************* write in Q **************************************************")

txtW.writeInQ("DFG3_config",Type3,Type3_non_Relative_selection,Type3_non_Relative_selection_ID_instances)

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

subprocess.run(['python', 'U24_Step_DFG3_DomainConceptLevel_All_20.py'])


print("********************************* Example **************************************************")


'''
Example:

Type3_Entity1_DF_Show=1
Type3_Entity2_DF_Show=1
Type3_Entity3_DF_Show=1

Type3_Count=0

Type3 = 1 # 1=RelateveAndAbsolute  2=OnlyAbsolute (non Relative)

if Type3 = 1:
    Type3_non_Relative_selection=False
    Type3_non_Relative_selection_ID_instances=[] 

if Type3 = 2:
    Type3_non_Relative_selection=False
    Type3_non_Relative_selection_ID_instances=[] 


if Type3 = 2:
    Type3_non_Relative_selection=True
    Type3_non_Relative_selection_ID_instances=[["1"],["13"],["44054006"]] 


Type1_Domain_selection = False/True
Type1_Domain_ID = ["Transfer",...] or ["snomedTermA",..] or []


'''
