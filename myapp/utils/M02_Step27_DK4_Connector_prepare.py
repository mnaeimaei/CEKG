from neo4j import GraphDatabase
import pandas as pd
import time, os, csv
import M01_funcs27_DK4_Connector_prepare as cl1e
import B02_base as cl2
import A5_EntryCol_Step3_Step as cl1


print("")
print("************************** From Event Log Entry (performance) ****************************************************************************")


Perf_file_path = cl1.Perf_file_path
print("Perf_file_path=", Perf_file_path)




print("************************** input from cl1: ****************************************************************************")

driver = cl1.driver


Neo4JImport=cl2.Neo4j_import_dir(driver)
print("Neo4JImport=",Neo4JImport)



print("************************** input from cl1: Potential_OCT ****************************************************************************")

DK4_Input_ICD_OCT_FileName=cl1.DK4_Input_ICD_OCT_FileName
DK4_Neo4JImport_ICD_OCT_FileName=cl1.DK4_Neo4JImport_ICD_OCT_FileName


DK4_icd_code = cl1.DK4_icd_code
DK4_OTC  = cl1.DK4_OTC




csv_ICD_OCT=cl2.ImportCSV(DK4_Input_ICD_OCT_FileName)
print("csv_ICD_OCT=\n",csv_ICD_OCT)
print(csv_ICD_OCT.dtypes)
#print("")



cl1e.Create_CSV_in_Neo4J_import(csv_ICD_OCT, Neo4JImport, DK4_Neo4JImport_ICD_OCT_FileName )

header_ICD_OCT, csvLog_ICD_OCT = cl2.LoadLog(Neo4JImport+DK4_Neo4JImport_ICD_OCT_FileName)
print("header_ICD_OCT=",header_ICD_OCT)
print("")
print("csvLog_ICD_OCT=\n",csvLog_ICD_OCT)
print("")



print("************************** DK 4 ****************************************************************************")

icdOCT=cl1e.CreateRel(csvLog_ICD_OCT)
print("icdOCT=",icdOCT)
