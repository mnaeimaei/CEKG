
import os
from neo4j import GraphDatabase
import A1_Scenario_Step3 as sc
import A5_EntryCol_Step3_Func as A4_Func

EventLog=sc.EventLog
otherEntities=sc.otherEntities
otherEntitiesRel=sc.otherEntitiesRel
acProperties=sc.acProperties
Domain=sc.Domain
ICD=sc.ICD
octNode=sc.octNode
octRel=sc.octRel


DK1=sc.DK1
DK2=sc.DK2
DK3=sc.DK3
DK4=sc.DK4
DK5=sc.DK5
DK6_1=sc.DK6_1
DK6_2=sc.DK6_2
DK7=sc.DK7




print("************************** General ****************************************************************************")

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))
driverUserName="neo4j"
driverPassword="12345678"


selenium=False

Data1 =  '../../media/uploads/0_Data'
Data = os.path.realpath(Data1)
Data_Extension = '.csv'

perf_Name= 'all_Performance'
Perf_FileName = Data + "/" + perf_Name + Data_Extension
Perf_file_path = os.path.realpath(Perf_FileName)

confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)
print("confPath=",confPath)

fileSourceInt, value1, value2, sheetTitles=A4_Func.readtxtFiles()
print("fileSourceInt=", fileSourceInt)
print("value1=", value1)
print("value2=", value2)
print("sheetTitles=", sheetTitles)



print("************************** Step2 ****************************************************************************")



