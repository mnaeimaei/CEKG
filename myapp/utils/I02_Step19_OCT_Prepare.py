from neo4j import GraphDatabase
import pandas as pd
import time, os, csv
import I01_funcs19_OCT_prepare as cl1c
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



print("************************** input from cl1: OCT_Node ****************************************************************************")


OCT_Input_OCT_Node_FileName = cl1.OCT_Input_OCT_Node_FileName
OCT_Neo4JImport_OCT_Node_FileName = cl1.OCT_Neo4JImport_OCT_Node_FileName

OCT_OCT_Node_conceptId = cl1.OCT_OCT_Node_conceptId
OCT_OCT_Node_ConceptCode = cl1.OCT_OCT_Node_ConceptCode
OCT_OCT_Node_termA = cl1.OCT_OCT_Node_termA
OCT_OCT_Node_termB = cl1.OCT_OCT_Node_termB
OCT_OCT_Node_semanticTags = cl1.OCT_OCT_Node_semanticTags
OCT_OCT_Node_ConceptType = cl1.OCT_OCT_Node_ConceptType
OCT_OCT_Node_Levels = cl1.OCT_OCT_Node_Levels




csv_OCT_Node=cl2.ImportCSV(OCT_Input_OCT_Node_FileName)
print("csv_OCT_Node=\n",csv_OCT_Node)
print("")

cl1c.Create_CSV_in_Neo4J_import(csv_OCT_Node, Neo4JImport, OCT_Neo4JImport_OCT_Node_FileName)

header_OCT_Node, csvLog_header_OCT_Node = cl2.LoadLog(Neo4JImport+OCT_Neo4JImport_OCT_Node_FileName)
print("header_OCT_Node=",header_OCT_Node)
print("")
print("csvLog_header_OCT_Node=\n",csvLog_header_OCT_Node)
print("")




