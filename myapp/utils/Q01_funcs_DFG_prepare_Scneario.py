import pandas as pd
import time, os, csv
from itertools import combinations
from itertools import chain, permutations
import itertools
import re
import copy
from neo4j import GraphDatabase
import random

def EntityOriginValue_Temp(EntityOrgValue, EnNum):
    flat_list = [item for sublist in EntityOrgValue for item in sublist]
    list1 = []
    for i in range(EnNum):
        list1.append(flat_list)

    return list1





def select_two_random_items(input_list):
    # Check if the list has at least two elements
    if len(input_list) < 2:
        raise ValueError("List must have at least two elements.")

    # Use random.sample() to select two random items from the list
    random_items = random.sample(input_list, 2)

    return random_items





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


def idColumnAndValueMaler(EntityIDColumnList, EntityOriginIDValue, EnNum):
    list2 = []
    for i in range(EnNum):
        list1 = []
        list1.append(EntityIDColumnList[i])
        list1.append(EntityOriginIDValue[i])
        list2.append(list1)

    return list2


def eventListMaker(df3, eventIdTitle):
    EventList = df3[eventIdTitle].tolist()

    def get_sort_key(s):
        m = re.match('e([0-9]+)', s)
        return (int(m.group(1)))

    EventList.sort(key=get_sort_key)

    return EventList


def EntitiesOrgList(EntityOrgValueAbr, EnNum):
    list1 = []
    for k1 in range(EnNum):
        EntityOrgValueAbr1 = EntityOrgValueAbr[k1]
        # print("EntityOrgValueAbr1=",EntityOrgValueAbr1)
        if len(EntityOrgValueAbr1) == 1:
            # print("OK")
            tempList = list(EntityOrgValueAbr1)
            # print(tempList)
        else:
            temp = combinations(EntityOrgValueAbr1, 2)
            tempList = list(temp)
            # print("tempList=", tempList)
        list1.append(tempList)
        # print(list1)
    return list1


def create_adjacent_pairs(input_list,ED_EnNum):
    list1=[]
    for j in range(ED_EnNum):

        myList = copy.deepcopy(input_list)
        myList2=myList[j]
        pair_list = []
        for i in range(len(myList2) - 1):
            pair = (myList2[i], myList2[i + 1])
            pair_list.append(pair)

        unique_list = []
        for item in pair_list:
            if item not in unique_list:
                unique_list.append(item)
        list1.append(unique_list)

    return list1



def create_adjacent_pairs_unique(input_list,ED_EnNum):
    list1=[]
    for j in range(ED_EnNum):

        myList = copy.deepcopy(input_list)
        myList2=myList[j]
        pair_list = []
        for i in range(len(myList2)):
            pair = (myList2[i], myList2[i])
            pair_list.append(pair)

        list1.append(pair_list)

    return list1



def EntitiesOrgList_Dual(EntityOrgValueAbr, EnNum):
    list1 = []
    for k1 in range(EnNum):
        # print(k1)
        EntityOrgValueAbr1 = EntityOrgValueAbr[k1]
        # print("EntityOrgValueAbr1=",EntityOrgValueAbr1)
        if len(EntityOrgValueAbr1) == 1:
            # print("OK")
            tempList = list(EntityOrgValueAbr1)
            # print(tempList)
        else:
            temp = combinations(EntityOrgValueAbr1, 2)
            tempList = list(temp)
            # print("tempList=", tempList)
            tempList_2 = [t[::-1] for t in tempList]
            # print("tempList_2=", tempList_2)
            tempList.extend(tempList_2)
            # print("tempList=", tempList)

        list1.append(tempList)
        # print(list1)
    return list1


