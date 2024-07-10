
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

TypeShow=txtW.writeEntityDFShiw(DFG_FilePath, EnNum, entityList,2)
print("TypeShow=", TypeShow)


print("********************************* Part2 **************************************************")


Type_selection=txtW.writeIDSelection(DFG_FilePath, 2)
print("Type1_selection=", Type_selection)

print("********************************* Part3 **************************************************")

Type_approach=txtW.writeIDSelectionTypeFeature(Type_selection, DFG_FilePath, 2)
print("Type1_approach=", Type_approach)

print("********************************* Part4 **************************************************")


txtW.writeIDSelectionInstancefeature(Type_approach,entityList,TypeShow,DFG_FilePath,2)


print("********************************* Part5 **************************************************")

TypeShowIntra=txtW.writeIntraEntityDFShiw(TypeShow,DFG_FilePath, EnNum, entityList,2)
print("TypeShowIntra=", TypeShowIntra)



print("********************************* Part6 **************************************************")

Type_Domain_selection=txtW.writeDomainIDSelection(DFG_FilePath, 2)
print("Type1_Domain_selection=", Type_Domain_selection)

DomainNode = Ne02.DomainNode
domainColTitle = Ne02.domainColTitle[0]

txtW.writeIDDomainSelectionInstance(Type_Domain_selection,DFG_FilePath,DomainNode[0],domainColTitle,2)

print("********************************* Execution **************************************************")

import subprocess

subprocess.run(['python', 'T52_Step_DFG2_featureValue_DomainConceptLevel_16.py'])


print("********************************* Example **************************************************")
'''

Example:

Type1_Entity1_DF_Show=1
Type1_Entity2_DF_Show=1
Type1_Entity3_DF_Show=1
Type1_selection=True
Type1_selection_ID=['Patient', 'Admission', 'Concept']
Type1_selection_ID_instances=[['1', '2'], ['1'], ['6']]





# Type1_Entity="Entity1_Origin"
# Type1_Entity_ID=2

Type1_Entity1_DF_Show = 1
Type1_Entity2_DF_Show = 1
Type1_Entity3_DF_Show = 0


Type1_selection = True # True if we wamt to select specific ID, False if we wamt to show all the table
Type1_approach=2 (0,1,2)

##################################################
NEW

#approach0:
Type1_selection_ID = []
Type1_selection_ID_instances = []  
Type1_selection_feature_Name=[]
Type1_selection_feature_label=[]
Type1_selection_feature_Value=[]


#approach1:
Type1_selection_ID = ["Patient","Admission"]
Type1_selection_ID_instances = [["1"],["13"]]  
Type1_selection_feature_Name=[]
Type1_selection_feature_label=[]
Type1_selection_feature_Value=[]



#approach2:
Type1_selection_ID = ["Patient"]
Type1_selection_ID_instances = []
Type1_selection_feature_Name=["ABG_Test"]
Type1_selection_feature_label=["Label1", "Label2", "Label3", "Label4", "Label5", "Label6", "Label7"]
Type1_selection_feature_Value=["Value1.3", "Value2.1", "Value3.4", "Value4.3",  "Value5.4", "Value6.4", "Value7.4"]


old
#approach1:
Type1_selection_ID_1 = ["Patient","Admission"]
Type1_selection_ID_instances_1 = [["1"],["13"]]  # Works if True # also [47,50]

#approach2:
Type1_selection_ID_2 = ["Patient"]
Type1_selection_feature_Name_2="ABG_Test"
Type1_selection_feature_label_2=["Label1", "Label2", "Label3", "Label4", "Label5", "Label6", "Label7"]
Type1_selection_feature_Value_2=["Value1.3", "Value2.1", "Value3.4", "Value4.3",  "Value5.4", "Value6.4", "Value7.4"]

##################################################
Type2_Entity1OrgRel_DF_Show = 1
Type2_Entity2OrgRel_DF_Show = 1
Type2_Entity3OrgRel_DF_Show = 1

Type1_Domain_selection = False/True
Type1_Domain_ID = ["Transfer",...] or ["snomedTermA",..] or []


'''