if EventLog:
    ED_dataSet = 'EventLog'
    print("ED_dataSet=", ED_dataSet)

    index_of_x = sc.sheetTitleshelper.index("ED_Event_FileName")
    ED_Event_FileName = sheetTitles[index_of_x] #C_Log


    ED_Input_Event_FileName = Data + "/" + ED_Event_FileName + Data_Extension
    print("ED_Input_Event_FileName=", ED_Input_Event_FileName)
    ED_Neo4JImport_Event_FileName = ED_Event_FileName + '_Neo4j' + Data_Extension
    print("ED_Neo4JImport_Event_FileName=", ED_Neo4JImport_Event_FileName)



    ED_Event_FileName = 'C_Log'
    dictFinal=A4_Func.Other_DefaultMenu(confPath, ED_Event_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value


    print("ED_eventIdTitle=", ED_eventIdTitle)
    print("ED_Activity=", ED_Activity)
    print("ED_ActivitySynonym=", ED_ActivitySynonym)
    print("ED_Activity_Value_ID=", ED_Activity_Value_ID)
    print("ED_Activity_Properties_ID=", ED_Activity_Properties_ID)


    print("Timestamp=", ED_Timestamp)


    print("ED_EnNum=", ED_EnNum)

    dicEntOrigin = A4_Func.EntityOrigins_values(ED_EnNum)
    # print(dicEnt)
    locals().update(dicEntOrigin)
    print("Entities Origin Columns (dicEntOrigin)=", dicEntOrigin)

    dicEntID = A4_Func.EntityIDColumn(ED_EnNum)
    # print(dicEnt)
    locals().update(dicEntID)
    print("Entities ID Column (dicEntID)=", dicEntID)

    EntityListEL=A4_Func.EntityListsELFunc(ED_Event_FileName,dicEntOrigin)
    print("EntityListEL=", EntityListEL)
    entityListIDproperty = ['ID'] * (ED_EnNum)
    print("entityListIDproperty=", entityListIDproperty)
    conditionProperty = ['Category'] * (ED_EnNum)
    print("conditionProperty=", conditionProperty)
    conditionPropertyValue = ['Absolute'] * (ED_EnNum)
    print("conditionPropertyValue=", conditionPropertyValue)

print("************************** Step4 ****************************************************************************")

if otherEntities==True and otherEntitiesRel==True:
    EnP_dataSet = 'EventLogEntities'
    print("EnP_dataSet=", EnP_dataSet)

    index_of_x1 = sc.sheetTitleshelper.index("EnP_PoNode_FileName_1")
    EnP_PoNode_FileName_1 = sheetTitles[index_of_x1] #C_Log


    index_of_x2 = sc.sheetTitleshelper.index("EnP_PoNode_FileName_2")
    EnP_PoNode_FileName_2 = sheetTitles[index_of_x2] #C_Log

    EnP_Input_PoNode_FileName_1 = Data + "/" + EnP_PoNode_FileName_1 + Data_Extension
    print("EnP_Input_PoNode_FileName_1=", EnP_Input_PoNode_FileName_1)
    EnP_Input_PoNode_FileName_2 = Data + "/" + EnP_PoNode_FileName_2 + Data_Extension
    print("EnP_Input_PoNode_FileName_2=", EnP_Input_PoNode_FileName_2)

    EnP_Neo4JImport_PoNode_FileName_1 = EnP_PoNode_FileName_1 + '_Neo4j' + Data_Extension
    print("EnP_Neo4JImport_PoNode_FileName_1=", EnP_Neo4JImport_PoNode_FileName_1)
    EnP_Neo4JImport_PoNode_FileName_2 = EnP_PoNode_FileName_2 + '_Neo4j' + Data_Extension
    print("EnP_Neo4JImport_PoNode_FileName_2=", EnP_Neo4JImport_PoNode_FileName_2)


    dictFinal=A4_Func.Other_DefaultMenu(confPath, EnP_PoNode_FileName_1)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value



    print("EnP_Origin=", EnP_Origin)
    print("EnP_ID=", EnP_ID)
    print("EnP_Name=", EnP_Name)
    print("EnP_Value=", EnP_Value)
    print("EnP_Category=", EnP_Category)

    dictFinal=A4_Func.Other_DefaultMenu(confPath, EnP_PoNode_FileName_2)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value


    print("EnP_Entity_Origin1=", EnP_Entity_Origin1)
    print("EnP_Entity_ID1=", EnP_Entity_ID1)
    print("EnP_Entity_Origin2=", EnP_Entity_Origin2)
    print("EnP_Entity_ID2=", EnP_Entity_ID2)




print("************************** Step5 ****************************************************************************")

if acProperties:
    AcP_dataSet = 'EventLogActivitiesProperties'
    print("AcP_dataSet=", AcP_dataSet)


    index_of_x = sc.sheetTitleshelper.index("AcP_PoNode_FileName")
    AcP_PoNode_FileName = sheetTitles[index_of_x] #C_Log


    AcP_Input_PoNode_FileName = Data + "/" + AcP_PoNode_FileName + Data_Extension
    print("AcP_Input_PoNode_FileName=", AcP_Input_PoNode_FileName)
    AcP_Neo4JImport_PoNode_FileName = AcP_PoNode_FileName + '_Neo4j' + Data_Extension
    print("AcP_Neo4JImport_PoNode_FileName=", AcP_Neo4JImport_PoNode_FileName)

    dictFinal=A4_Func.Other_DefaultMenu(confPath, AcP_PoNode_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value



    print("AcP_acID=", AcP_acID)
    print("AcP_activityName=", AcP_activityName)
    print("AcP_activitySynonym=", AcP_activitySynonym)
    print("AcP_label=", AcP_label)
    print("AcP_Value=", AcP_Value)


print("************************** Step6 ****************************************************************************")

if Domain:
    ACTdataSet = 'EventLogDomain'
    print("ACTdataSet=", ACTdataSet)


    index_of_x = sc.sheetTitleshelper.index("ACT_PoNode_FileName")
    ACT_PoNode_FileName = sheetTitles[index_of_x] #C_Log



    ACT_Input_PoNode_FileName = Data + "/" + ACT_PoNode_FileName + Data_Extension
    print("ACT_Input_PoNode_FileName=", ACT_Input_PoNode_FileName)
    ACT_Neo4JImport_PoNode_FileName = ACT_PoNode_FileName + '_Neo4j' + Data_Extension
    print("ACT_Neo4JImport_PoNode_FileName=", ACT_Neo4JImport_PoNode_FileName)



    dictFinal=A4_Func.Other_DefaultMenu(confPath, ACT_PoNode_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value

    print("ACT_Domain=", ACT_Domain)

print("************************** Step7 ****************************************************************************")

if ICD:
    CEdataSet = 'ICD'
    print("CEdataSet=", CEdataSet)

    index_of_x = sc.sheetTitleshelper.index("CE_PoNode_FileName")
    CE_PoNode_FileName = sheetTitles[index_of_x] #C_Log



    CE_Input_PoNode_FileName = Data + "/" + CE_PoNode_FileName + Data_Extension
    print("CE_Input_PoNode_FileName=", CE_Input_PoNode_FileName)
    CE_Neo4JImport_PoNode_FileName = CE_PoNode_FileName + '_Neo4j' + Data_Extension
    print("CE_Neo4JImport_PoNode_FileName=", CE_Neo4JImport_PoNode_FileName)

    dictFinal=A4_Func.Other_DefaultMenu(confPath, CE_PoNode_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value



    print("CE_ClinicalEntity=", CE_ClinicalEntity)
    print("CE_icd_code=", CE_icd_code)
    print("CE_icd_version=", CE_icd_version)
    print("CE_icd_code_title=", CE_icd_code_title)

print("************************** Step8 ****************************************************************************")

if octNode==True and octRel==True:

    OCTdataSet = 'SNOMED_CT'
    print("OCTdataSet=", OCTdataSet)

    index_of_x1 = sc.sheetTitleshelper.index("OCT_OCT_Node_FileName")
    OCT_OCT_Node_FileName = sheetTitles[index_of_x1] #C_Log

    index_of_x2 = sc.sheetTitleshelper.index("OCT_OCT_REL_FileName")
    OCT_OCT_REL_FileName = sheetTitles[index_of_x2] #C_Log



    OCT_Input_OCT_Node_FileName = Data + "/" + OCT_OCT_Node_FileName + Data_Extension
    print("OCT_Input_OCT_Node_FileName=", OCT_Input_OCT_Node_FileName)
    OCT_Input_OCT_REL_FileName = Data + "/" + OCT_OCT_REL_FileName + Data_Extension
    print("OCT_Input_OCT_REL_FileName=", OCT_Input_OCT_REL_FileName)


    OCT_Neo4JImport_OCT_Node_FileName = OCT_OCT_Node_FileName + '_Neo4j' + Data_Extension
    print("OCT_Neo4JImport_OCT_Node_FileName=", OCT_Neo4JImport_OCT_Node_FileName)
    OCT_Neo4JImport_OCT_REL_FileName = OCT_OCT_REL_FileName + '_Neo4j' + Data_Extension
    print("OCT_Neo4JImport_OCT_REL_FileName=", OCT_Neo4JImport_OCT_REL_FileName)


    dictFinal=A4_Func.Other_DefaultMenu(confPath, OCT_OCT_Node_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value

    print("OCT_OCT_Node_conceptId=", OCT_OCT_Node_conceptId)
    print("OCT_OCT_Node_ConceptCode=", OCT_OCT_Node_ConceptCode)
    print("OCT_OCT_Node_termA=", OCT_OCT_Node_termA)
    print("OCT_OCT_Node_termB=", OCT_OCT_Node_termB)
    print("OCT_OCT_Node_semanticTags=", OCT_OCT_Node_semanticTags)
    print("OCT_OCT_Node_ConceptType=", OCT_OCT_Node_ConceptType)
    print("OCT_OCT_Node_Levels=", OCT_OCT_Node_Levels)


    dictFinal=A4_Func.Other_DefaultMenu(confPath, OCT_OCT_REL_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value




    print("OCT_OCT_REL_s0=", OCT_OCT_REL_s0)
    print("OCT_OCT_REL_s0_code=", OCT_OCT_REL_s0_code)
    print("OCT_OCT_REL_s1=", OCT_OCT_REL_s1)
    print("OCT_OCT_REL_s1_code=", OCT_OCT_REL_s1_code)


print("************************** Step9 ****************************************************************************")

if DK1:

    DK1dataSet = 'empty'
    print("DK1dataSet=", DK1dataSet)

    index_of_x = sc.sheetTitleshelper.index("DK1_EnPo_FileName")
    DK1_EnPo_FileName = sheetTitles[index_of_x] #C_Log


    DK1_Input_EnPo_FileName = Data + "/" + DK1_EnPo_FileName + Data_Extension
    print("DK1_Input_EnPo_FileName=", DK1_Input_EnPo_FileName)
    DK1_Neo4JImport_EnPo_FileName = DK1_EnPo_FileName + '_Neo4j' + Data_Extension
    print("DK1_Neo4JImport_EnPo_FileName=", DK1_Neo4JImport_EnPo_FileName)

    #dictFinal=A3_Func.Other_DefaultMenu(confPath, DK1_EnPo_FileName)
    #print("dictFinal=", dictFinal)
    #for key, value in dictFinal.items():
        #locals()[key] = value



print("************************** Step10 ****************************************************************************")

if DK2:
    DK2dataSet = 'empty'
    print("DK2dataSet=", DK2dataSet)

    index_of_x = sc.sheetTitleshelper.index("DK2_EnPo_FileName")
    DK2_EnPo_FileName = sheetTitles[index_of_x] #C_Log



    DK2_Input_Multimorbidity_Disorders_FileName = Data + "/" + DK2_EnPo_FileName + Data_Extension
    print("DK2_Input_Multimorbidity_Disorders_FileName=", DK2_Input_Multimorbidity_Disorders_FileName)
    DK2_Neo4JImport_Multimorbidity_Disorders_FileName = DK2_EnPo_FileName + '_Neo4j' + Data_Extension
    print("DK2_Neo4JImport_Multimorbidity_Disorders_FileName=", DK2_Neo4JImport_Multimorbidity_Disorders_FileName)

    #dictFinal=A3_Func.Other_DefaultMenu(confPath, DK2_EnPo_FileName)
    #print("dictFinal=", dictFinal)
    #for key, value in dictFinal.items():
        #locals()[key] = value


print("************************** Step11 ****************************************************************************")

if DK3:
    DK3dataSet = 'manual'
    print("DK3dataSet=", DK3dataSet)

    index_of_x = sc.sheetTitleshelper.index("DK3_Potential_DK3_FileName")
    DK3_Potential_DK3_FileName = sheetTitles[index_of_x] #C_Log


    DK3_Input_Potential_DK3_FileName = Data + "/" + DK3_Potential_DK3_FileName + Data_Extension
    print("DK3_Input_Potential_DK3_FileName=", DK3_Input_Potential_DK3_FileName)

    DK3_Neo4JImport_Potential_OCPS_FileName = DK3_Potential_DK3_FileName + '_Neo4j' + Data_Extension
    print("DK3_Neo4JImport_Potential_OCPS_FileName=", DK3_Neo4JImport_Potential_OCPS_FileName)

    dictFinal=A4_Func.Other_DefaultMenu(confPath, DK3_Potential_DK3_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value


    print("DK3_Disorders=", DK3_Disorders)
    print("DK3_icd_code=", DK3_icd_code)

print("************************** Step12 ****************************************************************************")

if DK4:
    DK4dataSet = 'manual'
    print("DK4dataSet=", DK4dataSet)


    index_of_x = sc.sheetTitleshelper.index("DK4_ICD_OCT_FileName")
    DK4_ICD_OCT_FileName = sheetTitles[index_of_x] #C_Log

    DK4_Input_ICD_OCT_FileName = Data + "/" + DK4_ICD_OCT_FileName + Data_Extension
    print("DK4_Input_ICD_OCT_FileName=", DK4_Input_ICD_OCT_FileName)
    DK4_Neo4JImport_ICD_OCT_FileName = DK4_ICD_OCT_FileName + '_Neo4j' + Data_Extension
    print("DK4_Neo4JImport_ICD_OCT_FileName=", DK4_Neo4JImport_ICD_OCT_FileName)

    dictFinal=A4_Func.Other_DefaultMenu(confPath, DK4_ICD_OCT_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value



    print("DK4_icd_code=", DK4_icd_code)
    print("DK4_OTC=", DK4_OTC)


print("************************** Step13 ****************************************************************************")

if DK5:
    DK5dataSet = 'manual'
    print("DK5dataSet=", DK5dataSet)

    index_of_x = sc.sheetTitleshelper.index("DK5_FileName")
    DK5_FileName = sheetTitles[index_of_x] #C_Log

    DK5_Input_Activity_FileName = Data + "/" + DK5_FileName + Data_Extension
    print("DK5_Input_Activity_FileName=", DK5_Input_Activity_FileName)
    DK5_Neo4JImport_Activity_DK5_FileName = DK5_FileName + '_Neo4j' + Data_Extension
    print("DK5_Neo4JImport_Activity_DK5_FileName=", DK5_Neo4JImport_Activity_DK5_FileName)


    dictFinal=A4_Func.Other_DefaultMenu(confPath, DK5_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value



    print("DK5_Activity=", DK5_Activity)
    print("DK5_Activity_Synonym=", DK5_Activity_Synonym)
    print("DK5_OTC=", DK5_OTC)
    print("DK5_SCTCode=", DK5_SCTCode)


print("************************** Step14 ****************************************************************************")

if DK6_1==True and DK6_2==True:
    DomainDataSet = 'manual'
    print("DomainDataSet=", DomainDataSet)

    index_of_x1 = sc.sheetTitleshelper.index("Domain_FileName_1")
    Domain_FileName_1 = sheetTitles[index_of_x1] #C_Log

    index_of_x2 = sc.sheetTitleshelper.index("Domain_FileName_2")
    Domain_FileName_2 = sheetTitles[index_of_x2] #C_Log


    Domain_Input_FileName_1 = Data + "/" + Domain_FileName_1 + Data_Extension
    print("Domain_Input_FileName_1=", Domain_Input_FileName_1)
    Domain_Input_FileName_2 = Data + "/" + Domain_FileName_2 + Data_Extension
    print("Domain_Input_FileName_2=", Domain_Input_FileName_2)


    Domain_Neo4JImport_FileName_1 = Domain_FileName_1 + '_Neo4j' + Data_Extension
    print("Domain_Neo4JImport_FileName_1=", Domain_Neo4JImport_FileName_1)
    Domain_Neo4JImport_FileName_2 = Domain_FileName_2 + '_Neo4j' + Data_Extension
    print("Domain_Neo4JImport_FileName_2=", Domain_Neo4JImport_FileName_2)

    dictFinal=A4_Func.Other_DefaultMenu(confPath, Domain_FileName_1)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value


    print("Domain1_Activity=", Domain1_Activity)
    print("Domain1_Activity_Synonym=", Domain1_Activity_Synonym)
    print("Domain1_Domain=", Domain1_Domain)

    dictFinal=A4_Func.Other_DefaultMenu(confPath, Domain_FileName_2)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value



    print("Domain2_Domain=", Domain2_Domain)
    print("Domain2_OTC=", Domain2_OTC)
    print("Domain2_SCTCode=", Domain2_SCTCode)


print("************************** Step15 ****************************************************************************")


if DK7:
    DK7dataSet = 'ML'
    print("DK7dataSet=", DK7dataSet)

    index_of_x = sc.sheetTitleshelper.index("DK7_Activity_DK7_FileName")
    DK7_Activity_DK7_FileName = sheetTitles[index_of_x] #C_Log


    DK7_Input_Activity_DK7_FileName = Data + "/" +  DK7_Activity_DK7_FileName + Data_Extension
    print("DK7_Input_Activity_DK7_FileName=", DK7_Input_Activity_DK7_FileName)
    DK7_Neo4JImport_Activity_DK7_FileName = DK7_Activity_DK7_FileName + '_Neo4j' + Data_Extension
    print("DK7_Neo4JImport_Activity_DK7_FileName=", DK7_Neo4JImport_Activity_DK7_FileName)


    dictFinal=A4_Func.Other_DefaultMenu(confPath, DK7_Activity_DK7_FileName)
    print("dictFinal=", dictFinal)
    for key, value in dictFinal.items():
        locals()[key] = value



    print("DK7_Activity_Value_ID=", DK7_Activity_Value_ID)
    print("DK7_Disorders=", DK7_Disorders)

