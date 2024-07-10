import os
import csv

import A2_FileLocation_Step1_Address_Test_Func as fileFunc


fileSource=2
#Google Drive=1
#Local=2

confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)

print("confPath =", confPath)




print("#################################### Test ##################################################")

#Read the contents the Two Text Boxes
userNameNeo, passWordNeo= fileFunc.existanceFileName(confPath)
print("userNameNeo =", userNameNeo)
print("passWordNeo =", passWordNeo)



#update the userNameFIle = 2_downloadingLocal1.txt

userNameNeoFile = fileFunc.excelFileNameTest(confPath, userNameNeo)
print("userNameNeoFile =", userNameNeoFile)

#update the passWordFIle = 2_downloadingLocal2.txt
passWordNeoFile=fileFunc.local1_Test(confPath,passWordNeo)
print("passWordNeoFile =", passWordNeoFile)