def pair_memebr2(EntitiesTypeList, EnNum, dicEntAliasAbr):
    # print("EntitiesTypeList=",EntitiesTypeList)
    # print("EnNum=",EnNum)

    Temp = []
    list1 = []
    for k2 in range(EnNum):
        tempList = EntitiesTypeList[k2]
        stages = []
        for i in tempList:
            a = list(i[0:1])
            b = list(i[1:2])
            a = [str(i) for i in a]
            b = [str(i) for i in b]
            # print("a=",a)
            # print("b=",b)
            lst_tuple = list(zip(a, b))
            # print("lst_tuple=",lst_tuple)
            stages.extend(lst_tuple)

        # print("stages=",stages)
        def join_tuple_string(strings_tuple) -> str:
            return '_'.join(strings_tuple)

        result = map(join_tuple_string, stages)
        # print("result=",result)
        final1 = list(result)
        # print("final1=",final1)
        final1.sort()
        preFix1 = list(dicEntAliasAbr.values())[k2]
        # print(preFix1)
        model_entities_derived = [preFix1 + "_" + s for s in final1]
        model_entities_derived_temp = [preFix1 + "_" + s for s in final1]
        list1.extend(model_entities_derived)
        Temp.append(model_entities_derived_temp)

    return list1, Temp


def model_relations(model_entities_derived_Temp, EntityOrgValue, EnNum, dicEnt, dicEntAliasAbr):
    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    list2 = []
    for s in range(EnNum):
        #print("s=", s)
        EntityOrgVal = EntityOrgValue[s]
        Ent = list(dicEnt.values())[s]
        Alias = list(dicEntAliasAbr.values())[s]

        # print("EntityOrgValue=",EntityOrgValue)
        # print("EnID=",EnID)
        # print("model_entities_derived=",model_entities_derived_Temp)

        list1 = []
        for x in model_entities_derived_Temp[s]:
            #print("x=",x)
            d1 = re.search('_(.*)_', x)
            d1 = d1.group(1)
            #print(d1)
            d2 = re.search('_(.*)', x)
            d2 = d2.group(1)
            d2 = d2.split("_", 1)[1]
            #print(d2)
            Mix = []
            Mix.append(Alias)
            Mix.append(x)
            Mix.append(d1)
            Mix.append(d2)
            Mix.append(Ent)
            list1.append(Mix)
        list2.extend(list1)

    return list2



def include_entities(EntityOrgValue, model_entities_derived_Temp, EnNum):
    include_entities = []
    for i in range(EnNum):
        for j in EntityOrgValue[i]:
            include_entities.append(j)
    for i in range(EnNum):
        for j in model_entities_derived_Temp[i]:
            include_entities.append(j)
    return include_entities


def include_DF1(EntityOrgValue, model_entities_derived_Temp, EnNum):
    myList1 = copy.deepcopy(EntityOrgValue)
    myList2 = [[item[0], item[0]] for item in myList1]
    return myList2


def include_DF2(EntityOrgValue, model_entities_derived_Temp, EnNum):
    myList1 = copy.deepcopy(EntityOrgValue)
    myList3 = copy.deepcopy(model_entities_derived_Temp)
    myList2=[]
    for i,j in zip(myList1,myList3):
        for k in j:
            list2 = []
            list2.append(i[0])
            list2.append(k)
            myList2.append(list2)
    return myList2





def convert_to_list_of_lists(input_list):

    return [[item] for item in input_list]

def Entities_Alias_values (EnNum, EntityOrgValue):
    dicEnt = {}
    for x in range(1, EnNum+1):
        #print(x)
        dicEnt["Entity{0}Alias".format(x)] = EntityOrgValue[x-1][0]
    # print(dicEntity)
    return dicEnt


def EntityIDColumnL(dicEntID, EnNum):
    l1=[]
    for i in range(EnNum):
        #print(i)
        x = list(dicEntID.values())[i]
        #print(x)
        l1.append(x)
    return l1



def Finading_Entities_ID(driver,col1,entityListIDproperty, conditionProperty, conditionPropertyValue):
    listFinal=[]
    for i in range(len(col1)):
        EnityName=col1[i]
        idCol=entityListIDproperty[i]
        prop=conditionProperty[i]
        val = conditionPropertyValue[i]
        #print(EnityName)

        query1 = f'''     
        MATCH p=(e)-[:CORR]->(n:{EnityName})
        where n.{prop}="{val}"
        return distinct n.{idCol}
        '''

        print(query1)

        with driver.session() as session:
            record1 = session.run(query1).values()
            #print("record1=", record1)
            flat_list = [item for sublist in record1 for item in sublist]
            #print("flat_list=", flat_list)

        listFinal.append(flat_list)

    #print(listFinal)
    return listFinal




