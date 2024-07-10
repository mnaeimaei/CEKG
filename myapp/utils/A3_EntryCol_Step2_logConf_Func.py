def readtxtFiles():
    import os
    import ast
    confDirectory  = "../Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)


    value3List =[]


    theLast = confPath + "/3_previewXConf.txt"



    with open(theLast, 'r') as file:
        for line in file:
            variable_name3, value3 = line.split('=')
            value3 = value3.strip()
            value3List = ast.literal_eval(value3)


    return value3List




def DefaultValue(file1, file2, save):

    import ast
    with open(file1, 'r') as file:
        data = file.read()
        listData = ast.literal_eval(data)
        #print(listData)

    dicList=[]
    valueList=[]
    for item in listData:
        #print(item)
        #print(type(item))
        with open(file2, 'r') as file:
            for line in file:
                #print(line)
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                #print(variable_name)
                #print(value)
                value_cleaned = value.replace("\n", "")
                if item==variable_name:
                    #print("dsadasd")
                    valueList.append(value_cleaned)
                    dic={item: value_cleaned}
                    dicList.append(dic)


    with open(save, 'w') as file:
        file.write(f'''{valueList}''')

    combined_dict = {}
    for d in dicList:
        combined_dict.update(d)

    return combined_dict


def DefaultValueEventLog(file1, file2, save):


    with open(file2, 'r') as file:
        for line in file:
            variable_name, value = line.split('=')
            variable_name = variable_name.strip()
            value_cleaned = value.replace("\n", "")
            if "ED_EnNum" == variable_name:
                ED_EnNum=int(value_cleaned)
                itemDic1 = {"ED_EnNum": int(value_cleaned)}




    import ast
    with open(file1, 'r') as file:
        data = file.read()
        listData1= ast.literal_eval(data)
        listData=listData1[ED_EnNum-1]
    #print("listData=",listData)

    dicList = []
    valueList=[]
    for item in listData:
        #print(item)
        #print(type(item))
        with open(file2, 'r') as file:
            for line in file:
                #print(line)
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                #print(variable_name)
                #print(value)
                value_cleaned = value.replace("\n", "")
                if item==variable_name:
                    #print("dsadasd")
                    valueList.append(value_cleaned)

                    dic={item: value_cleaned}
                    dicList.append(dic)

    #print("valueList=", valueList)
    #print("dicList=", dicList)
    dicList.append(itemDic1)
    #print("dicList=", dicList)



    with open(save, 'r') as file:
        for line in file:
            listDataFinal = ast.literal_eval(line)

    listDataFinal[ED_EnNum-1] = valueList

    with open(save, 'w') as file:
        file.write(f'''{listDataFinal}''')

    combined_dict = {}
    for d in dicList:
        combined_dict.update(d)
    return combined_dict





def SaveDic(pathLocation,Dic,Name):
    with open(pathLocation, 'w') as file:
        file.write(f'''{Name}={Dic}''' + "\n")
