import os
import csv

import A2_FileLocation_Step2_xlsx_Func as fileFunc









print("#################################### Downloading ##################################################")


confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)
print(confPath)

fileSource= fileFunc.readFileSource(confPath)
print("fileSource =", fileSource)

EventLogName, Location= fileFunc.readFileLocation(confPath, fileSource)
print("EventLogName =", EventLogName)
print("Location =", Location)


confDirectory = '../../media/uploads/0_Data'
confPath = os.path.realpath(confDirectory)
savingPath = confPath + "/EventLog.xlsx"
print("savingPath=",savingPath)


fileFunc.copyFile(savingPath, fileSource,EventLogName,Location)










