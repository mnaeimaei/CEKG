from neo4j import GraphDatabase
import pandas as pd
import time, os, csv

import D09_funcs1_enRel_prepare3 as cl3
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


print("************************** DF 1 ****************************************************************************")

df1=cl3.creatingDfFromGraph(driver)
print("\ndf1=\n",df1)

dfWithRankingAdmission=cl3.rankingAdm(df1)
print("\ndfWithRankingAdmission=\n",dfWithRankingAdmission)

df1Disorders=cl3.groupingDisorder(df1)
print("\ndf1Disorders=\n",df1Disorders)

finalTable=cl3.lefJoinTable(df1Disorders, dfWithRankingAdmission)
print("\nfinalTable=\n",finalTable)

dfComparable=cl3.comparing(finalTable)
print("\ndfComparable=\n",dfComparable)

print("************************** DF 2 ****************************************************************************")

dfComparable=cl3.comparing(finalTable)
print("\ndfComparable=\n",dfComparable)

dfFinal=cl3.createFinal(dfComparable)
print("\ndfFinal=\n",dfFinal)

Treated=cl3.createTreated(dfFinal,"Treated")
print("\nTreated=\n",Treated)


NotTreated=cl3.createTreated(dfFinal,"New")
print("\nNotTreated=\n",NotTreated)


New=cl3.createTreated(dfFinal,"notTreated")
print("\nNew=\n",New)

print("************************** DF 3 ****************************************************************************")

multiMorbidityValue=cl3.multiDis(finalTable)
print("multiMorbidityValue=",multiMorbidityValue)

treatedValue=cl3.treatVal(dfFinal)
print("treatedValue=",treatedValue)


notTreatedValue=cl3.notVal(dfFinal)
print("notTreatedValue=",notTreatedValue)

newValue=cl3.newVal(dfFinal)
print("newValue=",newValue)