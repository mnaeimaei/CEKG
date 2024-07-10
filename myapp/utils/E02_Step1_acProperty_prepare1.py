from neo4j import GraphDatabase
import pandas as pd
import time, os, csv

import A5_EntryCol_Step3_Step as cl1
import B02_base as cl2
import E01_funcs1_acProperty_prepare1 as cl3


print("")


print("")
print("**************************  From Entry ****************************************************************************")


driver=cl1.driver


print("")
print("************************** From Event Log Entry (performance) ****************************************************************************")


Perf_file_path = cl1.Perf_file_path
print("Perf_file_path=", Perf_file_path)


print("**************************  From Entry ****************************************************************************")




Neo4JImport=cl2.Neo4j_import_dir(driver)
print("Neo4JImport=",Neo4JImport)

print("")
print("************************** From Property ****************************************************************************")

AcP_dataSet =cl1.AcP_dataSet

print("AcP_dataSet=", AcP_dataSet)



AcP_Input_PoNode_FileName = cl1.AcP_Input_PoNode_FileName
print("AcP_Input_PoNode_FileName=", AcP_Input_PoNode_FileName)
AcP_Neo4JImport_PoNode_FileName = cl1.AcP_Neo4JImport_PoNode_FileName
print("AcP_Neo4JImport_PoNode_FileName=", AcP_Neo4JImport_PoNode_FileName)



AcP_acID =cl1.AcP_acID
AcP_activityName=cl1.AcP_activityName
AcP_activitySynonym=cl1.AcP_activitySynonym
AcP_label=cl1.AcP_label
AcP_Value=cl1.AcP_Value
print("AcP_acID=", AcP_acID)
print("AcP_activityName=", AcP_activityName)
print("AcP_activitySynonym=", AcP_activitySynonym)
print("AcP_label=", AcP_label)
print("AcP_Value=", AcP_Value)




print("")
print("************************** From cl2 ****************************************************************************")


EnP_csv=cl2.ImportCSV(AcP_Input_PoNode_FileName)
print("EnP_csv=\n",EnP_csv)
print("")



print("")
print("************************** From Func ****************************************************************************")


cl3.Create_CSV_in_Neo4J_import(EnP_csv, Neo4JImport, AcP_Neo4JImport_PoNode_FileName)

header_EnP, csvLog_EnP = cl2.LoadLog(Neo4JImport+AcP_Neo4JImport_PoNode_FileName)
print("header_EnP=",header_EnP)
print("")
print("csvLog_EnP=\n",csvLog_EnP)
print("")

print("AcP_acID=", AcP_acID)
print("AcP_activityName=", AcP_activityName)
print("AcP_activitySynonym=", AcP_activitySynonym)
print("AcP_label=", AcP_label)
print("AcP_Value=", AcP_Value)

print("************************** input from cl1 ****************************************************************************")

acProp_1=cl3.CreatePro1(csvLog_EnP, AcP_acID, AcP_activityName, AcP_activitySynonym, AcP_label, AcP_Value)
print("acProp_1=",acProp_1)

'''
acProp_2=cl3.CreatePro2(csvLog_EnP, AcP_acID)
print("acProp_2=",acProp_2)
'''

