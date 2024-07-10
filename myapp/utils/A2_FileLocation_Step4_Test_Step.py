import os
import csv

import A2_FileLocation_Step4_Test_Func as fileFunc
import A1_Scenario_Step3 as sc1


print("#################################### goalList ##################################################")

goalList=sc1.goalList
print("goalList =", goalList)




print("#################################### default ##################################################")

confDirectory = '../../media/uploads/0_Data'
confPath2 = os.path.realpath(confDirectory)
excel_file_path = confPath2 + "/EventLog.xlsx"
print("excel_file_path =", excel_file_path)

confDirectory   = "../Data/0_DataConf"
confPath1 = os.path.realpath(confDirectory)
openingPath1 = confPath1 + "/3_previewDefault.txt"
print("openingPath1 =", openingPath1)

confDirectory  = "../Data/0_DataConf"
confPath1 = os.path.realpath(confDirectory)
savingPath1 = confPath1 + "/3_previewDefault.txt"
print("savingPath1 =", savingPath1)


default = fileFunc.local2_software(excel_file_path,goalList,openingPath1,savingPath1)
print("default =", default)






