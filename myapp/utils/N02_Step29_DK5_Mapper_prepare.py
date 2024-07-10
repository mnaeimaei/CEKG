from neo4j import GraphDatabase
import pandas as pd
import time, os, csv
import N01_funcs29_DK5_Mapper_prepare as cl1f
import B02_base as cl2
import A5_EntryCol_Step3_Step as cl1
import A1_Scenario_Step2 as clN
import B02_txt_read as txtF

print("")
print("************************** From Event Log Entry (performance) ****************************************************************************")


Perf_file_path = cl1.Perf_file_path
print("Perf_file_path=", Perf_file_path)




print("************************** input from cl1: ****************************************************************************")

driver = cl1.driver


Neo4JImport=cl2.Neo4j_import_dir(driver)
print("Neo4JImport=",Neo4JImport)




print("************************** input from cl1: Activity_OCT ****************************************************************************")


DK5_Input_Activity_DK5_FileName = cl1.DK5_Input_Activity_FileName
DK5_Neo4JImport_Activity_DK5_FileName = cl1.DK5_Neo4JImport_Activity_DK5_FileName

DK5_Activity = cl1.DK5_Activity
DK5_Activity_Synonym = cl1.DK5_Activity_Synonym
DK5_OTC = cl1.DK5_OTC
DK5_SCTCode = cl1.DK5_SCTCode



csv_Activity_OCT=cl2.ImportCSV(DK5_Input_Activity_DK5_FileName)
#print("csv_Activity_OCT=\n",csv_Activity_OCT)
#print("")

Activity_OCT_MappingRelation=cl1f.CreateMappingRelation3(csv_Activity_OCT, DK5_Activity,DK5_Activity_Synonym,DK5_OTC,DK5_SCTCode)
print("Activity_OCPS_MappingRelation=",Activity_OCT_MappingRelation)
print("")


cl1f.Create_CSV_in_Neo4J_import(csv_Activity_OCT, Neo4JImport, DK5_Neo4JImport_Activity_DK5_FileName)

header_Activity_OCT, csvLog_Activity_OCT = cl2.LoadLog(Neo4JImport+DK5_Neo4JImport_Activity_DK5_FileName)
print("header_Activity_OCT=",header_Activity_OCT)
print("")
print("csvLog_Activity_OCT=\n",csvLog_Activity_OCT)
print("")

print("************************** input from cl1: Final ****************************************************************************")

Activity=clN.Activity
print(Activity)

if Activity == "Activity_Label" or Activity == "Concept_Label" :
    print("************************** Activity_Selection: 1 ****************************************************************************")
    final_Activity_OCT_MappingRelation =Activity_OCT_MappingRelation
    print("final_Activity_OCT_MappingRelation=",final_Activity_OCT_MappingRelation)
    print(len(final_Activity_OCT_MappingRelation))


if Activity == "Concept_Label_Level" :
    print("************************** Activity_Selection: 2 ****************************************************************************")
    # ICD UP
    txtFileExistance = txtF.txtExistance(Activity)
    print("txtFileExistance=", txtFileExistance)

    if txtFileExistance==True:
        distanceFrom_ActConc = txtF.listIntTxt(Activity, "distanceFrom_ActConc")
    else:
        distanceFrom_ActConc = 2

    print("distanceFrom_ActConc=", distanceFrom_ActConc)
    final_Activity_OCT_MappingRelation =cl1f.sc3(driver, Activity_OCT_MappingRelation,distanceFrom_ActConc)
    print("final_Activity_OCT_MappingRelation=",final_Activity_OCT_MappingRelation)
    print(len(final_Activity_OCT_MappingRelation))
    print("")


