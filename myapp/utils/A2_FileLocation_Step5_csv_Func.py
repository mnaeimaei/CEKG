








def DefaultValue(file1, file2, save):

    import ast
    with open(file1, 'r') as file:
        data = file.read()
        listData = ast.literal_eval(data)
        #print(listData)

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

    with open(save, 'w') as file:
        file.write(f'''{valueList}''')

    print("valueList=",valueList)


def conf3creation(openPath,savePath):
    with open(openPath, 'r') as file:
        data=file.read()
    print("sheetList=", data)
    with open(savePath, 'w') as file:
        file.write(f'''sheetList={data}''' + "\n")

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





def saveASCSV(sheetName,excelPath):

    import pandas as pd
    import os
    #value1=excel file name
    #value2= location of excel file



    excel_file_path = excelPath
    xls = pd.ExcelFile(excel_file_path)

    df = pd.read_excel(xls, sheet_name=sheetName)

    directory = '../../media/uploads/0_Data'
    myCSV = os.path.realpath(directory + "/" +  sheetName + ".csv")
    print(myCSV)

    df.to_csv(myCSV, index=False)


def get_column_from_csv(file_name,savingPath,savingPathMap):
    import os
    confDirectory = '../../media/uploads/0_Data'
    confPath = os.path.realpath(confDirectory)
    open_FilePath = confPath + "/" + file_name + ".csv"

    import pandas as pd
    df = pd.read_csv(open_FilePath)
    list_of_column_names = list(df.columns)

    print(list_of_column_names)

    import copy
    dicList = copy.deepcopy(list_of_column_names)
    columns_dict = {str(i+1): dicList[i] for i in range(len(dicList))}
    print(columns_dict)

    with open(savingPath, 'w') as file:
        file.write(f'''{list_of_column_names}''')

    with open(savingPathMap, 'w') as file:
        file.write(f'''{columns_dict}''')

    return list_of_column_names





######################################################################################################


def DefaultSplit1(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''ED_eventIdTitle={firstItem}'''+"\n")
            file.write(f'''ED_Activity={firstItem}'''+"\n")
            file.write(f'''ED_ActivitySynonym={firstItem}'''+"\n")
            file.write(f'''ED_Timestamp={firstItem}'''+"\n")
            file.write(f'''ED_Activity_Value_ID={firstItem}'''+"\n")
            file.write(f'''ED_Activity_Properties_ID={firstItem}'''+"\n")

            file.write(f'''Entity1ID={firstItem}'''+"\n")
            file.write(f'''Entity2ID={firstItem}'''+"\n")
            file.write(f'''Entity3ID={firstItem}'''+"\n")
            file.write(f'''Entity4ID={firstItem}'''+"\n")
            file.write(f'''Entity5ID={firstItem}'''+"\n")
            file.write(f'''Entity6ID={firstItem}'''+"\n")
            file.write(f'''Entity7ID={firstItem}'''+"\n")
            file.write(f'''Entity8ID={firstItem}'''+"\n")
            file.write(f'''Entity9ID={firstItem}'''+"\n")
            file.write(f'''Entity10ID={firstItem}'''+"\n")
            file.write(f'''Entity11ID={firstItem}'''+"\n")
            file.write(f'''Entity12ID={firstItem}'''+"\n")
            file.write(f'''Entity13ID={firstItem}'''+"\n")
            file.write(f'''Entity14ID={firstItem}'''+"\n")
            file.write(f'''Entity15ID={firstItem}'''+"\n")
            file.write(f'''Entity16ID={firstItem}''' + "\n")
            file.write(f'''Entity17ID={firstItem}''' + "\n")
            file.write(f'''Entity18ID={firstItem}''' + "\n")
            file.write(f'''Entity19ID={firstItem}''' + "\n")
            file.write(f'''Entity20ID={firstItem}''' + "\n")

            file.write(f'''Entity1Origin={firstItem}''' + "\n")
            file.write(f'''Entity2Origin={firstItem}''' + "\n")
            file.write(f'''Entity3Origin={firstItem}''' + "\n")
            file.write(f'''Entity4Origin={firstItem}''' + "\n")
            file.write(f'''Entity5Origin={firstItem}''' + "\n")
            file.write(f'''Entity6Origin={firstItem}''' + "\n")
            file.write(f'''Entity7Origin={firstItem}''' + "\n")
            file.write(f'''Entity8Origin={firstItem}''' + "\n")
            file.write(f'''Entity9Origin={firstItem}''' + "\n")
            file.write(f'''Entity10Origin={firstItem}''' + "\n")
            file.write(f'''Entity11Origin={firstItem}''' + "\n")
            file.write(f'''Entity12Origin={firstItem}''' + "\n")
            file.write(f'''Entity13Origin={firstItem}''' + "\n")
            file.write(f'''Entity14Origin={firstItem}''' + "\n")
            file.write(f'''Entity15Origin={firstItem}''' + "\n")
            file.write(f'''Entity16Origin={firstItem}''' + "\n")
            file.write(f'''Entity17Origin={firstItem}''' + "\n")
            file.write(f'''Entity18Origin={firstItem}''' + "\n")
            file.write(f'''Entity19Origin={firstItem}''' + "\n")
            file.write(f'''Entity20Origin={firstItem}''' + "\n")

            file.write(f'''ED_EnNum=2''')

####################################################################################################################



######################################################################################################


def DefaultSplit2(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''EnP_Origin={firstItem}'''+"\n")
            file.write(f'''EnP_ID={firstItem}'''+"\n")
            file.write(f'''EnP_Name={firstItem}'''+"\n")
            file.write(f'''EnP_Value={firstItem}'''+"\n")
            file.write(f'''EnP_Category={firstItem}''')

