import os
import csv

import A2_FileLocation_Step2_xlsx_Func as fileFunc









print("#################################### Downloading ##################################################")


confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)
print(confPath)



userNameNeo, passWordNeo= fileFunc.readFileLocation(confPath,)
print("userNameNeo =", userNameNeo)
print("passWordNeo =", passWordNeo)


confDirectory = '../../media/uploads/0_Data'
confPath = os.path.realpath(confDirectory)



fileFunc.rename_first_excel_file(confPath, "EventLog.xlsx")










