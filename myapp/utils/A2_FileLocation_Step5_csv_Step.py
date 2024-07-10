import os
import csv

import A2_FileLocation_Step5_csv_Func as fileFunc

print("#################################### updating default value ##########################################")

confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)

openingPath1 = confPath + "/3_previewNumberOfQuestions.txt"
openingPath2 = confPath + "/3_previewDefault.txt"
savingPath = confPath + "/3_previewDefaultValue.txt"


fileFunc.DefaultValue(openingPath1, openingPath2, savingPath)

print("#################################### creatingConf3 ##################################################")

confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)
open_FilePath= confPath + "/3_previewDefaultValue.txt"
save_FilePath= confPath + "/3_previewXConf.txt"

fileFunc.conf3creation(open_FilePath,save_FilePath)


print("#################################### creatingConf3 ##################################################")


import A1_Scenario_Step3 as sc

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


confDirectory = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)

sheetTitles=fileFunc.readtxtFiles()
print("sheetTitles=", sheetTitles)



excelDirectory = '../../media/uploads/0_Data/EventLog.xlsx'
excelPath = os.path.realpath(excelDirectory)
print("excelPath=",excelPath)


print("#################################### savingCSV ##################################################")


if EventLog:  # Before Adding Entity

    index_of_x = sc.sheetTitleshelper.index("ED_Event_FileName")
    ED_Event_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(ED_Event_FileName, excelPath)

    savingPath1 = confPath + "/4_eventLogOption.txt"
    savingPathMap = confPath + "/4_eventLogMapping.txt"


    eventLogOptions = fileFunc.get_column_from_csv(ED_Event_FileName ,savingPath1,savingPathMap)


    savingPath2 = confPath + "/4_eventLogDefault.txt"
    fileFunc.DefaultSplit1(savingPath2, eventLogOptions[0])

    savingPath3 = confPath + "/4_eventLogNumber1.txt"
    fileFunc.tagNumber1(savingPath3)

    savingPath4 = confPath + "/4_eventLogNumber2.txt"
    fileFunc.tagNumber1b(savingPath4,20)

    savingPath5 = confPath + "/4_eventLogDefaultValue1.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)


    savingPath6 = confPath + "/4_eventLogDefaultValue2.txt"
    fileFunc.DefaultValue2(savingPath4, savingPath2, savingPath6,eventLogOptions[0],20)


if otherEntities == True:
    index_of_x1 = sc.sheetTitleshelper.index("EnP_PoNode_FileName_1")
    EnP_PoNode_FileName_1 = sheetTitles[index_of_x1]  # C_Log

    fileFunc.saveASCSV(EnP_PoNode_FileName_1, excelPath)

    savingPath1 = confPath + "/5_otherEntitiesOption.txt"
    savingPathMap = confPath + "/5_otherEntitiesMapping.txt"
    Options = fileFunc.get_column_from_csv(EnP_PoNode_FileName_1 ,savingPath1,savingPathMap)


    savingPath2 = confPath + "/5_otherEntitiesDefault.txt"
    fileFunc.DefaultSplit2(savingPath2, Options[0])


    savingPath3 = confPath + "/5_otherEntitiesNumber.txt"
    fileFunc.tagNumber2(savingPath3)


    savingPath5 = confPath + "/5_otherEntitiesDefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)



    
if otherEntitiesRel == True:

    index_of_x2 = sc.sheetTitleshelper.index("EnP_PoNode_FileName_2")
    EnP_PoNode_FileName_2 = sheetTitles[index_of_x2]  # C_Log

    fileFunc.saveASCSV(EnP_PoNode_FileName_2, excelPath)
    
    
    savingPath1 = confPath + "/6_otherEntitiesRelOption.txt"
    savingPathMap = confPath + "/6_otherEntitiesMapping.txt"
    Options = fileFunc.get_column_from_csv(EnP_PoNode_FileName_2 ,savingPath1,savingPathMap)
    
    
    savingPath2 = confPath + "/6_otherEntitiesRelDefault.txt"
    fileFunc.DefaultSplit3(savingPath2, Options[0])
    
    savingPath3 = confPath + "/6_otherEntitiesRelNumber.txt"
    fileFunc.tagNumber3(savingPath3)
    
    
    savingPath5 = confPath + "/6_otherEntitiesRelDefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)




if acProperties:
    index_of_x = sc.sheetTitleshelper.index("AcP_PoNode_FileName")
    AcP_PoNode_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(AcP_PoNode_FileName, excelPath)
    
    
    savingPath1 = confPath + "/7_acPropertiesOption.txt"
    savingPathMap = confPath + "/7_acPropertiesMapping.txt"
    Options = fileFunc.get_column_from_csv(AcP_PoNode_FileName ,savingPath1,savingPathMap)
    
    
    savingPath2 = confPath + "/7_acPropertiesDefault.txt"
    fileFunc.DefaultSplit4(savingPath2, Options[0])
    
    savingPath3 = confPath + "/7_acPropertiesNumber.txt"
    fileFunc.tagNumber4(savingPath3)
    
    savingPath5 = confPath + "/7_acPropertiesDefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)





