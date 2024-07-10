from neo4j import GraphDatabase
import pandas as pd
import time, os, csv

import A5_EntryCol_Step3_Step as cl1


import A1_Scenario_Step2 as Ne0
import A6_Scenario_Final_Step as Ne02
import Q01_funcs_DFG_prepare_Scneario as cl3

import B02_txt_read as txtRead



print("************************** Entry from cl1 ****************************************************************************")

driver=cl1.driver


print("")
print("************************** From Event Log Entry (performance) ****************************************************************************")


Perf_file_path = cl1.Perf_file_path
print("Perf_file_path=", Perf_file_path)





print("************************** Entry from clO ****************************************************************************")

entityList=Ne02.entityList
print("entityList=", entityList)

entityListIDproperty=Ne02.entityListIDproperty
print("entityListIDproperty=", entityListIDproperty)

conditionProperty=Ne02.conditionProperty
print("conditionProperty=", conditionProperty)

conditionPropertyValue=Ne02.conditionPropertyValue
print("conditionPropertyValue=", conditionPropertyValue)


ED_EnNum=len(entityList)
print("ED_EnNum=", ED_EnNum)





print("************************** Entry from cl6 ****************************************************************************")



EntityOriginIDValue=cl3.Finading_Entities_ID(driver,entityList,entityListIDproperty, conditionProperty, conditionPropertyValue)
print("EntityOriginIDValue=",EntityOriginIDValue)

EntityOrgValue=cl3.convert_to_list_of_lists(entityList)
print("EntityOrgValue=",EntityOrgValue)

dicEnt=cl3.Entities_Alias_values (ED_EnNum, EntityOrgValue)
#print(dicEnt)
locals().update(dicEnt)
print("dicEnt=",dicEnt)

EntityOriginValueTemp=cl3.EntityOriginValue_Temp(EntityOrgValue,  ED_EnNum)
print("EntityOriginValueTemp =", EntityOriginValueTemp)


dicNumEntOrgAbr=cl3.NumberEntityOriginAbr(EntityOriginValueTemp, ED_EnNum)
# print(dicNumEntTypeAbr)
locals().update(dicNumEntOrgAbr)
print("dicNumEntOrgAbr=", dicNumEntOrgAbr)



dicEntAliasAbr=cl3.EntityAliasAbr(dicEnt, dicNumEntOrgAbr, ED_EnNum)
# print(dicNumEntTypeAbr)
locals().update(dicEntAliasAbr)
print("dicEntAliasAbr=", dicEntAliasAbr)

model_entities_Temp=cl3.EntityAndEntityOrg_Creater_Final(EntityOriginIDValue, ED_EnNum, dicEnt,dicEntAliasAbr)
print("model_entities_Temp=",model_entities_Temp)

model_entities=cl3.model_entities(model_entities_Temp,ED_EnNum)
print("model_entities =", model_entities)

EntityIDValueOrdered=cl3.Finading_ID_List(driver,entityList,entityListIDproperty, conditionProperty, conditionPropertyValue)
print("EntityIDValueOrdered=",EntityIDValueOrdered)

EntityIDValueOrdered_pair=cl3.create_adjacent_pairs(EntityIDValueOrdered,ED_EnNum)
print("EntityIDValueOrdered_pair=",EntityIDValueOrdered_pair)

model_entities_derived, model_entities_derived_Temp = cl3.pair_memebr2(EntityIDValueOrdered_pair,ED_EnNum,dicEntAliasAbr)
print("model_entities_derived = " , model_entities_derived)
print("model_entities_derived_Temp = " , model_entities_derived_Temp)


model_relations=cl3.model_relations(model_entities_derived_Temp, EntityOrgValue,  ED_EnNum, dicEnt, dicEntAliasAbr)
print("model_relations = ",model_relations)

print("")
print("************************** Changing Dataset ****************************************************************************")



idColumnAndValue=cl3.idColumnAndValueMaler(entityList, EntityOriginIDValue, ED_EnNum)
print("idColumnAndValue =", idColumnAndValue)



print("")
print("**************************  ****************************************************************************")

EntityIDValueOrdered = cl3.Finading_ID_List(driver, entityList, entityListIDproperty, conditionProperty,
                                                 conditionPropertyValue)
# print("EntityIDValueOrdered=", EntityIDValueOrdered)

EntityIDValueOrdered_pair = cl3.create_adjacent_pairs(EntityIDValueOrdered, ED_EnNum)
# print("EntityIDValueOrdered_pair=", EntityIDValueOrdered_pair)

model_entities_derived, model_entities_derived_Temp = cl3.pair_memebr2(EntityIDValueOrdered_pair, ED_EnNum,
                                                                            dicEntAliasAbr)