####################################################################################################################


######################################################################################################


def DefaultSplit3(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''EnP_Entity_Origin1={firstItem}'''+"\n")
            file.write(f'''EnP_Entity_ID1={firstItem}'''+"\n")
            file.write(f'''EnP_Entity_Origin2={firstItem}'''+"\n")
            file.write(f'''EnP_Entity_ID2={firstItem}''')


####################################################################################################################


######################################################################################################


def DefaultSplit4(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''AcP_acID={firstItem}'''+"\n")
            file.write(f'''AcP_activityName={firstItem}'''+"\n")
            file.write(f'''AcP_activitySynonym={firstItem}'''+"\n")
            file.write(f'''AcP_label={firstItem}'''+"\n")
            file.write(f'''AcP_Value={firstItem}''')



####################################################################################################################


######################################################################################################


def DefaultSplit5(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''ACT_Domain={firstItem}''')


####################################################################################################################


######################################################################################################


def DefaultSplit6(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''CE_ClinicalEntity={firstItem}'''+"\n")
            file.write(f'''CE_icd_code={firstItem}'''+"\n")
            file.write(f'''CE_icd_version={firstItem}'''+"\n")
            file.write(f'''CE_icd_code_title={firstItem}''')


####################################################################################################################


######################################################################################################


def DefaultSplit7(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''OCT_OCT_Node_conceptId={firstItem}'''+"\n")
            file.write(f'''OCT_OCT_Node_ConceptCode={firstItem}'''+"\n")
            file.write(f'''OCT_OCT_Node_termA={firstItem}'''+"\n")
            file.write(f'''OCT_OCT_Node_termB={firstItem}'''+"\n")
            file.write(f'''OCT_OCT_Node_semanticTags={firstItem}'''+"\n")
            file.write(f'''OCT_OCT_Node_ConceptType={firstItem}'''+"\n")
            file.write(f'''OCT_OCT_Node_Levels={firstItem}''')


####################################################################################################################


######################################################################################################


def DefaultSplit8(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''OCT_OCT_REL_s0={firstItem}'''+"\n")
            file.write(f'''OCT_OCT_REL_s0_code={firstItem}'''+"\n")
            file.write(f'''OCT_OCT_REL_s1={firstItem}'''+"\n")
            file.write(f'''OCT_OCT_REL_s1_code={firstItem}''')



####################################################################################################################

def DefaultSplit9(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''DK1_XXXX={firstItem}'''+"\n")

######################################################################################################


def DefaultSplit10(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''DK2_XXXX={firstItem}'''+"\n")

####################################################################################################################


######################################################################################################


def DefaultSplit11(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''DK3_Disorders={firstItem}'''+"\n")
            file.write(f'''DK3_icd_code={firstItem}''')


####################################################################################################################


######################################################################################################


def DefaultSplit12(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''DK4_icd_code={firstItem}'''+"\n")
            file.write(f'''DK4_OTC={firstItem}''')



####################################################################################################################


######################################################################################################


def DefaultSplit13(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''DK5_Activity={firstItem}'''+"\n")
            file.write(f'''DK5_Activity_Synonym={firstItem}'''+"\n")
            file.write(f'''DK5_OTC={firstItem}'''+"\n")
            file.write(f'''DK5_SCTCode={firstItem}''')


####################################################################################################################


######################################################################################################


####################################################################################################################


######################################################################################################


def DefaultSplit14(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''Domain1_Activity={firstItem}'''+"\n")
            file.write(f'''Domain1_Activity_Synonym={firstItem}'''+"\n")
            file.write(f'''Domain1_Domain={firstItem}''')



####################################################################################################################


######################################################################################################