def Finading_ID_List(driver,col1,IDcol, conditionProperty, conditionPropertyValue):
    listFinal=[]
    for i in range(len(col1)):
        EnityName=col1[i]
        id=IDcol[i]
        prop = conditionProperty[i]
        val = conditionPropertyValue[i]
        #print(EnityName)

        query1 = f'''     
        MATCH (e)-[r:CORR]->(n:{EnityName})
        where n.{prop}="{val}"
        with n.{id} AS id, e.timestamp as time
        order by time
        WITH id, time
        RETURN id
        '''

        #print(query1)

        with driver.session() as session:
            record1 = session.run(query1).values()
            #print("record1=", record1)
            flat_list = [item for sublist in record1 for item in sublist]
            #print("flat_list=", flat_list)
            result = []
            for i, item in zip(range(len(flat_list)), flat_list):
                #print(item, "   ", i)
                if i==0:
                    result.append(item)
                if i!=0:
                    if item!=flat_list[i-1]:
                        result.append(item)
                        #print(item)
            #print(result)

        listFinal.append(result)

    #print(listFinal)
    return listFinal



def Finading_ID_ListUnique(driver,col1,Type_selection,Type_selection_ID,Type_selection_ID_instances,entityListIDproperty, conditionProperty, conditionPropertyValue):
    listFinal=[]
    for i in range(len(col1)):
        EnityName=col1[i]
        id=entityListIDproperty[i]
        prop = conditionProperty[i]
        val = conditionPropertyValue[i]

        query1 = f'''     
        MATCH (e)-[r:CORR]->(n:{EnityName})
        where n.{prop}="{val}"
        RETURN distinct n.{id}
        '''

        #print(query1)

        with driver.session() as session:
            record1 = session.run(query1).values()
            #print("record1=", record1)
            flat_list = [item for sublist in record1 for item in sublist]
            #print("flat_list=", flat_list)


        listFinal.append(flat_list)

    #print(listFinal)
    return listFinal

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

def EntityAndEntityOrg_CreaterAG(dicEntOrigin, EntityOriginIDValue, dicEntID, EnNum, dicEnt):
    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    list6 = []
    for k1 in range(EnNum):
        EntityOrgValue = EntityOriginIDValue[k1]
        EntityOrgCol = list(dicEntOrigin.values())[k1]
        EntityIDCol = list(dicEntID.values())[k1]
        EntityEntCol = list(dicEnt.values())[k1]
        # print("EntityOrgValue=",EntityOrgValue)
        # print("EntityOrgCol=",EntityOrgCol)
        # print("EntityIDCol=",EntityIDCol)
        # print("EntityEntCol=", EntityEntCol)

        list5 = []
        # print("list5=",list5)
        for i in EntityOrgValue:
            list4 = []
            # print("i=",i)
            # list4.append(i)
            list4.append(EntityEntCol)
            # print("list4=",list4)
            txt = f"{EntityOrgCol}"
            # print("txt=", txt)
            list4.append(txt)
            list4.append(EntityIDCol)
            # print("list4=",list4)
            list5.append(list4)
        # print("list5=", list5)

        list6.append(list5)

    return list6


def model_entities_AG(EntityAndEntityOrg, EnNum):
    model_entities = []
    for i in range(EnNum):
        model_entities.extend(EntityAndEntityOrg[i])
    return model_entities


def removeDuplicateLists(myListA):
    myList = copy.deepcopy(myListA)
    myList.sort()
    myList2 = list(k for k, _ in itertools.groupby(myList))
    return myList2


def pair_memebr3(EntitiesTypeList, EnNum,dicEntAliasAbr):
    #print("EntitiesTypeList=",EntitiesTypeList)
    #print("EnNum=",EnNum)

    Temp=[]
    list1=[]
    for k2 in range(EnNum):
        tempList=EntitiesTypeList[k2]
        stages = []
        for i in tempList:
            a = list(i[0:1])
            b = list(i[1:2])
            a = [str(i) for i in a]
            b = [str(i) for i in b]
            #print("a=",a)
            #print("b=",b)
            lst_tuple = list(zip(a, b))
            #print("lst_tuple=",lst_tuple)
            stages.extend(lst_tuple)

        #print("stages=",stages)
        def join_tuple_string(strings_tuple) -> str:
            return '_'.join(strings_tuple)

        result = map(join_tuple_string, stages)
        #print("result=",result)
        final1 = list(result)
        #print("final1=",final1)
        final1.sort()
        preFix1 = list(dicEntAliasAbr.values())[k2]
        #print(preFix1)
        model_entities_derived = [s for s in final1]
        model_entities_derived_temp = [s for s in final1]

        list1.extend(model_entities_derived)
        Temp.append(model_entities_derived_temp)



    return list1, Temp



