import os
import csv

import A2_FileLocation_Step1_Address_Test_Func as fileFunc


fileSource=2
#Google Drive=1
#Local=2

confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)
print(confPath)

fileFunc.saveFileSource(confPath,fileSource)



print("#################################### Test ##################################################")


EventLogFinalDefault, myCredentialsDefault= fileFunc.existanceFileName(confPath, fileSource)
print("EventLogFinalDefault =", EventLogFinalDefault)
print("myCredentialsDefault =", myCredentialsDefault)



EventLogList = ["EventLog1", "EventLog4", "EventLog5", "EventLog6"]
EventLogSelector = 4

EventLogFinalTest = EventLogList[EventLogSelector - 1]


EventLogFinal = fileFunc.excelFileNameTest(confPath, fileSource,EventLogFinalTest)
print("EventLogFinal =", EventLogFinal)




if fileSource == 1: #Google

    symPath = '../../media/uploads/gcKey/miladGoogleSheet.json'
    myCredentials = os.path.realpath(symPath)
    fileFunc.GCP1_Test(confPath,myCredentials)
    print("myCredentials =", myCredentials)




if fileSource == 2:  #Local

    importPath = "/home/milad/Downloads/"
    fileFunc.local1_Test(confPath,importPath)
    print("importPath =", importPath)





