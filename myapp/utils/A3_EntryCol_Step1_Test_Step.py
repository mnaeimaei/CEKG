import os

import A1_Scenario_Step3 as sc

import A3_EntryCol_Step1_Test_Func as entryFunc

EventLog=sc.EventLog
otherEntities=sc.otherEntities
otherEntitiesRel=sc.otherEntitiesRel
acProperties=sc.acProperties
Domain=sc.Domain
ICD=sc.ICD
octNode=sc.octNode
octRel=sc.octRel


DK1=sc.DK1
DK2=sc.DK2
DK3=sc.DK3
DK4=sc.DK4
DK5=sc.DK5
DK6_1=sc.DK6_1
DK6_2=sc.DK6_2
DK7=sc.DK7



print("##################################### General #####################################################")





confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)






print("************************** Step3 ****************************************************************************")



if EventLog:  # Before Adding Entity

    savingPath = confPath + "/4_eventLogDefault.txt"


    goalList = ["ED_eventIdTitle", "ED_Activity", "ED_ActivitySynonym", "ED_Timestamp", "ED_Activity_Value_ID",
                 "ED_Activity_Properties_ID"]

    colValue = ["Event", "Activity", "Activity_Synonym", "timestamp", "Activity_Value_ID",
                 "Activity_Properties_ID"]

    entryFunc.modifyDefault(savingPath, goalList,colValue)

    EntityNumber=entryFunc.EventLog_EntityFinder(savingPath)
    print("EntityNumber=", EntityNumber)


    optionPath = confPath + "/4_eventLogOption.txt"

    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)


    entryFunc.EventLog_func(savingPath,EntityNumber,options)


if otherEntities == True:

    savingPath = confPath + "/5_otherEntitiesDefault.txt"
    goalList=["EnP_Origin","EnP_ID","EnP_Name","EnP_Value","EnP_Category"]


    optionPath = confPath + "/5_otherEntitiesOption.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)

if otherEntitiesRel == True:

    savingPath = confPath + "/6_otherEntitiesRelDefault.txt"
    goalList = ["EnP_Entity_Origin1", "EnP_Entity_ID1", "EnP_Entity_Origin2", "EnP_Entity_ID2"]

    optionPath = confPath + "/6_otherEntitiesRelOption.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)


if acProperties:

    savingPath = confPath + "/7_acPropertiesDefault.txt"
    goalList = ["AcP_acID", "AcP_activityName", "AcP_activitySynonym", "AcP_label", "AcP_Value"]

    optionPath = confPath + "/7_acPropertiesOption.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)


if Domain:

    savingPath = confPath + "/8_domainEntitiesDefault.txt"
    goalList = ["ACT_Domain"]

    optionPath = confPath + "/8_domainOption.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)



if ICD:

    savingPath = confPath + "/9_icdDefault.txt"
    goalList = ["CE_ClinicalEntity", "CE_icd_code", "CE_icd_version", "CE_icd_code_title"]

    optionPath = confPath + "/9_icdOption.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)



if octNode == True:

    savingPath = confPath + "/10_octNodeDefault.txt"
    goalList = ["OCT_OCT_Node_conceptId", "OCT_OCT_Node_ConceptCode", "OCT_OCT_Node_termA", "OCT_OCT_Node_termB",
                "OCT_OCT_Node_semanticTags", "OCT_OCT_Node_ConceptType", "OCT_OCT_Node_Levels"]

    optionPath = confPath + "/10_octNodeOption.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)




if octRel == True:

    savingPath = confPath + "/11_octRelDefault.txt"
    goalList = ["OCT_OCT_REL_s0", "OCT_OCT_REL_s0_code", "OCT_OCT_REL_s1", "OCT_OCT_REL_s1_code"]

    optionPath = confPath + "/11_octRelOption.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)



if DK1:

    savingPath = confPath + "/12_dk1Default.txt"
    goalList = ["DK1_XXXX"]

    optionPath = confPath + "/12_dk1Option.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)



if DK2:

    savingPath = confPath + "/13_dk2Default.txt"
    goalList = ["DK2_XXXX"]

    optionPath = confPath + "/13_dk2Option.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)



if DK3:

    savingPath = confPath + "/14_dk3Default.txt"
    goalList = ["DK3_Disorders", "DK3_icd_code"]

    optionPath = confPath + "/14_dk3Option.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)


if DK4:

    savingPath = confPath + "/15_dk4Default.txt"
    goalList = ["DK4_icd_code", "DK4_OTC"]

    optionPath = confPath + "/15_dk4Option.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)


if DK5:

    savingPath = confPath + "/16_dk5Default.txt"
    goalList = ["DK5_Activity", "DK5_Activity_Synonym", "DK5_OTC", "DK5_SCTCode"]

    optionPath = confPath + "/16_dk5Option.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)



if DK6_1 == True:

    savingPath = confPath + "/17_dk61Default.txt"
    goalList = ["Domain1_Activity", "Domain1_Activity_Synonym", "Domain1_Domain"]

    optionPath = confPath + "/17_dk61Option.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)



if DK6_2 == True:

    savingPath = confPath + "/18_dk62Default.txt"
    goalList = ["Domain2_Domain", "Domain2_OTC", "Domain2_SCTCode"]

    optionPath = confPath + "/18_dk62Option.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)



if DK7:

    savingPath = confPath + "/19_dk7Default.txt"
    goalList = ["DK7_Activity_Value_ID", "DK7_Disorders"]

    optionPath = confPath + "/19_dk7Option.txt"
    options=entryFunc.Others_func_first(optionPath)
    print("options=", options)

    entryFunc.modifyDefault(savingPath, goalList,options)