def DefaultSplit15(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''Domain2_Domain={firstItem}'''+"\n")
            file.write(f'''Domain2_OTC={firstItem}'''+"\n")
            file.write(f'''Domain2_SCTCode={firstItem}''')



####################################################################################################################


def DefaultSplit16(savingPath, firstItem):
    import os

    if os.path.exists(savingPath):
        print("event log file exists")
    else:
        print("file not exists")
        with open(savingPath, 'w') as file:
            file.write(f'''DK7_Activity_Value_ID={firstItem}'''+"\n")
            file.write(f'''DK7_Disorders={firstItem}'''+"\n")



####################################################################################

def tagNumber1(savingPath):
    list1=["ED_eventIdTitle","ED_Activity","ED_ActivitySynonym","ED_Timestamp","ED_Activity_Value_ID","ED_Activity_Properties_ID"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')

####################################################################################
def tagNumber2(savingPath):
    list1=["EnP_Origin","EnP_ID","EnP_Name","EnP_Value","EnP_Category"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')

####################################################################################
def tagNumber3(savingPath):
    list1=["EnP_Entity_Origin1","EnP_Entity_ID1","EnP_Entity_Origin2","EnP_Entity_ID2"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')

####################################################################################
def tagNumber4(savingPath):
    list1=["AcP_acID","AcP_activityName","AcP_activitySynonym","AcP_label","AcP_Value"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')

####################################################################################
def tagNumber5(savingPath):
    list1=["ACT_Domain"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber6(savingPath):
    list1 = ["CE_ClinicalEntity","CE_icd_code","CE_icd_version","CE_icd_code_title"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber7(savingPath):
    list1 = ["OCT_OCT_Node_conceptId","OCT_OCT_Node_ConceptCode","OCT_OCT_Node_termA","OCT_OCT_Node_termB","OCT_OCT_Node_semanticTags","OCT_OCT_Node_ConceptType","OCT_OCT_Node_Levels"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber8(savingPath):
    list1 = ["OCT_OCT_REL_s0","OCT_OCT_REL_s0_code","OCT_OCT_REL_s1","OCT_OCT_REL_s1_code"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber9(savingPath):
    list1 = ["DK1_XXXX"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber10(savingPath):
    list1 = ["DK2_XXXX"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber11(savingPath):
    list1 = ["DK3_Disorders","DK3_icd_code"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber12(savingPath):
    list1 = ["DK4_icd_code","DK4_OTC"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber13(savingPath):
    list1 =["DK5_Activity","DK5_Activity_Synonym","DK5_OTC","DK5_SCTCode"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber14(savingPath):
    list1 = ["Domain1_Activity","Domain1_Activity_Synonym","Domain1_Domain"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber15(savingPath):
    list1 = ["Domain2_Domain","Domain2_OTC","Domain2_SCTCode"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


####################################################################################
def tagNumber16(savingPath):
    list1 = ["DK7_Activity_Value_ID","DK7_Disorders"]
    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')




def tagNumber1b(savingPath,i):
    base_items = ["Entity1ID", "Entity1Origin"]
    list1 = []
    for n in range(1, i + 1):
        current_sublist = base_items.copy()
        for entity_num in range(2, n + 1):
            current_sublist += [f"Entity{entity_num}ID", f"Entity{entity_num}Origin"]
        list1.append(current_sublist)

    with open(savingPath, 'w') as file:
        file.write(f'''{list1}''')


def DefaultValue1(file1, file2, save):

    import ast
    with open(file1, 'r') as file:
        data = file.read()
        listData = ast.literal_eval(data)
        #print(listData)

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

    with open(save, 'w') as file:
        file.write(f'''{valueList}''')

    print(valueList)


def DefaultValue2(file1, file2, save, item0,n):

    refrence = []
    for i in range(1, n + 1):
        sublist = [item0] * (2 * i)
        refrence.append(sublist)
    print("refrence=",refrence)

    import ast
    with open(file1, 'r') as file:
        data = file.read()
        listData = ast.literal_eval(data)
        print("listData=", listData)

    for item, ref,iIndex in zip(listData,refrence,range(len(listData))):
        #print("iIndex=",iIndex)
        with open(file2, 'r') as file:
            for line in file:
                #print(line)
                variable_name, value = line.split('=')
                value_cleaned = value.replace("\n", "")
                #print(value_cleaned)
                if str(iIndex+1) == value_cleaned:
                    #print("yes")
                    compareIndex = iIndex+1
                    valueList2=[]
                    for each in item:
                        with open(file2, 'r') as file_new:
                            for line2 in file_new:
                                # print(line)
                                variable_name2, value2 = line2.split('=')
                                variable_name2 = variable_name2.strip()
                                # print(variable_name2)
                                value_cleaned2 = value2.replace("\n", "")
                                if each == variable_name2:
                                    # print("dsadasd")
                                    valueList2.append(value_cleaned2)

    #print("valueList2=",valueList2)
    #print("compareIndex=", compareIndex)

    valueList1 = []
    for ref,indexNew in zip(refrence,range(len(listData))):
        if indexNew+1==compareIndex:
            valueList1.append(valueList2)
        else:
            valueList1.append(ref)

    print("valueList1=",valueList1)

    with open(save, 'w') as file:
        file.write(f'''{valueList1}''')





