import pandas as pd
import time, os, csv
from itertools import combinations
from itertools import chain, permutations
import itertools
import re
import copy
from neo4j import GraphDatabase





def removeDecimalInIDs(csvlog, dicEntID, EnNum):

    def trim_fraction(text):   #removing Decimal from IDs
        if text != 'nan':
            if '.0' in text:
                x = text[:text.rfind('.0')]
            else:
                x=text
        if text == 'nan':
            x = float('nan')
        return x

    for k in range(EnNum):
        IDcol= list(dicEntID.values())[k]
        #print("IDcol=",IDcol)
        csvlog[IDcol] = csvlog[IDcol].astype(str)
        #print("csvlog[IDcol]=", csvlog[IDcol])
        csvlog[IDcol] = csvlog[IDcol].apply(trim_fraction)
    return csvlog


def removeDecimalInAct(csvlog, colTitle):

    def trim_fraction(text):   #removing Decimal from IDs
        if text != 'nan':
            if '.0' in text:
                x = text[:text.rfind('.0')]
            else:
                x=text
        if text == 'nan':
            x = float('nan')
        return x

    csvlog[colTitle] = csvlog[colTitle].astype(str)
    csvlog[colTitle] = csvlog[colTitle].apply(trim_fraction)
    return csvlog



def EntityOriginValue_Temp(EntityOrgValue, EnNum):
    flat_list = [item for sublist in EntityOrgValue for item in sublist]
    list1 = []
    for i in range(EnNum):
        list1.append(flat_list)

    return list1



def NumberEntityOriginAbr(EntityOriginValue_First, EnNum):
    dicNumEntOrgAbr = {}
    for s in range(0, EnNum):
        list4 = EntityOriginValue_First[s]
        if not list4:
            moduleVaribale = float("nan")
        else:
            # findingNumber###################################
            x = len(list4)
            result = max(len(x) for x in list4)
            for s2 in range(result):
                final = s2 + 1
                p = []
                for i in range(x):
                    k = list4[i]
                    d = k[:s2 + 1]
                    p.append(d)
                p = list(dict.fromkeys(p))
                if len(p) == x:
                    break
            # findingNumber####################################

            moduleVaribale = final

        dicNumEntOrgAbr["nEnt{0}Org_Abr".format(s + 1)] = moduleVaribale
    return dicNumEntOrgAbr



def EntityAliasAbr(dicEnt, dicNumEntOrgAbr, EnNum):
    dicEntAliaAbr = {}
    for i in range(EnNum):
        # print(i)
        y1 = f"Entity{i + 1}Alias"
        # print(y)
        x = dicEnt[y1]
        y2 = f"nEnt{i + 1}Org_Abr"
        nEnt_Abr = dicNumEntOrgAbr[y2]
        moduleVaribale = x[0:nEnt_Abr]

        dicEntAliaAbr["nEnt{0}Org_Abr".format(i + 1)] = moduleVaribale
    return dicEntAliaAbr

#Reanmeing column
def ImportCSVRename(csvLog, activityTitle, Timestamp):

    csvLog = csvLog.rename(columns={activityTitle: 'Activity', Timestamp: 'timestamp'})


    activityTitle = 'Activity'
    Timestamp = 'timestamp'
    return csvLog, activityTitle, Timestamp

#Changing column
def Create_CSV_in_Neo4J_import(csvLog, Neo4JImport, outputFileName, EntityIDColumnList, ED_Activity_Properties_ID):
    sampleIds = []
    sampleList = []  # create a list (of lists) for the sample data containing a list of events for each of the selected cases
    # fix missing entity identifier for one record: check all records in the list of sample cases (or the entire dataset)
    for index, row in csvLog.iterrows():
        if sampleIds == [] :
            rowList = list(row)  # add the event data to rowList
            #print(rowList)
            sampleList.append(rowList)  # add the extended, single row to the sample dataset
            #print(sampleList)

    header = list(csvLog)  # save the updated header data
    #print(header)
    logSamples = pd.DataFrame(sampleList, columns=header)  # create pandas dataframe and add the samples

    logSamples['timestamp'] = pd.to_datetime(logSamples['timestamp'], format='%Y-%m-%d %H:%M:%S')

    logSamples.fillna(0)

    logSamples['timestamp'] = logSamples['timestamp'].map(lambda x: x.strftime('%Y-%m-%dT%H:%M:%S.%f')[0:-3] + '+0100')




    #------converting IDs Columns values to list in dataframe-------
    for i in range(len(EntityIDColumnList)):
        item=EntityIDColumnList[i]
        #print(item)
        #print(logSamples[item])
        logSamples[item] = logSamples[item].map(lambda x: x.split(",") if ("," in str(x) and str(x) != 'nan')
                                                     else (list(x.split(" ")) if ("," not in str(x) and str(x) != 'nan')
                                                     else "Unknown" )
                                                )
        #print(logSamples[item])
        logSamples[item] = logSamples[item].map(lambda x: x.split(" ") if (str(x) == 'Unknown') else (x))

        #print(logSamples[item])
    #------converting IDs Columns values to list in dataframe-------

    #------converting Act Properties Columns values to list in dataframe-------
    logSamples[ED_Activity_Properties_ID] = logSamples[ED_Activity_Properties_ID].map(
                                                 lambda x: sorted(x.split(",")) if ("," in str(x) and str(x) != 'nan')
                                                 else (list(x.split(" ")) if ("," not in str(x) and str(x) != 'nan')
                                                 else "Unknown" )
                                            )


    logSamples[ED_Activity_Properties_ID] = logSamples[ED_Activity_Properties_ID].map(lambda x: x.split(" ") if (str(x) == 'Unknown') else (x))
    #------converting IDs Columns values to list in dataframe-------

    print(Neo4JImport)
    logSamples.to_csv(Neo4JImport + outputFileName, index=True, index_label="idx", na_rep="Unknown")
    #print(logSamples.to_string())







