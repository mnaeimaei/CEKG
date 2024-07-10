import os
import csv

import A2_FileLocation_Step3_sheetName_Func as fileFunc


dataDirectory = '../../media/uploads/0_Data'
dataPath2 = os.path.realpath(dataDirectory)
print("dataPath2 =", dataPath2)


confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)
print("confPath =", confPath)

print("#################################### ExcelSheets ##################################################")



excel_file_path = dataPath2 + "/EventLog.xlsx"
savingPath = confPath + "/3_previewOptionSheetNames.txt"
savingPath2 = confPath + "/3_previewOptionSheetNamesMapping.txt"
ExcelSheets = fileFunc.sheetName(excel_file_path,savingPath,savingPath2)

print("ExcelSheets =", ExcelSheets)


print("#################################### default ##################################################")

savingPath = confPath + "/3_previewDefault.txt"


fileFunc.DefaultSplit(savingPath, ExcelSheets[0])


print("#################################### default List ##################################################")


openingPath1 = confPath + "/3_previewNumberOfQuestions.txt"
openingPath2 = confPath + "/3_previewDefault.txt"
savingPath = confPath + "/3_previewDefaultValue.txt"


fileFunc.DefaultValue(openingPath1, openingPath2, savingPath)