def combining_IDs_List_func(EnNum, myListA, myListB):
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    myList = []
    for i in range(EnNum):
        k1 = myList1[i]
        k2 = myList2[i]
        k1.extend(k2)
        myList.append(k1)

    return myList


def color_combine(combining_IDs_List):
    k = -1
    list2 = []
    for i in range(len(combining_IDs_List)):
        list1 = []
        for j in range(len(combining_IDs_List[i])):
            list1.append(k + 1)
            k = k + 1
        list2.append(list1)

    return list2


def entity_basedon_column(EnNum, myListA, myListB):
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    myList = []
    for i in range(EnNum):
        k1 = myList1[i]
        k2 = myList2[i]
        k1.extend(k2)
        myList.append(k1)

    return myList


def entity_basedon_column_2(EnNum, myListA, myListB):
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    myList = []
    for i in range(EnNum):
        k1 = myList1[i]
        k2 = myList2[i]
        k1.extend(k2)
        myList.append(k1)

    return myList


def final_DFG_List_Absolute(EnNum, myListA, myListB):
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    # print("myList1=",myList1)
    # print("myList2=",myList2)
    myList = []
    for i in range(EnNum):
        k1 = myList1[i]
        # print("k1=", k1)
        t1 = myList2[i]
        # print("k3=", t1)
        e3 = list(itertools.product(k1, t1))
        e4 = [list(tup) for tup in e3]
        # print("e4=", e4)
        myList.append(e4)
    return myList


def final_DFG_List_Absolute_2(EnNum, myListA, myListB, myListC):
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    myList3 = copy.deepcopy(myListC)
    # print("myList1=",myList1)
    # print("myList2=",myList2)
    myList = []
    for i in range(EnNum):
        k1 = myList1[i]
        # print("k1=", k1)
        t1 = myList2[i]
        # print("k3=", t1)
        s1 = myList3[i]
        # print("s1=", s1)
        e3 = list(itertools.product(k1, t1))
        e4 = [list(tup) for tup in e3]
        # print("e4=", e4)
        for f in range(len(e4)):
            e4[f].append(s1[f])
        myList.append(e4)
    return myList


def two_pair_permutations(myList):
    result = list(chain.from_iterable([permutations(myList, x) for x in range(len(myList) + 1)]))
    result = [list(k) for k in result]

    final = []
    for i in result:
        if len(i) == 2:
            final.append(i)

    return final


def combining_two_list(myListA, myListB):
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)

    myList = []
    for i in myList1:
        # print(i)
        for j in myList2:
            # print(j)
            if i[1] == j[0]:
                i.extend(j)
                i.pop(1)
        # print(i)
        myList.append(i)

    return myList


def Final_AG_forListID(En1, En2, idColumnAndValue):
    list2 = []
    list2.append(En1)
    list2.append(En2)
    for i in range(len(idColumnAndValue)):
        if En2 == idColumnAndValue[i][0]:
            list2.append(idColumnAndValue[i][1])
    return list2





def discrete_combination_fun(myListA):
    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    myList1 = copy.deepcopy(myListA)
    myList2 = []
    # print(myList1)
    if myList1:
        for i in range(len(myListA)):
            s1 = []
            s2 = []
            s3 = []
            k1 = myList1[i][0]
            k2 = myList1[i][1]
            s1.insert(0, k1)
            s2.insert(0, k2)
            s3.append(s1)
            s3.append(s2)
            myList2.append(s3)
    else:
        myList2 = []

    return myList2


