from neo4j import GraphDatabase
import pandas as pd
import time, os, csv
import I05_funcs19_OCTrel_prepare as cl1c
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




print("************************** input from cl1: OCT_REL ****************************************************************************")


OCT_Input_OCT_REL_FileName = cl1.OCT_Input_OCT_REL_FileName
OCT_Neo4JImport_OCT_REL_FileName = cl1.OCT_Neo4JImport_OCT_REL_FileName

OCT_OCT_REL_s0 = cl1.OCT_OCT_REL_s0
OCT_OCT_REL_s0_code = cl1.OCT_OCT_REL_s0_code
OCT_OCT_REL_s1 = cl1.OCT_OCT_REL_s1
OCT_OCT_REL_s1_code = cl1.OCT_OCT_REL_s1_code




csv_OCT_REL=cl2.ImportCSV(OCT_Input_OCT_REL_FileName)
#print("csv_OCT_REL=\n",csv_OCT_REL)
#print(csv_OCT_REL.dtypes)
csv_OCT_REL[OCT_OCT_REL_s0] = csv_OCT_REL[OCT_OCT_REL_s0].astype(int)
csv_OCT_REL[OCT_OCT_REL_s1] = csv_OCT_REL[OCT_OCT_REL_s1].astype(int)
#print(csv_OCT_REL.dtypes)
#print("csv_OCT_REL=\n",csv_OCT_REL)
#print("")


OCT_REL_MappingRelation=cl1c.CreateMappingRelation1(csv_OCT_REL)
print("OCT_REL_MappingRelation=",OCT_REL_MappingRelation)
print("")




cl1c.Create_CSV_in_Neo4J_import(csv_OCT_REL, Neo4JImport, OCT_Neo4JImport_OCT_REL_FileName)

header_OCT_REL, csvLog_OCT_REL = cl2.LoadLog(Neo4JImport+OCT_Neo4JImport_OCT_REL_FileName)
#print("header_OCT_REL=",header_OCT_REL)
#print("")
#print("csvLog_OCT_REL=\n",csvLog_OCT_REL)
#print("")


