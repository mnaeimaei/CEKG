import os

import A1_Scenario_Step3 as sc

import A3_EntryCol_Step2_logConf_Func as entryFunc

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

fileSourceInt, value1, value2, sheetTitles=entryFunc.readtxtFiles()
print("fileSourceInt=", fileSourceInt)
print("value1=", value1)
print("value2=", value2)
print("sheetTitles=", sheetTitles)


print("##################################### General #####################################################")


if EventLog:  # Before Adding Entity

    index_of_x = sc.sheetTitleshelper.index("ED_Event_FileName")
    ED_Event_FileName = sheetTitles[index_of_x]  # C_Log

    openingPath0 = confPath + "/4_eventLogDefault.txt"


    openingPath1 = confPath + "/4_eventLogNumber1.txt"
    savingPath = confPath + "/4_eventLogDefaultValue1.txt"
    valueList1=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList1=",valueList1)

    openingPath2 = confPath + "/4_eventLogNumber2.txt"
    savingPath2 = confPath + "/4_eventLogDefaultValue2.txt"
    valueList2=entryFunc.DefaultValueEventLog(openingPath2, openingPath0, savingPath2)
    print("valueList2=", valueList2)

    FilePath = confPath + "/" + ED_Event_FileName + "_conf.txt"
    valueList1.update(valueList2)
    print("valueList1=", valueList1)
    entryFunc.SaveDic(FilePath, valueList1,"EventLog")





if otherEntities == True:
    index_of_x1 = sc.sheetTitleshelper.index("EnP_PoNode_FileName_1")
    EnP_PoNode_FileName_1 = sheetTitles[index_of_x1]  # C_Log


    openingPath0 = confPath + "/5_otherEntitiesDefault.txt"


    openingPath1 = confPath + "/5_otherEntitiesNumber.txt"
    savingPath = confPath + "/5_otherEntitiesDefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + EnP_PoNode_FileName_1 + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")




if otherEntitiesRel == True:
    index_of_x2 = sc.sheetTitleshelper.index("EnP_PoNode_FileName_2")
    EnP_PoNode_FileName_2 = sheetTitles[index_of_x2]  # C_Log

    openingPath0 = confPath + "/6_otherEntitiesRelDefault.txt"


    openingPath1 = confPath + "/6_otherEntitiesRelNumber.txt"
    savingPath = confPath + "/6_otherEntitiesRelDefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + EnP_PoNode_FileName_2 + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")


if acProperties:
    index_of_x = sc.sheetTitleshelper.index("AcP_PoNode_FileName")
    AcP_PoNode_FileName = sheetTitles[index_of_x]  # C_Log

    openingPath0 = confPath + "/7_acPropertiesDefault.txt"


    openingPath1 = confPath + "/7_acPropertiesNumber.txt"
    savingPath = confPath + "/7_acPropertiesDefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + AcP_PoNode_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")

if Domain:
    index_of_x = sc.sheetTitleshelper.index("ACT_PoNode_FileName")
    ACT_PoNode_FileName = sheetTitles[index_of_x]  # C_Log

    openingPath0 = confPath + "/8_domainEntitiesDefault.txt"


    openingPath1 = confPath + "/8_domainNumber.txt"
    savingPath = confPath + "/8_domainDefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + ACT_PoNode_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")


if ICD:
    index_of_x = sc.sheetTitleshelper.index("CE_PoNode_FileName")
    CE_PoNode_FileName = sheetTitles[index_of_x]  # C_Log

    openingPath0 = confPath + "/9_icdDefault.txt"


    openingPath1 = confPath + "/9_icdNumber.txt"
    savingPath = confPath + "/9_icdDefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + CE_PoNode_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")



if octNode == True:
    index_of_x1 = sc.sheetTitleshelper.index("OCT_OCT_Node_FileName")
    OCT_OCT_Node_FileName = sheetTitles[index_of_x1]  # C_Log

    openingPath0 = confPath + "/10_octNodeDefault.txt"


    openingPath1 = confPath + "/10_octNodeNumber.txt"
    savingPath = confPath + "/10_octNodeDefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + OCT_OCT_Node_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")




