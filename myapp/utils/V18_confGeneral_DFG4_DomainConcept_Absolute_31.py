


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

TypeShow=txtW.writeEntityDFShiwType4(DFG_FilePath, entityList,4)
print("TypeShow=", TypeShow)


print("********************************* Part2 **************************************************")


Type_selection=txtW.writeIDSelection(DFG_FilePath, 4)
print("Type_selection=", Type_selection)

print("********************************* Part3 **************************************************")


txtW.writeIDSelectionInstanceType4(Type_selection,entityList,TypeShow,DFG_FilePath,4)

print("********************************* Part4 **************************************************")

txtW.writeCount(DFG_FilePath,4)


print("********************************* Part4 **************************************************")


Type_Domain_selection=txtW.writeDomainIDSelection(DFG_FilePath, 4)
print("Type1_Domain_selection=", Type_Domain_selection)

DomainNode = Ne02.DomainNode
domainColTitle = Ne02.domainColTitle[0]

txtW.writeIDDomainSelectionInstance(Type_Domain_selection,DFG_FilePath,DomainNode[0],domainColTitle,4)



print("********************************* Execution **************************************************")

import subprocess

subprocess.run(['python', 'V03_Step_DFG4_Absolute_29.py'])


print("********************************* Example **************************************************")

'''
Example:

Type4_Entity1_DF_Show=0
Type4_Entity2_DF_Show=0
Type4_Entity3_DF_Show=1

Type4_Count=2

Type4_selection = False  # True if we wamt to select specific ID, False if we wamt to show all the table
Type4_selection_ID_instances = ["41","42"]  # Works if True # also [47,50]

Type4_Domain_selection = False/True
Type4_Domain_ID = ["Transfer",...] or ["snomedTermA",..] or []

'''