from neo4j import GraphDatabase
import pandas as pd
import time, os, csv

import D05_funcs1_enRel_prepare2 as cl3
import B02_base as cl2
import A5_EntryCol_Step3_Step as cl1




print("")


print("")
print("**************************  From Entry ****************************************************************************")


driver=cl1.driver


print("")
print("************************** From Event Log Entry (performance) ****************************************************************************")


Perf_file_path = cl1.Perf_file_path
print("Perf_file_path=", Perf_file_path)

EnP_dataSet =cl1.EnP_dataSet
print("EnP_dataSet=", EnP_dataSet)



print("**************************  From Entry ****************************************************************************")




Neo4JImport=cl2.Neo4j_import_dir(driver)
print("Neo4JImport=",Neo4JImport)


print("")
print("************************** From Nodes ****************************************************************************")

EnP_Input_PoNode_FileName_2 = cl1.EnP_Input_PoNode_FileName_2
print("EnP_Input_PoNode_FileName_2=", EnP_Input_PoNode_FileName_2)
EnP_Neo4JImport_PoNode_FileName_2 = cl1.EnP_Neo4JImport_PoNode_FileName_2
print("EnP_Neo4JImport_PoNode_FileName_2=", EnP_Neo4JImport_PoNode_FileName_2)

EnP_Rel_csv=cl2.ImportCSV(EnP_Input_PoNode_FileName_2)
#print("EnP_Rel_csv=\n",EnP_Rel_csv)
print("")

cl3.Create_CSV_in_Neo4J_import(EnP_Rel_csv, Neo4JImport, EnP_Neo4JImport_PoNode_FileName_2)

header_EnP_REL, csvLog_EnP_REL = cl2.LoadLog(Neo4JImport+EnP_Neo4JImport_PoNode_FileName_2)
print("header_EnP_REL=",header_EnP_REL)
print("")
#print("csvLog_EnP_REL=\n",csvLog_EnP_REL)
print("")


EnP_Entity_Origin1 =cl1.EnP_Entity_Origin1
EnP_Entity_ID1=cl1.EnP_Entity_ID1
EnP_Entity_Origin2=cl1.EnP_Entity_Origin2
EnP_Entity_ID2=cl1.EnP_Entity_ID2
print("EnP_Entity_Origin1=", EnP_Entity_Origin1)
print("EnP_Entity_ID1=", EnP_Entity_ID1)
print("EnP_Entity_Origin2=", EnP_Entity_Origin2)
print("EnP_Entity_ID2=", EnP_Entity_ID2)



print("************************** input from cl1 ****************************************************************************")



RelList=cl3.CreateLoL(csvLog_EnP_REL)
print("RelList=",RelList)

RelFinal=cl3.ListMaker(RelList)
print("RelFinal=",RelFinal)

