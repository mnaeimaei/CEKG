from neo4j import GraphDatabase
import pandas as pd
import time, os, csv

import D01_funcs1_otherEntities_prepare1 as cl3
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

EnP_Input_PoNode_FileName_1 = cl1.EnP_Input_PoNode_FileName_1
print("EnP_Input_PoNode_FileName_1=", EnP_Input_PoNode_FileName_1)
EnP_Neo4JImport_PoNode_FileName_1 = cl1.EnP_Neo4JImport_PoNode_FileName_1
print("EnP_Neo4JImport_PoNode_FileName_1=", EnP_Neo4JImport_PoNode_FileName_1)

EnP_Node_csv=cl2.ImportCSV(EnP_Input_PoNode_FileName_1)
#print("EnP_Node_csv=\n",EnP_Node_csv)
print("")

cl3.Create_CSV_in_Neo4J_import(EnP_Node_csv, Neo4JImport, EnP_Neo4JImport_PoNode_FileName_1)


header_EnP_Node, csvLog_EnP_Node = cl2.LoadLog(Neo4JImport+EnP_Neo4JImport_PoNode_FileName_1)
print("header_EnP_Node=",header_EnP_Node)
print("")
#print("csvLog_EnP_Node=\n",csvLog_EnP_Node)
print("")


EnP_Origin =cl1.EnP_Origin
EnP_ID=cl1.EnP_ID
EnP_Name=cl1.EnP_Name
EnP_Value=cl1.EnP_Value
EnP_Category=cl1.EnP_Category
print("EnP_Origin=", EnP_Origin)
print("EnP_ID=", EnP_ID)
print("EnP_Name=", EnP_Name)
print("EnP_Value=", EnP_Value)
print("EnP_Category=", EnP_Category)



print("************************** input from cl1 ****************************************************************************")

NodeList=cl3.CreateLoL(csvLog_EnP_Node)
print("NodeList=",NodeList)


NodeEntity=cl3.CreateEntity(NodeList)
print("NodeEntity=",NodeEntity)

