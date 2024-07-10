from neo4j import GraphDatabase
import pandas as pd
import time, os, csv
import H01_funcs17_ClinicalEntity_prepare as cl1b
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

print("************************** input from cl1: Potential_Nodes ****************************************************************************")


CE_Input_PoNode_FileName = cl1.CE_Input_PoNode_FileName
print(CE_Input_PoNode_FileName)
CE_Neo4JImport_PoNode_FileName = cl1.CE_Neo4JImport_PoNode_FileName

CE_ClinicalEntity = cl1.CE_ClinicalEntity
CE_icd_code = cl1.CE_icd_code
CE_icd_version = cl1.CE_icd_version
CE_icd_code_title = cl1.CE_icd_code_title


csv_CE=cl2.ImportCSV(CE_Input_PoNode_FileName)
print("csv_CE=\n",csv_CE)
print("")

cl1b.Create_CSV_in_Neo4J_import(csv_CE, Neo4JImport, CE_Neo4JImport_PoNode_FileName)

header_CE, csvLog_CE = cl2.LoadLog(Neo4JImport+CE_Neo4JImport_PoNode_FileName)
print("header_CE=",header_CE)
print("")
print("csvLog_CE=\n",csvLog_CE)
print("")


print("************************** input from cl1 ****************************************************************************")

caseICD=cl1b.CreateCase(csvLog_CE, CE_ClinicalEntity, CE_icd_code, CE_icd_version, CE_icd_code_title)
print("caseICD=",caseICD)