def EntityOrgAG3_Func(myListA, myListB):
    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    # print("myList1=",myList1)
    # print("myList2=", myList2)
    listFinal = []
    for i in range(len(myList2)):
        # print("AAAAAAAAAAAAAAAAAAAAa")
        item1myList2 = myList2[i][0][0]
        # print("item1myList2=", item1myList2)
        for j in range(len(myList1)):
            item1myList1 = myList1[j][0]
            # print("item1myList1=", item1myList1)
            if item1myList2 == item1myList1:
                # print("yes")
                myList2[i].append(myList1[j][1:])
                # print(myList2[i])
        listFinal.append(myList2[i])

    return listFinal


def EntityOrgAG3_Func_2(myListA, myListB, myListC):
    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    myList3 = copy.deepcopy(myListC)
    # print("myList1=",myList1)
    # print("myList2=", myList2)
    listFinal = []
    for i in range(len(myList2)):
        # print("AAAAAAAAAAAAAAAAAAAAa")
        item1myList2 = myList2[i][0][0]
        # print("item1myList2=", item1myList2)
        for j in range(len(myList1)):
            item1myList1 = myList1[j][0]
            item1myList3 = myList3[j][0]
            # print("item1myList1=", item1myList1)
            if item1myList2 == item1myList1:
                # print("yes")
                myList2[i].append(myList1[j][1:])
                # print(myList2[i])
            if item1myList2 == item1myList3:
                # print("yes")
                myList2[i].append(myList3[j][1:])
                # print(myList2[i])

        listFinal.append(myList2[i])

    return listFinal


def final_DFG_List_func(myListA):
    myList1 = copy.deepcopy(myListA)
    # print("myList1=",myList1)
    # print("len(myList1)=", len(myList1))

    if myList1:
        myList = []
        for i in range(len(myList1)):
            k1 = myList1[i][0]
            k2 = myList1[i][1]
            t1 = myList1[i][2]
            # print("k1=", k1)
            # print("k2=", k2)
            # print("t3=", t1)
            e3 = list(itertools.product(k1, k2, t1))
            e4 = [list(tup) for tup in e3]
            # print("e4=", e4)
            myList.append(e4)
    else:
        myList = []

    return myList


def final_DFG_List_func_2(myListA):
    myList1 = copy.deepcopy(myListA)
    # print("myList1=",myList1)
    # print("len(myList1)=", len(myList1))

    if myList1:
        myList = []
        for i in range(len(myList1)):
            k1 = myList1[i][0]
            k2 = myList1[i][1]
            t1 = myList1[i][2]
            s1 = myList1[i][3]

            # print("k1=", k1)
            # print("k2=", k2)
            # print("t3=", t1)
            e3 = list(itertools.product(k1, k2, t1))
            e4 = [list(tup) for tup in e3]
            # print("e4=", e4)

            for f in range(len(e4)):
                e4[f].append(s1[f])

            myList.append(e4)
    else:
        myList = []

    return myList



def final_DFG_6( model_relations, Type6_Rel_1_DF_Show , Type6_Rel_2_DF_Show):
    myList1 = copy.deepcopy(model_relations)
    en1=Type6_Rel_1_DF_Show
    en2=Type6_Rel_2_DF_Show
    list2=[]
    for i in range(len(myList1)):
        list1=[]
        k1 = myList1[i][0]
        k2 = myList1[i][1]
        k3 = myList1[i][2]
        k4 = myList1[i][3]
        k5 = myList1[i][4]
        if en1 == k5:
            list1.append(k2)
            list1.append(k3)
            list1.append(k4)
            list1.append(k5)
            list1.append(en2)
            list2.append(list1)
    return list2


def final_DFG_7( model_relations, Type7_Rel_1_DF_Show , Type7_Rel_2_DF_Show,Type7_Rel_1_Node):
    myList1 = copy.deepcopy(model_relations)
    en1=Type7_Rel_1_DF_Show
    en2=Type7_Rel_2_DF_Show
    en3=Type7_Rel_1_Node
    list2=[]
    for i in range(len(myList1)):
        list1=[]
        k1 = myList1[i][0]
        k2 = myList1[i][1]
        k3 = myList1[i][2]
        k4 = myList1[i][3]
        k5 = myList1[i][4]
        if en1 == k5:
            list1.append(k2)
            list1.append(k3)
            list1.append(k4)
            list1.append(k5)
            list1.append(en2)
            list1.append(en3)
            list2.append(list1)
    return list2


