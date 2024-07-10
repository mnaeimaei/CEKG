

import A1_Scenario_Step2 as Ne0
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


TypeShow=txtW.writeEntityDFShiw(DFG_FilePath, EnNum, entityList,1)
print("TypeShow=", TypeShow)


print("********************************* Part2 **************************************************")


Type_selection=txtW.writeIDSelection(DFG_FilePath, 1)
print("Type1_selection=", Type_selection)

print("********************************* Part3 **************************************************")


txtW.writeIDSelectionInstance(Type_selection,entityList,TypeShow,DFG_FilePath,1)

print("********************************* Part4 **************************************************")


Type_Domain_selection=txtW.writeDomainIDSelection(DFG_FilePath, 1)
print("Type1_Domain_selection=", Type_Domain_selection)

DomainNode = Ne02.DomainNode
domainColTitle = Ne02.domainColTitle[0]

txtW.writeIDDomainSelectionInstance(Type_Domain_selection,DFG_FilePath,DomainNode[0],domainColTitle,1)

print("********************************* Execution **************************************************")


import subprocess

subprocess.run(['python', 'S10_Step_DFG1_Domain_2.py'])


print("********************************* Example **************************************************")
'''

Example:


Type1_Entity1_DF_Show = 1
Type1_Entity2_DF_Show = 1
Type1_Entity3_DF_Show = 0


Type1_selection = False # True if we wamt to select specific ID, False if we wamt to show all the table
Type1_selection_ID = ["Subject","Visit"]
Type1_selection_ID_instances = [["1"],["21","22"]]  # Works if True # also [47,50]

Type1_Domain_selection = False/True
Type1_Domain_ID = ["Transfer",...] or ["snomedTermA",..] or []



'''