def Entities_Alias_values (EnNum, EntityOrgValue):
    dicEnt = {}
    for x in range(1, EnNum+1):
        #print(x)
        dicEnt["Entity{0}Alias".format(x)] = EntityOrgValue[x-1][0]
    # print(dicEntity)
    return dicEnt


def EntityOrigins_values (EnNum, input):
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





def EntityIDColumn (EnNum, input):
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









def EntityOriginValue(df,dicEntOrigin,EnNum):
    list1=[]
    for i in range(EnNum):
        #print("SSSSSSSSSSSSSSSSSSSSSSSS")
        x = list(dicEntOrigin.values())[i]
        #print("x=",x)
        l1 = df[x].tolist()
        #print(l1)
        EntityTypeValue1 = list(dict.fromkeys(l1))
        EntityTypeValue = [k for k in EntityTypeValue1 if str(k) != 'nan']
        #print("EntityTypeValue=", EntityTypeValue)
        list1.append(EntityTypeValue)
        #print(list1)
    return list1




def flat_list(original_list):
    new_list = [item[0] if isinstance(item, list) and len(item) == 1 else item for item in original_list]
    return new_list




def EntityOriginIDValue(df,dicEntOrigin,EnNum):
    #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")

    list1=[]
    for i in range(EnNum):
        x = list(dicEntOrigin.values())[i]
        #print(" ")
        #print("x=",x)
        l1 = df[x].tolist()
        #print("l1=",l1)
        l2 = []
        for i in range(len(l1)):
            item=l1[i]
            #print("item=", item)
            if "," in str(item) and str(item) != 'nan':

                my_list1 = item.split(",")
                #print("my_list11=",my_list1)
            if "," not in str(item) and str(item) != 'nan':
                my_list1 = [str(int(item))]

                #print("my_list12=", my_list1)
            if str(item) == 'nan' :
                my_list1 = []
            l2.extend(my_list1)
        #print("l2=", l2)

        EntityTypeValue = list(dict.fromkeys(l2))
        #print("EntityTypeValue=", EntityTypeValue)
        if isinstance(EntityTypeValue[0], float):
            #print(type(EntityTypeValue[0]))
            #print("EntityTypeValue=", EntityTypeValue)
            EntityTypeValue = [str(int(float(k))) for k in EntityTypeValue]
        if isinstance(EntityTypeValue[0], str):
            EntityTypeValue = [str(k) for k in EntityTypeValue]
        list1.append(EntityTypeValue)
        #print("EntityTypeValue=", EntityTypeValue)
        #print("list1=",list1)
    #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")

    return list1


def activityNode(df, ED_Activity, ED_ActivitySynonym):
    dataF = df
    column_names = [ED_Activity, ED_ActivitySynonym]
    # print(column_names)

    # Get distinct values from the specified columns
    distinct_values = dataF[column_names].drop_duplicates().values.tolist()

    return distinct_values


