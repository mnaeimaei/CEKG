

import A1_Scenario_Step2 as Ne0
import A6_Scenario_Final_Step as Ne02

import B02_txt_write as txtW




print("********************************* Create the file **************************************************")
DFG=Ne0.DFG


DFG_FilePath=txtW.createEmptyGeneralFile(DFG)
print("DFG_FilePath=", DFG_FilePath)

print("********************************* Part1 **************************************************")

entityList=Ne0.entityList
print("entityList=", entityList)

EnNum=len(Ne0.entityList)
print("EnNum=", EnNum)

TypeShow=txtW.writeEntityDFShiw(DFG_FilePath, EnNum, entityList,1)
print("TypeShow=", TypeShow)


print("********************************* Part2 **************************************************")


Type_selection=txtW.writeIDSelection(DFG_FilePath, 1)
print("Type_selection=", Type_selection)

print("********************************* Part3 **************************************************")


txtW.writeIDSelectionInstance(Type_selection,entityList,TypeShow,DFG_FilePath,1)


print("********************************* Execution **************************************************")

import subprocess

subprocess.run(['python', 'XXXXX.py'])


print("********************************* Example **************************************************")
'''

Example:

Type1_Entity1_DF_Show=1
Type1_Entity2_DF_Show=1
Type1_Entity3_DF_Show=1
Type1_selection=True
Type1_selection_ID=['Patient', 'Admission', 'Concept']
Type1_selection_ID_instances=[['1', '2'], ['1'], ['6']]


'''


