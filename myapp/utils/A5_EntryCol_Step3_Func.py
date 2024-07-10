import os
import copy
import os
import pandas as pd



def readtxtFiles():
    import os
    import ast
    confDirectory  = "../Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    fileSourceInt=1
    value1="X"
    value2="X"
    value3List =[]



    FilePath0 = confPath + "/2_downloadingFileSource.txt"
    Google1= confPath + "/2_downloadingGoogleCloud1.txt"
    Google2= confPath + "/2_downloadingGoogleCloud2.txt"
    Local1= confPath + "/2_downloadingLocal1.txt"
    Local2= confPath + "/2_downloadingLocal2.txt"
    theLast = confPath + "/3_previewXConf.txt"


    with open(FilePath0, 'r') as file:
        for line in file:
            variable_name, fileSource = line.split('=')
            fileSource = fileSource.strip()
            fileSourceInt=int(fileSource)
            if fileSourceInt == 1:
                with open(Google1, 'r') as file:
                    for line in file:
                        variable_name1, value1 = line.split('=')
                        value1 = value1.strip()
                with open(Google2, 'r') as file:
                    for line in file:
                        variable_name2, value2 = line.split('=')
                        value2 = value2.strip()
                with open(theLast, 'r') as file:
                    for line in file:
                        variable_name3, value3 = line.split('=')
                        value3 = value3.strip()
                        value3List = ast.literal_eval(value3)


            if fileSourceInt == 2:
                with open(Local1, 'r') as file:
                    for line in file:
                        variable_name1, value1 = line.split('=')
                        value1 = value1.strip()
                with open(Local2, 'r') as file:
                    for line in file:
                        variable_name2, value2 = line.split('=')
                        value2 = value2.strip()
                with open(theLast, 'r') as file:
                    for line in file:
                        variable_name3, value3 = line.split('=')
                        value3 = value3.strip()
                        value3List = ast.literal_eval(value3)

    return fileSourceInt, value1, value2, value3List



def Other_DefaultMenu(confPath, ED_Event_FileName):

    ED_FilePath = confPath + "/" + ED_Event_FileName + "_conf.txt"
    #print(ED_FilePath)

    import ast
    with open(ED_FilePath, 'r') as file:
        line = file.readline()
        if line:
            dict_str = line.split("=", 1)[1].strip()
            dictFinal = ast.literal_eval(dict_str)


            #print(type(dictFinal))

            return dictFinal



def EntityOrigins_values (EnNum):
    import A5_EntryCol_Step3_Step as input

    dicEntOrigin = {}
    for x in range(1, EnNum+1):
        #print(x)
        moduleVaribale = 'Entity' + str(x) + 'Origin'
        #print(moduleVaribale)
        if hasattr(input, moduleVaribale) == True:
            moduleVaribale2 = (getattr(input, moduleVaribale))
            #print(moduleVaribale2)
            dicEntOrigin["Entity{0}Origin".format(x)] = moduleVaribale2
        else:
            moduleVaribale2 = float("nan")
            #print(moduleVaribale2)
            dicEntOrigin["Entity{0}Origin".format(x)] = moduleVaribale2
    # print(dicEntity)
    return dicEntOrigin

def EntityIDColumn (EnNum):
    import A5_EntryCol_Step3_Step as input
    dicEntID = {}
    for x in range(1, EnNum+1):
        #print(x)
        moduleVaribale = 'Entity' + str(x) + 'ID'
        #print(moduleVaribale)
        if hasattr(input, moduleVaribale) == True:
            moduleVaribale2 = (getattr(input, moduleVaribale))
            # print(moduleVaribale2)
            dicEntID["Entity{0}ID".format(x)] = moduleVaribale2
        else:
            moduleVaribale2 = float("nan")
            #print(moduleVaribale2)
            dicEntID["Entity{0}ID".format(x)] = moduleVaribale2

    # print(dicEntity)
    return dicEntID

def EntityListsELFunc (csvName,ED_EnNum):
    import pandas as pd

    confDirectory = '../../media/uploads/0_Data'
    confPath = os.path.realpath(confDirectory)
    # print(confPath)

    confPath = confPath + "/" + csvName +".csv"
    #print(confPath)

    df = pd.read_csv(confPath)

    list1=[]
    for value in ED_EnNum.values():
        distinct_values = df[value].unique()
        #print("distinct_values=",distinct_values)
        list1.append(distinct_values[0])

    return list1