# print("model_entities_derived = ", model_entities_derived)
# print("model_entities_derived_Temp = ", model_entities_derived_Temp)
include_entities = cl3.include_entities(EntityOrgValue, model_entities_derived_Temp, ED_EnNum)
# print("include_entities =", include_entities)


include_DF1 = cl3.include_DF1(EntityOrgValue, model_entities_derived_Temp, ED_EnNum)
# print("include_DF1 =", include_DF1)
include_DF2 = cl3.include_DF2(EntityOrgValue, model_entities_derived_Temp, ED_EnNum)
# print("include_DF2 =", include_DF2)
include_DF = include_DF1 + include_DF2
# print("include_DF =", include_DF)



print("")
print("************************** DFG_3: Defualt ****************************************************************************")

Dfg3_existance=cl3.txtExistanceQ("DFG3_config")

if Dfg3_existance==False:
    status=11
    Final_AG_All = EntityOrgValue
    print("Final_AG_All=",Final_AG_All)

    Final_AG_All_ID = []
    print("Final_AG_All_ID=", Final_AG_All_ID)

else:

    Type3 = cl3.TypeCount("DFG3_config", "Type3")
    print("Type3=", Type3)

    Type3_non_Relative_selection = cl3.TrueFalseTxt("DFG3_config", "Type3_non_Relative_selection")
    print("Type3_non_Relative_selection=", Type3_non_Relative_selection)

    Type3_non_Relative_selection_ID_instances = cl3.listIntTxt("DFG3_config", "Type3_non_Relative_selection_ID_instances")
    print("Type3_non_Relative_selection_ID_instances=", Type3_non_Relative_selection_ID_instances)

    if Type3==1:
        status = 22
        Final_AG_All = EntityOrgValue
        print("Final_AG_All=", Final_AG_All)

        Final_AG_All_ID = []
        print("Final_AG_All_ID=", Final_AG_All_ID)


    if Type3==2 and Type3_non_Relative_selection==False:
        status = 33
        Final_AG_All = cl3.entity_basedon_column(ED_EnNum, EntityOrgValue, model_entities_derived_Temp)
        print("Final_AG_All=", Final_AG_All)
        Final_AG_All_ID = Type3_non_Relative_selection_ID_instances
        print("Final_AG_All_ID=", Final_AG_All_ID)

    if Type3==2 and Type3_non_Relative_selection==True:
        status = 44
        Final_AG_All = EntityOrgValue
        print("Final_AG_All=", Final_AG_All)
        Final_AG_All_ID = Type3_non_Relative_selection_ID_instances
        print("Final_AG_All_ID=", Final_AG_All_ID)




print("")
print("************************** DFG5_Relative: Default ****************************************************************************")

Dfg5_existance=cl3.txtExistanceQ("DFG5_config")


if Dfg5_existance==False:
    #status=11
    random_entity = cl3.select_two_random_items(entityList)
    # print("random_entity:", random_entity)

    Type5_Rel_1_DF_Show_Random = random_entity[0]
    Type5_Rel_2_DF_Show_Random = random_entity[1]

    print("Type5_Rel_1_DF_Show_Random=", Type5_Rel_1_DF_Show_Random)
    print("Type5_Rel_2_DF_Show_Random=", Type5_Rel_2_DF_Show_Random)

else:
    #status = 12
    Type5_Rel_1_DF_Show_Random = cl3.stringTxt("DFG5_config", "Type5_Rel_1_DF_Show")
    print("Type5_Rel_1_DF_Show_Random=", Type5_Rel_1_DF_Show_Random)

    Type5_Rel_2_DF_Show_Random = cl3.stringTxt("DFG5_config", "Type5_Rel_2_DF_Show")
    print("Type5_Rel_2_DF_Show_Random=", Type5_Rel_2_DF_Show_Random)


Final_AG_New=cl3.Final_AG_forListID(Type5_Rel_1_DF_Show_Random, Type5_Rel_2_DF_Show_Random,idColumnAndValue)
print("Final_AG_New=",Final_AG_New)


print("")
print("************************** DFG_6: ****************************************************************************")

node1=cl3.node1Finder(driver)
print("node1=",node1)

nodeLast=cl3.nodeLastFinder(driver)
print("nodeLast=",nodeLast)

otherNodes=cl3.otherLastFinder(driver)
print("otherNodes=",otherNodes)

maxLength=cl3.maxLengthFinder(driver)
print("maxLength=",maxLength)


nodeOther=cl3.node3Finder(driver,node1, nodeLast,maxLength)
print("nodeOther=",nodeOther)

converted_list=cl3.converted_lister(nodeOther)
print("converted_list=",converted_list)


pathNode=cl3.pathFinder(converted_list)
print("pathNode=",pathNode)

excludedNode=cl3.nodeExcluder(driver)
print("excludedNode=",excludedNode)

nodeReal=cl3.creatingDfFromGraph(driver,pathNode,excludedNode)
print("nodeReal=",nodeReal)





