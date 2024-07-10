from neo4j import GraphDatabase
import pandas as pd
import time, os, csv

import A5_EntryCol_Step3_Step as cl1
import B02_base as cl2
import C01_funcs1_Log_prepare1 as cl3

print("")
print("**************************  From Entry ****************************************************************************")



driver=cl1.driver
Neo4JImport=cl2.Neo4j_import_dir(driver)
print("Neo4JImport=",Neo4JImport)


print("")
print("************************** From Event Log Entry (performance) ****************************************************************************")



Perf_file_path = cl1.Perf_file_path
print("Perf_file_path=", Perf_file_path)


cl2.create_csv_with_row(Perf_file_path)



print("")
print("************************** From Event Log Entry ****************************************************************************")

ED_dataSet =cl1.ED_dataSet
print("ED_dataSet=", ED_dataSet)



ED_Input_Event_FileName = cl1.ED_Input_Event_FileName
print("ED_Input_Event_FileName=", ED_Input_Event_FileName)

ED_Neo4JImport_Event_FileName = cl1.ED_Neo4JImport_Event_FileName
print("ED_Neo4JImport_Event_FileName=", ED_Neo4JImport_Event_FileName)



ED_eventIdTitle =cl1.ED_eventIdTitle
ED_Activity=cl1.ED_Activity
ED_ActivitySynonym=cl1.ED_ActivitySynonym
ED_Activity_Value_ID=cl1.ED_Activity_Value_ID
ED_Activity_Properties_ID=cl1.ED_Activity_Properties_ID

print("ED_eventIdTitle=", ED_eventIdTitle)
print("ED_Activity=", ED_Activity)
print("ED_ActivitySynonym=", ED_ActivitySynonym)
print("ED_Activity_Value_ID=", ED_Activity_Value_ID)
print("ED_Activity_Properties_ID=", ED_Activity_Properties_ID)

Timestamp=cl1.ED_Timestamp
print("Timestamp=", Timestamp)


ED_EnNum=int(cl1.ED_EnNum)
print("ED_EnNum=", ED_EnNum)

dicEntOrigin = cl1.dicEntOrigin
print("Entities Origin Columns (dicEntOrigin)=", dicEntOrigin)

dicEntID = cl1.dicEntID
print("Entities ID Column (dicEntID)=", dicEntID)

EntityIDColumnList=cl3.EntityIDColumnL(dicEntID, ED_EnNum)
print("EntityIDColumnList =", EntityIDColumnList)

print("")
print("************************** DF ****************************************************************************")


df=cl2.ImportCSV(ED_Input_Event_FileName)
print(df)


df2=cl3.removeDecimalInIDs(df, dicEntID, ED_EnNum)
#print(df2.to_string())

df22=cl3.removeDecimalInAct(df2, ED_Activity_Properties_ID)
#print(df22.to_string())


df3, activityTitle, Timestamp = cl3.ImportCSVRename(df2, ED_Activity, Timestamp)
#print(df3.to_string(), activityTitle, Timestamp )



cl3.Create_CSV_in_Neo4J_import(df3, Neo4JImport, ED_Neo4JImport_Event_FileName, EntityIDColumnList, ED_Activity_Properties_ID)




print("")
print("************************** Step1:  Clearing,Droping,Creating*******************************************************************")


EntityOrgValue=cl3.EntityOriginValue(df, dicEntOrigin,  ED_EnNum)
print("Entities Origin Value (EntityOrgValue) =", EntityOrgValue)

dicEnt=cl3.Entities_Alias_values (ED_EnNum, EntityOrgValue)
#print(dicEnt)
locals().update(dicEnt)
print("Entities Alias Values (dicEnt)=",dicEnt)

EntityLists=cl3.flat_list(EntityOrgValue)
print("EntityLists =", EntityLists)


print("")
print("************************** Step5:  Creating Event ****************************************************************************")


header_ED, csvLog_ED = cl2.LoadLog(Neo4JImport+ED_Neo4JImport_Event_FileName)
print("header_CE=",header_ED)
print("")
print("csvLog_header_CE=\n",csvLog_ED)
print("")



print("")
print("************************** StepC5:  Creating Entitirs ****************************************************************************")




EntityOriginIDValue=cl3.EntityOriginIDValue(df,dicEntID,  ED_EnNum)
print("EntityOriginIDValue =", EntityOriginIDValue)





model_entities_Temp=cl3.EntityAndEntityOrg_Creater_Final(dicEntOrigin,EntityOriginIDValue, dicEntID, ED_EnNum, dicEnt)
print("model_entities_Temp=",model_entities_Temp)

model_entities=cl3.model_entities(model_entities_Temp,ED_EnNum)
print("model_entities =", model_entities)



print("")
print("************************** StepC6:  Creating Activities ****************************************************************************")


actNode=cl3.activityNode(csvLog_ED,ED_Activity,ED_ActivitySynonym)
print("actNode=", actNode)

actNodeWithID=cl3.activityNodewithID(csvLog_ED,ED_Activity,ED_ActivitySynonym,ED_Activity_Properties_ID)
print("actNodeWithID=", actNodeWithID)

print("")
print("************************** StepC7: For Log-Event ****************************************************************************")




print("")
print("************************** StepC8: For Event-Entity ****************************************************************************")



print("")
print("************************** StepC9: For Event-Entity ****************************************************************************")

eventAct_Rel=cl3.eventAct_Rel(actNode,ED_Activity,ED_ActivitySynonym)
print("eventAct_Rel=", eventAct_Rel)

print("")
print("************************** StepC10: For Event-Domain ****************************************************************************")



print("")
print("************************** StepC10: For Saving Queries ****************************************************************************")



downloadDir = "../../media/download/dfgTool"
downD = os.path.realpath(downloadDir)
outDir = downD + "/" + '01_EventLog'
if not os.path.exists(outDir):
    os.mkdir(outDir)