if octRel == True:
    index_of_x2 = sc.sheetTitleshelper.index("OCT_OCT_REL_FileName")
    OCT_OCT_REL_FileName = sheetTitles[index_of_x2]  # C_Log

    openingPath0 = confPath + "/11_octRelDefault.txt"


    openingPath1 = confPath + "/11_octRelNumber.txt"
    savingPath = confPath + "/11_octRelDefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + OCT_OCT_REL_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")



if DK1:
    index_of_x = sc.sheetTitleshelper.index("DK1_EnPo_FileName")
    DK1_EnPo_FileName = sheetTitles[index_of_x]  # C_Log

    openingPath0 = confPath + "/12_dk1Default.txt"


    openingPath1 = confPath + "/12_dk1Number.txt"
    savingPath = confPath + "/12_dk1DefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + DK1_EnPo_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")



if DK2:
    index_of_x = sc.sheetTitleshelper.index("DK2_EnPo_FileName")
    DK2_EnPo_FileName = sheetTitles[index_of_x]  # C_Log

    openingPath0 = confPath + "/13_dk2Default.txt"


    openingPath1 = confPath + "/13_dk2Number.txt"
    savingPath = confPath + "/13_dk2DefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + DK2_EnPo_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")


if DK3:
    index_of_x = sc.sheetTitleshelper.index("DK3_Potential_DK3_FileName")
    DK3_Potential_DK3_FileName = sheetTitles[index_of_x]  # C_Log

    openingPath0 = confPath + "/14_dk3Default.txt"


    openingPath1 = confPath + "/14_dk3Number.txt"
    savingPath = confPath + "/14_dk3DefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + DK3_Potential_DK3_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")

if DK4:
    index_of_x = sc.sheetTitleshelper.index("DK4_ICD_OCT_FileName")
    DK4_ICD_OCT_FileName = sheetTitles[index_of_x]  # C_Log

    openingPath0 = confPath + "/15_dk4Default.txt"


    openingPath1 = confPath + "/15_dk4Number.txt"
    savingPath = confPath + "/15_dk4DefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + DK4_ICD_OCT_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")


if DK5:
    index_of_x = sc.sheetTitleshelper.index("DK5_FileName")
    DK5_FileName = sheetTitles[index_of_x]  # C_Log

    openingPath0 = confPath + "/16_dk5Default.txt"


    openingPath1 = confPath + "/16_dk5Number.txt"
    savingPath = confPath + "/16_dk5DefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + DK5_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")


if DK6_1 == True:
    index_of_x1 = sc.sheetTitleshelper.index("Domain_FileName_1")
    Domain_FileName_1 = sheetTitles[index_of_x1]  # C_Log

    openingPath0 = confPath + "/17_dk61Default.txt"


    openingPath1 = confPath + "/17_dk61Number.txt"
    savingPath = confPath + "/17_dk61DefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + Domain_FileName_1 + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")



if DK6_2 == True:
    index_of_x2 = sc.sheetTitleshelper.index("Domain_FileName_2")
    Domain_FileName_2 = sheetTitles[index_of_x2]  # C_Log

    openingPath0 = confPath + "/18_dk62Default.txt"


    openingPath1 = confPath + "/18_dk62Number.txt"
    savingPath = confPath + "/18_dk62DefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + Domain_FileName_2 + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")



if DK7:
    index_of_x = sc.sheetTitleshelper.index("DK7_Activity_DK7_FileName")
    DK7_Activity_DK7_FileName = sheetTitles[index_of_x]  # C_Log


    openingPath0 = confPath + "/19_dk7Default.txt"


    openingPath1 = confPath + "/19_dk7Number.txt"
    savingPath = confPath + "/19_dk7DefaultValue.txt"
    valueList=entryFunc.DefaultValue(openingPath1, openingPath0, savingPath)
    print("valueList=",valueList)

    FilePath = confPath + "/" + DK7_Activity_DK7_FileName + "_conf.txt"
    entryFunc.SaveDic(FilePath, valueList,"EventLog")


