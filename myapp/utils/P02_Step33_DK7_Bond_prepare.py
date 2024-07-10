from neo4j import GraphDatabase
import pandas as pd
import time, os, csv
import P01_funcs33_DK7_Bond_prepare as cl1g
import B02_base as cl2
import A5_EntryCol_Step3_Step as cl1
import A1_Scenario_Step2 as clo
import B02_txt_read as txtF

print("")
print("************************** From Event Log Entry (performance) ****************************************************************************")


Perf_file_path = cl1.Perf_file_path
print("Perf_file_path=", Perf_file_path)



print("************************** input from cl1: ****************************************************************************")

driver = cl1.driver


Neo4JImport=cl2.Neo4j_import_dir(driver)
print("Neo4JImport=",Neo4JImport)

print("************************** input from CSV: DK ****************************************************************************")


DK7_Input_Activity_DK7_FileName = cl1.DK7_Input_Activity_DK7_FileName
DK7_Neo4JImport_Activity_DK7_FileName = cl1.DK7_Neo4JImport_Activity_DK7_FileName


DK7_Activity_Value_ID = cl1.DK7_Activity_Value_ID
DK7_Disorders = cl1.DK7_Disorders



csv_Event_Diagnoses=cl2.ImportCSV(DK7_Input_Activity_DK7_FileName)
#print("csv_Event_Diagnoses=\n",csv_Event_Diagnoses)
#print("")


Event_Diagnoses_MappingRelation=cl1g.CreateMappingRelation2(csv_Event_Diagnoses,  DK7_Activity_Value_ID , DK7_Disorders)
print("Event_Diagnoses_MappingRelation=",Event_Diagnoses_MappingRelation)
print("")


cl1g.Create_CSV_in_Neo4J_import(csv_Event_Diagnoses, Neo4JImport, DK7_Neo4JImport_Activity_DK7_FileName)

Event_Diagnoses_OCPS, csvLog_Event_Diagnoses= cl2.LoadLog(Neo4JImport+DK7_Neo4JImport_Activity_DK7_FileName)
#print("Event_Diagnoses_OCPS=",Event_Diagnoses_OCPS)
#print("")
#print("csvLog_Event_Diagnoses=\n",csvLog_Event_Diagnoses)
#print("")



print("************************** input for: Split ****************************************************************************")

Event_Diagnose_MappingRelation_split =cl1g.dkSplit(Event_Diagnoses_MappingRelation)
print("Event_Diagnose_MappingRelation_split=",Event_Diagnose_MappingRelation_split)
print(len(Event_Diagnose_MappingRelation_split))
print("")

print("************************** input for: ScenarioEntity ****************************************************************************")

myInput=clo.myInput
print("myInput=",myInput)



if myInput == 'main_Entities': #1
    print("************************** input for: Scenario 1 ****************************************************************************")
    # Main Disorder
    print("This scenario doesn't use DK7")


if myInput == 'main_Entities_plus_Disorder': #2
    print("************************** input for: Scenario 1 ****************************************************************************")
    # Main Disorder
    sc2_list =cl1g.sc2(driver, Event_Diagnose_MappingRelation_split)
    print("sc2_list=",sc2_list)
    print(len(sc2_list))
    print("")

if myInput == 'main_Entities_plus_ICD': #3
    print("************************** input for: Scenario 2 ****************************************************************************")
    # ICD
    sc3_list =cl1g.sc3(driver, Event_Diagnose_MappingRelation_split)
    print("sc3_list=",sc3_list)
    print(len(sc3_list))
    print("")

if myInput == 'main_Entities_plus_ICD_level_doesnt_work': #4
    print("************************** input for: Scenario 3 ****************************************************************************")
    # ICD UP
    sc4_list =cl1g.sc4(driver, Event_Diagnose_MappingRelation_split)
    print("sc4_list=",sc4_list)
    print(len(sc4_list))
    print("")

if myInput == 'main_Entities_plus_SCT': #5
    print("************************** input for: Scenario 4 ****************************************************************************")
    # SNOMED
    sc5_list =cl1g.sc5(driver, Event_Diagnose_MappingRelation_split)
    print("sc5_list=",sc5_list)
    print(len(sc5_list))
    print("")


if myInput == 'main_Entities_plus_SCT_level': #6
    print("************************** input for: Scenario 5 ****************************************************************************")
    # SNOMED UP

    txtFileExistance = txtF.txtExistance(myInput)
    print("txtFileExistance=", txtFileExistance)

    if txtFileExistance == True:
        distanceFromTLC = txtF.listIntTxt(myInput, "distanceFromTLC")
        Semanti_tags = txtF.stringTxt(myInput, "Semanti_tags")
        ConceptType = txtF.stringTxt(myInput, "ConceptType")
        TLC_Semanti_tags = txtF.stringTxt(myInput, "TLC_Semanti_tags")
    else:
        distanceFromTLC = 1
        Semanti_tags = "disorder"
        ConceptType = "Concept"
        TLC_Semanti_tags = "finding"

    sc6_list =cl1g.sc6(driver, Event_Diagnose_MappingRelation_split,distanceFromTLC,Semanti_tags,ConceptType,TLC_Semanti_tags)
    print("sc6_list=",sc6_list)
    print(len(sc6_list))
    print("")


if myInput == 'main_Entities_plus_SCT_Level_One': #7
    print("************************** input for: Scenario 6 ****************************************************************************")


    txtFileExistance = txtF.txtExistance(myInput)
    print("txtFileExistance=", txtFileExistance)

    if txtFileExistance == True:
        distanceFromTLC = txtF.listIntTxt(myInput, "distanceFromTLC")
        Semanti_tags = txtF.stringTxt(myInput, "Semanti_tags")
        ConceptType = txtF.stringTxt(myInput, "ConceptType")
        TLC_Semanti_tags = txtF.stringTxt(myInput, "TLC_Semanti_tags")
    else:
        distanceFromTLC = 1
        Semanti_tags = "disorder"
        ConceptType = "Concept"
        TLC_Semanti_tags = "finding"


    sc7_list =cl1g.sc7(driver, Event_Diagnose_MappingRelation_split,distanceFromTLC,Semanti_tags,ConceptType,TLC_Semanti_tags)
    print("sc7_list=",sc7_list)
    print(len(sc7_list))
    print("")

if myInput == 'main_Entities_plus_ICD_one': #8
    print("************************** input for: Scenario 7 ****************************************************************************")
    # ICD Specific

    txtFileExistance = txtF.txtExistance(myInput)
    print("txtFileExistance=", txtFileExistance)

    if txtFileExistance==True:
        icdCode = txtF.listIntTxt(myInput, "icdCode")
    else:
        icdCode = cl1g.sc8_icdFinder(driver)


    print("icdCode=", icdCode)
    sc8_list =cl1g.sc8(driver, Event_Diagnose_MappingRelation_split,icdCode)
    print("sc8_list=",sc8_list)
    print(len(sc8_list))
    print("")


if myInput == 'main_Entities_plus_SCT_one': #9
    print("************************** input for: Scenario 8 ****************************************************************************")
    # SNOMED Specific
    txtFileExistance = txtF.txtExistance(myInput)
    print("txtFileExistance=", txtFileExistance)

    if txtFileExistance==True:
        conceptId = txtF.listIntTxt(myInput, "conceptId")
    else:
        conceptId = cl1g.sc9_sctIDFinder(driver)

    print("conceptId=", conceptId)
    sc9_list =cl1g.sc9(driver, Event_Diagnose_MappingRelation_split,conceptId)
    print("sc9_list=",sc9_list)
    print(len(sc9_list))
    print("")