def final_DFG_property_7(A, A1 ,A2 ,A3):
    original_list=[A, A1 ,A2 ,A3]
    result_list = [[original_list[0], item] for item in original_list[1:]]
    return result_list






def final_DFG_extend( lsit1, list2 ):
    myList1 = copy.deepcopy(lsit1)
    myList2 = copy.deepcopy(list2)

    myList1.extend(myList2)
    return myList1


def final_DFG_8( model_relations, Type8_Rel_1_DF_Show , Type8_Rel_2_DF_Show,Type8_Rel_3_DF_Show):
    myList1 = copy.deepcopy(model_relations)
    en1=Type8_Rel_1_DF_Show
    en2=Type8_Rel_2_DF_Show
    en3=Type8_Rel_3_DF_Show
    #print("en1=", en1)
    #print("en2=", en2)
    #print("en3=", en3)


    # print("len(myList1)=", len(myList1))
    list2=[]
    for i in range(len(myList1)):
        list1=[]
        k1 = myList1[i][0]
        k2 = myList1[i][1]
        k3 = myList1[i][2]
        k4 = myList1[i][3]
        k5 = myList1[i][4]

        # print("k1=", k1)
        # print("k2=", k2)
        # print("t3=", t1)
        if en2 == k5:
            list1.append(k1)
            list1.append(k2)
            list1.append(k3)
            list1.append(k4)
            list1.append(en1)
            list1.append(en2)
            list1.append(en3)
            list2.append(list1)
    return list2


def create_string_list(Type8_Rel_1_DF_Show, Type8_Rel_2_DF_Show, Type8_Rel_3_DF_Show):
    string_list = [Type8_Rel_1_DF_Show, Type8_Rel_2_DF_Show, Type8_Rel_3_DF_Show]
    return string_list

def EntityAndEntityOrg_Creater_Final(EntityOriginIDValue, EnNum, dicEnt,dicEntAliasAbr):
    #print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    list6=[]
    for k1 in range(EnNum):
        EntityOrgValue=EntityOriginIDValue[k1]
        EntityEntCol = list(dicEnt.values())[k1]
        EntityAliasCol = list(dicEntAliasAbr.values())[k1]
        list5 = []

        for i in EntityOrgValue:
            list4=[]
            list4.append(EntityAliasCol)
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



def node1Finder(driver):
    query1 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE NOT EXISTS {{ (x)-[:INCLUDED]->(n) }} and n.Category="Absolute"
    RETURN  COLLECT (distinct LABELS(n))
    '''
    #print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        #print("record1=", record1)
        flat_list = record1[0][0]
        flattened_list = [label for sublist in flat_list for label in sublist]

    return flattened_list



def nodeLastFinder(driver):
    query1 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE NOT EXISTS {{ (z)-[:INCLUDED]->(y) }} and z.Category="Absolute"
    RETURN  COLLECT (distinct LABELS(z))
    '''
    #print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        #print("record1=", record1)
        flat_list = record1[0][0]
        flattened_list = [label for sublist in flat_list for label in sublist]

    return flattened_list