def activityNodewithID(df, ED_Activity, ED_ActivitySynonym,ED_Activity_Properties_ID):
    dataF = df
    column_names = [ED_Activity, ED_ActivitySynonym,ED_Activity_Properties_ID]
    # print(column_names)
    dataF2=dataF[column_names].values.tolist()
    #print("dataF2=",dataF2)


    '''
    #Sorting:
    dataF3 = []
    for item in dataF2:
        numbers_str = item[2].strip("[]").split(', ')
        sorted_numbers = sorted([int(num.strip("'")) for num in numbers_str])
        string_list = [str(num) for num in sorted_numbers]
        new_item = [item[0], item[1], str(string_list)]
        dataF3.append(new_item)
    #print("dataF3=",dataF3)
    '''

    #Distinct
    distinct_items = set()
    dataF4 = []

    for item in dataF2:
        item_str = item[2]  # Assuming the distinctness is judged based on the third element of each sublist
        if item_str not in distinct_items:
            distinct_items.add(item_str)
            dataF4.append(item)
    #print("dataF4=",dataF4)

    for i in range(len(dataF4)):
        dataF4[i].insert(0, 'ap' + str(i + 1))

    return dataF4


def eventAct_Rel(actNode, ED_Activity, ED_ActivitySynonym):
    list3 = []
    for list1 in actNode:
        list2 = []
        txt1 = f" e.{ED_Activity} =\"{list1[0]}\""
        txt2 = f" e.{ED_ActivitySynonym} =\"{list1[1]}\""
        list2.append(txt1)
        list2.append(txt2)
        list2.append(list1[0])
        list2.append(list1[1])
        list3.append(list2)
    return list3






def EntityAndEntityOrg_Creater(dicEntOrigin,EntityOriginIDValue, dicEntID, EnNum, dicEnt):
    #print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    list6=[]
    for k1 in range(EnNum):
        EntityOrgValue=EntityOriginIDValue[k1]
        EntityOrgCol = list(dicEntOrigin.values())[k1]
        EntityIDCol= list(dicEntID.values())[k1]
        EntityEntCol = list(dicEnt.values())[k1]
        list5 = []

        for i in EntityOrgValue:
            list4=[]
            list4.append(i)
            list4.append(EntityIDCol)
            txt = f"WHERE e.{EntityOrgCol} =\"{EntityEntCol}\""
            list4.append(txt)
            list4.append(EntityEntCol)
            list5.append(list4)
        list6.append(list5)

    return list6


def EntityAndEntityOrg_Creater_Final(dicEntOrigin,EntityOriginIDValue, dicEntID, EnNum, dicEnt):
    #print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    list6=[]
    for k1 in range(EnNum):
        EntityOrgValue=EntityOriginIDValue[k1]
        EntityOrgCol = list(dicEntOrigin.values())[k1]
        EntityIDCol= list(dicEntID.values())[k1]
        EntityEntCol = list(dicEnt.values())[k1]
        list5 = []

        for i in EntityOrgValue:
            list4=[]
            list4.append(i)
            list4.append(EntityIDCol)
            txt = f"WHERE e.{EntityOrgCol} =\"{EntityEntCol}\""
            list4.append(txt)
            list4.append(EntityEntCol)
            list5.append(list4)
        list6.append(list5)

    return list6



def EntityAndEntityOrg_Creater2(EntityOriginIDValue, EnNum, dicEnt):
    list6=[]
    for k1 in range(EnNum):
        EntityOrgValue=EntityOriginIDValue[k1]
        EntityEntCol = list(dicEnt.values())[k1]
        list5 = []
        for i in EntityOrgValue:
            list4=[]
            list4.append(i)
            list4.append(EntityEntCol)
            list5.append(list4)
        list6.append(list5)

    return list6


def EntityAndEntityOrg_Creater3(EntityOriginIDValue, EnNum, dicEnt,dicEntAliasAbr):
    list6=[]
    for k1 in range(EnNum):
        EntityOrgValue=EntityOriginIDValue[k1]
        EntityEntCol = list(dicEnt.values())[k1]
        AbrEntCol = list(dicEntAliasAbr.values())[k1]
        list5 = []
        for i in EntityOrgValue:
            list4=[]
            list4.append(AbrEntCol)
            list4.append(i)
            list4.append(EntityEntCol)
            list5.append(list4)
        list6.append(list5)

    return list6

















def model_entities(EntityAndEntityOrg,EnNum):

    model_entities=[]
    for i in range(EnNum):
        model_entities.extend(EntityAndEntityOrg[i])

    return model_entities

import re







def EntityIDColumnL(dicEntID, EnNum):
    l1=[]
    for i in range(EnNum):
        #print(i)
        x = list(dicEntID.values())[i]
        #print(x)
        l1.append(x)
    return l1



def CreateActivity(csvLog_ED,ED_Activity,ED_ActivitySynonym):
    dataF=csvLog_ED
    column_names = [ED_Activity, ED_ActivitySynonym]
    #print(column_names)

    # Get distinct values from the specified columns
    distinct_values = dataF[column_names].drop_duplicates().values.tolist()

    return distinct_values