

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


Type_selection=txtW.writeIDSelectionNonRelativT5(DFG_FilePath, 5,1)
print("Type_selection=", Type_selection)


txtW.writeIDSelectionInstanceType5(Type_selection,entityList,Type_selection,DFG_FilePath,5,1)

print("********************************* Part4 **************************************************")


Type_selection=txtW.writeIDSelectionNonRelativT5(DFG_FilePath, 5,2)
print("Type_selection=", Type_selection)


txtW.writeIDSelectionInstanceType5(Type_selection,entityList,Type_selection,DFG_FilePath,5,2)

print("********************************* Part5 **************************************************")


Type_Domain_selection=txtW.writeDomainIDSelection(DFG_FilePath, 5)
print("Type1_Domain_selection=", Type_Domain_selection)

DomainNode = Ne02.DomainNode
domainColTitle = Ne02.domainColTitle[0]

txtW.writeIDDomainSelectionInstance(Type_Domain_selection,DFG_FilePath,DomainNode[0],domainColTitle,5)

print("********************************* write in Q **************************************************")

txtW.writeInQTyep5("DFG5_config",Type5_Rel_1_DF_Show,Type5_Rel_2_DF_Show)




print("********************************* Execution **************************************************")

import subprocess


subprocess.run(['python', 'Q02_Step1_DFG_prepare_Scenario.py'])

subprocess.run(['python', 'Q04_Step2_DFG_importingNeo4J_Scneario.py'])

subprocess.run(['python', 'W17_Step_DFG5_DomainConcept_Relative_43.py'])


print("********************************* Example **************************************************")
'''


Example:

Type5_Rel_1_DF_Show = "Patient"  #Q02
Type5_Rel_2_DF_Show = "Concept" #Q02

Type5_Count=2

Type5_Rel_1_DF_Show_selection=True
Type5_Rel_1_DF_Show_selection_ID_instances=['1', '5']

Type5_Rel_2_DF_Show_selection = False #Q02  # True if we wamt to select specific ID, False if we wamt to show all the table
Type5_Rel_2_DF_Show_selection_ID_instances = ["1","5"] #Q02 # Works if True # also [47,50]



Type4_Domain_selection = False/True
Type4_Domain_ID = ["Transfer",...] or ["snomedTermA",..] or []

'''