from neo4j import GraphDatabase
import pandas as pd
import time, os, csv
import L01_funcs25_DK3_Linker_prepare  as clk01
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

print("************************** input from cl1: Diagnose_Potential ****************************************************************************")


DK3_Input_Potential_DK3_FileName = cl1.DK3_Input_Potential_DK3_FileName
DK3_Neo4JImport_Potential_OCPS_FileName = cl1.DK3_Neo4JImport_Potential_OCPS_FileName


DK3_Disorders = cl1.DK3_Disorders
DK3_icd_code = cl1.DK3_icd_code




csv_DP=cl2.ImportCSV(DK3_Input_Potential_DK3_FileName)
print("csv_EnPo=\n",csv_DP)
print(csv_DP.dtypes)
#print("")






clk01.Create_CSV_in_Neo4J_import(csv_DP, Neo4JImport, DK3_Neo4JImport_Potential_OCPS_FileName)

header_Diagnose_Potential, csvLog_Diagnose_Potential = cl2.LoadLog(Neo4JImport+DK3_Neo4JImport_Potential_OCPS_FileName)
print("header_Diagnose_Potential=",header_Diagnose_Potential)
print("")
print("csvLog_Diagnose_Potential=\n",csvLog_Diagnose_Potential)
print("")


print("************************** DK 3 ****************************************************************************")

DiagClinRel=clk01.CreateRel(csvLog_Diagnose_Potential)
print("DiagClinRel=",DiagClinRel)
