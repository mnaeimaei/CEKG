


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

txtW.writeCount(DFG_FilePath,4)


print("********************************* Part3 **************************************************")


Type_selection=txtW.writeIDSelection(DFG_FilePath, 4)
print("Type_selection=", Type_selection)


print("********************************* Part4 **************************************************")

Type_approach = txtW.writeIDSelectionTypeFeature(Type_selection, DFG_FilePath, 4)
print("Type3_approach=", Type_approach)

print("********************************* Part6 **************************************************")

txtW.writeIDSelectionInstancefeatureType4(Type_approach, entityList, TypeShow, DFG_FilePath, 4)


print("********************************* Execution **************************************************")


import subprocess

subprocess.run(['python', 'V31_Step_DFG4_feature_Absolute_33.py'])



print("********************************* Example **************************************************")

'''
Example:

Type4_Entity1_DF_Show=1
Type4_Entity2_DF_Show=0
Type4_Entity3_DF_Show=0

Type4_Count=2

Type4_selection = True # True if we wamt to select specific ID, False if we wamt to show all the table


Type4_approach=0

    Type4_selection_ID = []  
    Type4_selection_ID_instances = []
    Type4_selection_feature_Name = []
    Type4_selection_feature_label = []
    Type4_selection_feature_Value = []
    
    
Type4_approach=1

    Type4_selection_ID = ["Patient"]  
    Type4_selection_ID_instances = ["2"]
    Type4_selection_feature_Name = []
    Type4_selection_feature_label = []
    Type4_selection_feature_Value = []


Type4_approach=2

    Type4_selection_ID = ["Patient"]  
    Type4_selection_ID_instances = [] Then convert to somthing like ["2"]
    Type4_selection_feature_Name = ["ABG_Test"]
    Type4_selection_feature_label = ["Label1", "Label2", "Label3", "Label4", "Label5", "Label6", "Label7"]
    Type4_selection_feature_Value = ["Value1.3", "Value2.1", "Value3.4", "Value4.3",  "Value5.4", "Value6.4", "Value7.4"]




'''
