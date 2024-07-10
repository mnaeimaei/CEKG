


import A6_Scenario_Final_Step as Ne0
import A6_Scenario_Final_Step as Ne02

import B02_txt_write as txtW





print("********************************* Create the file **************************************************")
DFG=Ne0.DFG


DFG_FilePath=txtW.createEmptyGeneralFile(DFG)
print("DFG_FilePath=", DFG_FilePath)


print("********************************* Part1 **************************************************")

txtW.writeTypeApproach6(DFG_FilePath)



print("********************************* Part4 **************************************************")


mainEntity_selection=txtW.writeIDSelectionNonRelativT6(DFG_FilePath)
print("mainEntity_selection=", mainEntity_selection)



txtW.writeIDSelectionInstanceType6(mainEntity_selection,DFG_FilePath)



print("********************************* Execution **************************************************")

import subprocess

subprocess.run(['python', 'X10_Step_DFG6_Morbid_54.py'])


'''   
print("********************************* Example **************************************************")


Example:

Type_approach=2  (1 show common, 2 show unique)

mainEntity_selection="False"
mainEntity_selection_ID_instances = []

mainEntity_selection="True"
mainEntity_selection_ID_instances = ["1","2"]

'''




