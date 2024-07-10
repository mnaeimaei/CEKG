from neo4j import GraphDatabase
import pandas as pd
import time, os, csv
import F01_funcs13_Domain_prepare as cl1b
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


ACT_Input_PoNode_FileName = cl1.ACT_Input_PoNode_FileName
print(ACT_Input_PoNode_FileName)
ACT_Neo4JImport_PoNode_FileName = cl1.ACT_Neo4JImport_PoNode_FileName


ACT_Domain = cl1.ACT_Domain
print("ACT_Domain=", ACT_Domain)



csv_ACT=cl2.ImportCSV(ACT_Input_PoNode_FileName)
print("csv_ACT=\n",csv_ACT)
print("")

cl1b.Create_CSV_in_Neo4J_import(csv_ACT, Neo4JImport, ACT_Neo4JImport_PoNode_FileName)

header_ACT, csvLog_header_ACT = cl2.LoadLog(Neo4JImport+ACT_Neo4JImport_PoNode_FileName)
print("header_ACT=",header_ACT)
print("")
print("csvLog_header_ACT=\n",csvLog_header_ACT)
print("")


print("************************** input from cl1 ****************************************************************************")

domainNode=cl1b.domainNode(csvLog_header_ACT)
print("domainNode=",domainNode)