if Domain:
    index_of_x = sc.sheetTitleshelper.index("ACT_PoNode_FileName")
    ACT_PoNode_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(ACT_PoNode_FileName, excelPath)
    
    
    savingPath1 = confPath + "/8_domainOption.txt"
    savingPathMap = confPath + "/8_domainMapping.txt"
    Options = fileFunc.get_column_from_csv(ACT_PoNode_FileName ,savingPath1,savingPathMap)

    savingPath2 = confPath + "/8_domainEntitiesDefault.txt"
    fileFunc.DefaultSplit5(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/8_domainNumber.txt"
    fileFunc.tagNumber5(savingPath3)

    savingPath5 = confPath + "/8_domainDefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)


if ICD:
    index_of_x = sc.sheetTitleshelper.index("CE_PoNode_FileName")
    CE_PoNode_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(CE_PoNode_FileName, excelPath)
    
    savingPath1 = confPath + "/9_icdOption.txt"
    savingPathMap = confPath + "/9_icdOptionMapping.txt"
    Options = fileFunc.get_column_from_csv(CE_PoNode_FileName ,savingPath1,savingPathMap)
    
    savingPath2 = confPath + "/9_icdDefault.txt"
    fileFunc.DefaultSplit6(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/9_icdNumber.txt"
    fileFunc.tagNumber6(savingPath3)

    savingPath5 = confPath + "/9_icdDefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)


if octNode == True :
    index_of_x1 = sc.sheetTitleshelper.index("OCT_OCT_Node_FileName")
    OCT_OCT_Node_FileName = sheetTitles[index_of_x1]  # C_Log


    fileFunc.saveASCSV(OCT_OCT_Node_FileName, excelPath)
    
    savingPath1 = confPath + "/10_octNodeOption.txt"
    savingPathMap = confPath + "/10_octNodeMapping.txt"
    Options = fileFunc.get_column_from_csv(OCT_OCT_Node_FileName ,savingPath1,savingPathMap)
    
    savingPath2 = confPath + "/10_octNodeDefault.txt"
    fileFunc.DefaultSplit7(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/10_octNodeNumber.txt"
    fileFunc.tagNumber7(savingPath3)

    savingPath5 = confPath + "/10_octNodeDefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)
    
if octRel == True:

    index_of_x2 = sc.sheetTitleshelper.index("OCT_OCT_REL_FileName")
    OCT_OCT_REL_FileName = sheetTitles[index_of_x2]  # C_Log

    fileFunc.saveASCSV(OCT_OCT_REL_FileName, excelPath)
    
    savingPath1 = confPath + "/11_octRelOption.txt"
    savingPathMap = confPath + "/11_octRelMapping.txt"
    Options = fileFunc.get_column_from_csv(OCT_OCT_REL_FileName ,savingPath1,savingPathMap)
    
    savingPath2 = confPath + "/11_octRelDefault.txt"
    fileFunc.DefaultSplit8(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/11_octRelNumber.txt"
    fileFunc.tagNumber8(savingPath3)


    savingPath5 = confPath + "/11_octRelDefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)



if DK1:
    index_of_x = sc.sheetTitleshelper.index("DK1_EnPo_FileName")
    DK1_EnPo_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(DK1_EnPo_FileName, excelPath)
    
    savingPath1 = confPath + "/12_dk1Option.txt"
    savingPathMap = confPath + "/12_dk1Mapping.txt"
    Options = fileFunc.get_column_from_csv(DK1_EnPo_FileName ,savingPath1,savingPathMap)
    
    savingPath2 = confPath + "/12_dk1Default.txt"
    fileFunc.DefaultSplit9(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/12_dk1Number.txt"
    fileFunc.tagNumber9(savingPath3)

    savingPath5 = confPath + "/12_dk1DefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)



if DK2:
    index_of_x = sc.sheetTitleshelper.index("DK2_EnPo_FileName")
    DK2_EnPo_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(DK2_EnPo_FileName, excelPath)
    
    savingPath1 = confPath + "/13_dk2Option.txt"
    savingPathMap = confPath + "/13_dk2Mapping.txt"
    Options = fileFunc.get_column_from_csv(DK2_EnPo_FileName ,savingPath1,savingPathMap)
    
    
    savingPath2 = confPath + "/13_dk2Default.txt"
    fileFunc.DefaultSplit10(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/13_dk2Number.txt"
    fileFunc.tagNumber10(savingPath3)

    savingPath5 = confPath + "/13_dk2DefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)



if DK3:
    index_of_x = sc.sheetTitleshelper.index("DK3_Potential_DK3_FileName")
    DK3_Potential_DK3_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(DK3_Potential_DK3_FileName, excelPath)
    
    savingPath1 = confPath + "/14_dk3Option.txt"
    savingPathMap = confPath + "/14_dk3Mapping.txt"
    Options = fileFunc.get_column_from_csv(DK3_Potential_DK3_FileName ,savingPath1,savingPathMap)
    
    
    savingPath2 = confPath + "/14_dk3Default.txt"
    fileFunc.DefaultSplit11(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/14_dk3Number.txt"
    fileFunc.tagNumber11(savingPath3)

    savingPath5 = confPath + "/14_dk3DefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)



if DK4:
    index_of_x = sc.sheetTitleshelper.index("DK4_ICD_OCT_FileName")
    DK4_ICD_OCT_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(DK4_ICD_OCT_FileName, excelPath)
    
    savingPath1 = confPath + "/15_dk4Option.txt"
    savingPathMap = confPath + "/15_dk4Mapping.txt"
    Options = fileFunc.get_column_from_csv(DK4_ICD_OCT_FileName ,savingPath1,savingPathMap)
    
    
    savingPath2 = confPath + "/15_dk4Default.txt"
    fileFunc.DefaultSplit12(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/15_dk4Number.txt"
    fileFunc.tagNumber12(savingPath3)

    savingPath5 = confPath + "/15_dk4DefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)



if DK5:
    index_of_x = sc.sheetTitleshelper.index("DK5_FileName")
    DK5_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(DK5_FileName, excelPath)
    
    savingPath1 = confPath + "/16_dk5Option.txt"
    savingPathMap = confPath + "/16_dk5Mapping.txt"
    Options = fileFunc.get_column_from_csv(DK5_FileName ,savingPath1,savingPathMap)
    
    
    savingPath2 = confPath + "/16_dk5Default.txt"
    fileFunc.DefaultSplit13(savingPath2, Options[0])
    
    
    
    savingPath3 = confPath + "/16_dk5Number.txt"
    fileFunc.tagNumber13(savingPath3)

    savingPath5 = confPath + "/16_dk5DefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)

if DK6_1 == True:
    index_of_x1 = sc.sheetTitleshelper.index("Domain_FileName_1")
    Domain_FileName_1 = sheetTitles[index_of_x1]  # C_Log

    fileFunc.saveASCSV(Domain_FileName_1,excelPath)
    
    savingPath1 = confPath + "/17_dk61Option.txt"
    savingPathMap = confPath + "/17_dk61Mapping.txt"
    Options = fileFunc.get_column_from_csv(Domain_FileName_1 ,savingPath1,savingPathMap)
    
    savingPath2 = confPath + "/17_dk61Default.txt"
    fileFunc.DefaultSplit14(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/17_dk61Number.txt"
    fileFunc.tagNumber14(savingPath3)

    savingPath5 = confPath + "/17_dk61DefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)
    
if DK6_2 == True:

    index_of_x2 = sc.sheetTitleshelper.index("Domain_FileName_2")
    Domain_FileName_2 = sheetTitles[index_of_x2]  # C_Log

    fileFunc.saveASCSV(Domain_FileName_2,excelPath)
    
    savingPath1 = confPath + "/18_dk62Option.txt"
    savingPathMap = confPath + "/18_dk62Mapping.txt"
    Options = fileFunc.get_column_from_csv(Domain_FileName_2 ,savingPath1,savingPathMap)
    
    savingPath2 = confPath + "/18_dk62Default.txt"
    fileFunc.DefaultSplit15(savingPath2, Options[0])
    
    
    
    savingPath3 = confPath + "/18_dk62Number.txt"
    fileFunc.tagNumber15(savingPath3)

    savingPath5 = confPath + "/18_dk62DefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)

if DK7:
    index_of_x = sc.sheetTitleshelper.index("DK7_Activity_DK7_FileName")
    DK7_Activity_DK7_FileName = sheetTitles[index_of_x]  # C_Log

    fileFunc.saveASCSV(DK7_Activity_DK7_FileName, excelPath)
    
    savingPath1 = confPath + "/19_dk7Option.txt"
    savingPathMap = confPath + "/19_dk7Mapping.txt"
    Options = fileFunc.get_column_from_csv(DK7_Activity_DK7_FileName ,savingPath1,savingPathMap)
    
    
    
    savingPath2 = confPath + "/19_dk7Default.txt"
    fileFunc.DefaultSplit16(savingPath2, Options[0])
    
    
    savingPath3 = confPath + "/19_dk7Number.txt"
    fileFunc.tagNumber16(savingPath3)

    savingPath5 = confPath + "/19_dk7DefaultValue.txt"
    fileFunc.DefaultValue1(savingPath3, savingPath2, savingPath5)