def otherLastFinder(driver):
    query1 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE NOT EXISTS {{ (x)-[:INCLUDED]->(n) }} and n.Category="Absolute"
    RETURN  COLLECT (distinct LABELS(n))
    '''
    #print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        #print("record1=", record1)
        flat_list = record1[0][0]
        flattened_list = [label for sublist in flat_list for label in sublist]



    query2 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE NOT EXISTS {{ (z)-[:INCLUDED]->(y) }} and z.Category="Absolute"
    RETURN  COLLECT (distinct LABELS(z))
    '''
    #print(query1)
    with driver.session() as session:
        record2 = session.run(query2).values()
        #print("record1=", record1)
        flat_list2 = record2[0][0]
        flattened_list2 = [label for sublist in flat_list2 for label in sublist]




    query3 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE z.Category="Absolute" and n.Category="Absolute"
    RETURN COLLECT(DISTINCT LABELS(z)) + COLLECT(DISTINCT LABELS(n)) AS combinedLabels
    '''
    #print(query1)
    with driver.session() as session:
        record3 = session.run(query3).values()
        #print("record3=", record3)
        flat_list3 = record3[0][0]
        flattened_list3 = [label for sublist in flat_list3 for label in sublist]
        no_duplicates_list = list(set(flattened_list3))

    #print(no_duplicates_list)

    result1 = [item for item in no_duplicates_list if item not in flattened_list]
    result2 = [item for item in result1 if item not in flattened_list2]




    return result2




def maxLengthFinder(driver):
    query1 = f'''     
    MATCH path = (start)-[:INCLUDED*]->(end)
    WHERE NOT ()-[:INCLUDED]->(start) AND NOT (end)-[:INCLUDED]->()
    RETURN LENGTH(path) AS maxLength
    ORDER BY maxLength DESC
    LIMIT 1
    '''
    #print(query1)

    with driver.session() as session:
        record1 = session.run(query1).values()
        if record1:
            #print("record1=", record1)
            flat_list = record1[0][0]
        else:
            flat_list = None

    return flat_list

def node2Finder(driver, node1):
    list1=[]
    for item in node1:
        list3=[]
        list2=[item]
        list3.append(list2)
        #print(list3)
        query1 = f'''     
        MATCH (n:{item})-[:INCLUDED]->(z)
        WHERE  z.Category="Absolute"
        RETURN  COLLECT (distinct LABELS(z))
        '''
        #print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            #print("record1=", record1)
            flat_list = record1[0][0]
            flattened_list = [label for sublist in flat_list for label in sublist]
            list3.append(flattened_list)
            #print(list3)
        list1.append(list3)

    return list1


def node3Finder(driver, node1, nodeLast,maxLength):
    list1=[]
    for item in node1:
        list3=[]
        list2=[item]
        list3.append(list2)
        #print(list3)
        query1 = f'''     
        MATCH (n:{item})-[:INCLUDED]->(z)
        WHERE  z.Category="Absolute"
        RETURN  COLLECT (distinct LABELS(z))
        '''
        #print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            #print("record1=", record1)
            flat_list = record1[0][0]
            flattened_list = [label for sublist in flat_list for label in sublist]
            list3.append(flattened_list)
            #print(list3)
        list1.append(list3)
    #print("list1=",list1)

    for each in list1:
        for item in each[1]:
            #print(item)
            if item not in nodeLast:
                #print("yes")
                list3 = []
                list2 = [item]
                list3.append(list2)
                # print(list3)
                query1 = f'''     
                MATCH (n:{item})-[:INCLUDED]->(z)
                WHERE  z.Category="Absolute"
                RETURN  COLLECT (distinct LABELS(z))
                '''
                # print(query1)
                with driver.session() as session:
                    record1 = session.run(query1).values()
                    # print("record1=", record1)
                    flat_list = record1[0][0]
                    flattened_list = [label for sublist in flat_list for label in sublist]
                    list3.append(flattened_list)
                    # print(list3)

                list1.append(list3)
                #print("list11=",list1)


    return list1



def converted_lister(node):
    converted_nodeOther = [[first, [second]] for first, seconds in node for second in seconds]
    converted_list = [first + second for first, second in converted_nodeOther]

    return converted_list


def pathFinder(node):

    list1=[]
    for x in range(len(node)):
        i=node[x]
        #print(x)
        #print("i=",i)
        list1.append(node[x])
        #print("i[-1]=",i[-1])
        for j in node[x+1:]:
            #print(j)
            #print("j[0]=", j[0])

            if i[-1] == j[0]:
                #print("i=", i)
                #print("j=", j)
                index_of_b = node.index(j)
                #print("index_of_b=",index_of_b)
                j=i[:-1]+j
                #print("newJ=", j)

                node[index_of_b] = j
                #print(node)
    return node


def nodeExcluder(driver):
    query1 = f'''     
    MATCH p=(a)-[r:LINKED_TO]->(b)
    RETURN  COLLECT (distinct LABELS(a))
    '''
    # print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        if record1 != [[[]]]:
            print("record1=", record1)
            flat_list = record1[0][0][0]
        else:
            flat_list = None
    return flat_list


def creatingDfFromGraph(driver, pathNode,excludedNode):
    list1=[]
    for item in pathNode:
        #print(item)
        new = item.copy()
        n=(len(item))
        z=item[-1]
        if z not in excludedNode:
            my_list = [f'a{i}' for i in range(1, n + 1)]
            x=my_list[-1]
            if len(my_list)==2: k=my_list[0]
            if len(my_list)!=2: k=my_list[1]
            my_list = [i+":" for i in my_list]

            #print(my_list)
            for i in range(min(len(item), len(my_list))):
                item[i] = "(" + my_list[i] + item[i] + ")"
            #print(item)
            part1=' -[:INCLUDED]- '.join(item)
            part1b= "MATCH (e)-[:CORR]-> " + part1
            part2=f'''RETURN a1.ID AS Patient, {x}.ID AS {z}, e.timestamp AS Time;'''
            #print(part1b)
            #print(part2)


            query1 = f'''     
            {part1b}
            {part2}
            '''
            #print(query1)
            with driver.session() as session:
                record = session.run(query1).values()
                #print("record=", record)
            x=[]
            for each in record:
                #print(each)
                each[2] = each[2].isoformat()
                #print(each)
                x.append(each)

            df = pd.DataFrame(x, columns=['Patient', z, 'Time'])

            #print(df)

            columns_order = ['Patient', z, 'Time']
            new_df = df[columns_order]
            result = new_df.groupby(['Patient', z])['Time'].max().reset_index(name='MaxT')
            #print(result)
            result_sorted = result.sort_values(by=['Patient', 'MaxT'])
            #print(result_sorted)
            # Group by 'A1', 'A2', and 'C' and use cumcount to create the 'Row' column

            result_sorted['Row'] = result_sorted.groupby(['Patient']).cumcount(z) + 1
            #print(result_sorted)
            fianl_df = result_sorted[['Patient', z,'Row']]
            # Now, df includes the 'Row' column as in Table2

            conditioned_sorted_df = fianl_df.sort_values(by=['Patient', 'Row'])
            #print(conditioned_sorted_df)
            result = conditioned_sorted_df.groupby(['Patient'])[z].agg(','.join).reset_index(name=z)
            original_list = result.values.tolist()

            # Convert the original list into the desired format
            converted_list = [
                [[sublist[0]],
                 [[sublist[1].split(',')[i], sublist[1].split(',')[i + 1]] for i in range(len(sublist[1].split(',')) - 1)]]
                for sublist in original_list
            ]

            # Convert the original list into the desired format
            converted_list1 = [[[sublist[0][0]], pair] for sublist in converted_list for pair in sublist[1]]

            updated_list = [[z[0], new, z[1] , [part1b], [k]] for z in converted_list1]
            #print("updated_list=",updated_list)
            if updated_list :
                list1.append(updated_list)
            #print(list1)

    return list1


def txtExistanceQ(FilaeName):
    import os
    confDirectory  = "../Data/0_qRelationship"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + FilaeName + ".txt"

    if os.path.exists(DFG_FilePath):
        return True
    else:
        return False


def TypeCount(FilaeName, searchText):
    import os
    import ast
    confDirectory  = "../Data/0_qRelationship"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"

    with open(DFG_FilePath, 'r') as file:
        for line in file:
            if line.startswith(searchText):
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                if variable_name == searchText:
                    value = value.strip()
                    value = ast.literal_eval(value)
                    TypeApproach = value
    return TypeApproach



def TrueFalseTxt(FilaeName, searchText):
    import os
    confDirectory  = "../Data/0_qRelationship"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"

    with open(DFG_FilePath, 'r') as file:
        for line in file:
            if line.startswith(searchText):
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                if variable_name == searchText:
                    value = value.strip()
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    case_selector_activation = value
    return case_selector_activation


def listIntTxt(FilaeName, searchText):
    import os
    import ast
    confDirectory  = "../Data/0_qRelationship"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"

    with open(DFG_FilePath, 'r') as file:
        for line in file:
            if line.startswith(searchText):
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                if variable_name == searchText:
                    value = value.strip()
                    value = ast.literal_eval(value)
                    Type1_selection_ID = value
    return Type1_selection_ID

def stringTxt(FilaeName, searchText):
    import os
    import ast
    confDirectory  = "../Data/0_qRelationship"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"

    with open(DFG_FilePath, 'r') as file:
        for line in file:
            if line.startswith(searchText):
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                if variable_name == searchText:
                    value = value.strip()
                    Type1_selection_ID = value
    return Type1_selection_ID
